<script setup>
import imagePath from "@/assets/img/search.jpg";
import useAxios from "../composables/useAxios";
import { useReportStore } from "../stores/report";
import { ref, onMounted } from "vue";

const reportStore = useReportStore();
const axios = useAxios();

const nextPage = ref(null);
const previousPage = ref(null);
const currentPage = ref(1);
const totalPage = ref(0);
const categorys = ref({});
const data = ref({
  author: "",
  category: "",
  title: "",
  year: "",
  month: "",
  day: "",
});

const reports = ref({});

const handleSubmit = async () => {
  console.log(data.value);
  const response = await axios.get("http://localhost:8000/search", {
    params: data.value,
  });

  reportStore.data = response.data;
  reports.value = reportStore.data.results;
  nextPage.value = reportStore.data.links.next;
  previousPage.value = reportStore.data.links.previous;
  totalPage.value = reportStore.data.total_pages;
  console.log(reportStore.data);
  console.log("TOT: ", totalPage.value);
};

const getDateTime = (timeDate) => {
  const year = timeDate.getFullYear();
  const month = ("0" + (timeDate.getMonth() + 1)).slice(-2);
  const date = ("0" + timeDate.getDate()).slice(-2);
  const hours = ("0" + timeDate.getHours()).slice(-2);
  const minutes = ("0" + timeDate.getMinutes()).slice(-2);
  const seconds = ("0" + timeDate.getSeconds()).slice(-2);

  const time = `${year}-${month}-${date} ${hours}:${minutes}:${seconds}`;

  return time;
};

const changePageNumber = async (page) => {
  const response = await axios.get(
    `http://localhost:8000/search/?author=${data.value.author}&category=${data.value.category}&day=${data.value.day}&month=${data.value.month}&page=${page}&title=${data.value.title}&year=${data.value.year}`
  );
  console.log(response);
  currentPage.value = page;
  reportStore.data = response.data;
  reports.value = reportStore.data.results;
  nextPage.value = reportStore.data.links.next;
  previousPage.value = reportStore.data.links.previous;
  totalPage.value = reportStore.data.total_pages;
};

const changeToNextPage = async () => {
  // nextPage.value = nextPage.value.replace("http://localhost:8000", "api");

  const response = await axios.get(nextPage.value);

  currentPage.value += 1;
  reportStore.data = response.data;
  reports.value = reportStore.data.results;
  nextPage.value = reportStore.data.links.next;
  previousPage.value = reportStore.data.links.previous;
  totalPage.value = reportStore.data.total_pages;
};

const changeToPreviousPage = async () => {
  // previousPage.value = previousPage.value.replace(
  //   "http://localhost:8000",
  //   "api"
  // );

  const response = await axios.get(previousPage.value);

  currentPage.value -= 1;
  reportStore.data = response.data;
  reports.value = reportStore.data.results;
  nextPage.value = reportStore.data.links.next;
  previousPage.value = reportStore.data.links.previous;
  totalPage.value = reportStore.data.total_pages;
};

onMounted(async () => {
  if (reportStore.data.results) {
    reports.value = reportStore.data.results;
    nextPage.value = reportStore.data.links.next;
    previousPage.value = reportStore.data.links.previous;
  }

  const response = await axios.get(
    "http://localhost:8000/reports/category/list_create/"
  );
  categorys.value = response.data;
});
</script>

<template>
  <section
    id="showcase-inner"
    class="showcase-search text-white py-5"
    v-bind:style="{
      background: 'center / cover no-repeat url(' + imagePath + ')',
    }"
  >
    <div class="plane"></div>
    <div class="container">
      <div class="row text-center">
        <div class="col-md-12">
          <form action="/" @submit.prevent="handleSubmit">
            <!-- Form Row 1 -->
            <div class="form-row">
              <div class="col-md-4 mb-3">
                <label class="sr-only">Title</label>
                <input
                  type="text"
                  name="title"
                  v-model="data.title"
                  class="form-control"
                  placeholder="Title"
                />
              </div>

              <div class="col-md-4 mb-3">
                <label class="sr-only">Author</label>
                <input
                  type="text"
                  name="author"
                  v-model="data.author"
                  class="form-control"
                  placeholder="Author"
                />
              </div>
              <div class="col-md-4 mb-3">
                <label class="sr-only">Year</label>
                <select
                  name="category"
                  class="form-control"
                  v-model="data.category"
                >
                  <option selected="true" disabled="disabled">
                    Select Category
                  </option>
                  <option value=""></option>
                  <template v-for="category in categorys">
                    <option :value="category.id">
                      {{ category.category }}
                    </option></template
                  >
                </select>
              </div>
            </div>
            <!-- Form Row 2 -->
            <div class="form-row">
              <div class="col-md-4 mb-3">
                <label class="sr-only">Created Year</label>
                <input
                  type="text"
                  name="year"
                  class="form-control"
                  placeholder="Year"
                />
              </div>
              <div class="col-md-4 mb-3">
                <label class="sr-only">Created Month</label>
                <input
                  type="text"
                  name="month"
                  class="form-control"
                  placeholder="Month"
                />
              </div>
              <div class="col-md-4 mb-3">
                <label class="sr-only">Created Day</label>
                <input
                  type="text"
                  name="day"
                  class="form-control"
                  placeholder="Day"
                />
              </div>
            </div>
            <button
              class="submit-button btn btn-primary btn-block mt-4"
              type="submit"
            >
              Search
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- Breadcrumb -->
  <section id="bc" class="mt-3">
    <div class="container">
      <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <router-link to="/"
              ><font-awesome-icon icon="fa-solid fa-house-chimney" size="xs" />
              Home</router-link
            >
          </li>
          <li class="breadcrumb-item">
            <router-link to="/listings"> Browse Listings</router-link>
          </li>
          <li class="breadcrumb-item active">Search Results</li>
        </ol>
      </nav>
    </div>
  </section>

  <!-- Listings -->
  <section id="listings" class="py-4">
    <div class="container">
      <div class="row">
        <template v-if="reports">
          <div class="col-md-6 col-lg-4 mb-4" v-for="report in reports">
            <div class="card listing-preview">
              <div class="card-body">
                <div class="listing-heading text-center">
                  <h4 class="text-primary">{{ report.title }}</h4>
                  <p>
                    <font-awesome-icon
                      icon="fa-brands fa-leanpub"
                      style="color: #2f6ad0"
                    />
                    {{ report.category.category }}
                  </p>
                </div>
                <hr />

                <div class="row text-secondary pb-2">
                  <div>
                    <font-awesome-icon
                      icon="fa-solid fa-clock"
                      style="color: #5dee95"
                    />
                    {{ getDateTime(new Date(report.create_time)) }}
                  </div>
                </div>
                <hr />
                <h2>
                  <span class="badge badge-secondary text-white">{{
                    report.author.username
                  }}</span>
                </h2>
                <router-link
                  :to="`listings/${report.id}/`"
                  class="btn btn-primary btn-block"
                >
                  More Info</router-link
                >
              </div>
            </div>
          </div>
        </template>
        <template v-else
          ><div class="col-md-12">
            <p>No Listings Available</p>
          </div></template
        >
      </div>

      <div class="row">
        <div class="col-md-12">
          <ul class="pagination">
            <template v-if="previousPage">
              <li class="page-item">
                <a @click="changeToPreviousPage" class="page-link">&laquo;</a>
              </li>
            </template>
            <template v-else>
              <li class="page-item disabled">
                <a class="page-link">&laquo;</a>
              </li>
            </template>
            <template v-for="page in totalPage">
              <template v-if="page == currentPage">
                <li class="page-item active">
                  <a class="page-link">{{ page }}</a>
                </li>
              </template>
              <template v-else>
                <li class="page-item">
                  <a @click="changePageNumber(page)" class="page-link">{{
                    page
                  }}</a>
                </li></template
              >
            </template>
            <template v-if="nextPage">
              <li class="page-item">
                <a @click="changeToNextPage" class="page-link">&raquo;</a>
              </li>
            </template>
            <template v-else>
              <li class="page-item disabled">
                <a class="page-link">&raquo;</a>
              </li>
            </template>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
#showcase-inner {
  position: relative;
  overflow: hidden;
  min-height: 200px;
  background-color: rgba(51, 51, 51, 1);
}

.submit-button {
  background-color: #a4b2ff;
  color: white;
}

div.plane {
  width: 100%;
  min-height: 70vh;
  background-color: rgba(0, 0, 0, 0.5);
  position: absolute;
  top: 0;
  right: 0;
  /* z-index: -1; */
}

.page-item {
  user-select: none;
}
</style>
