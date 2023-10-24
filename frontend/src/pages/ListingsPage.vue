<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import useAxios from "../composables/useAxios";
import { useReportStore } from "../stores/report";

const reportStore = useReportStore();
const axios = useAxios();
const router = useRouter();
const categorys = ref({});
const data = ref({
  author: "",
  category: "",
  title: "",
  year: "",
  month: "",
  day: "",
});

const handleSubmit = async () => {
  const response = await axios.get("/api/search/", { params: data.value });

  reportStore.data = response.data;
  router.push("/search");
};

onMounted(async () => {
  const response = await axios.get("/api/reports/category/list_create/");
  categorys.value = response.data;
});
</script>
<template>
  <section id="search-title" class="py-5 text-white bg-dark">
    <div class="container">
      <div class="row text-center">
        <div class="col-md-12">
          <h1 class="display-4">Search for Reports</h1>
          <p class="lead">Here you can search for the report you want.</p>
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
          <li class="breadcrumb-item active">Listings</li>
        </ol>
      </nav>
    </div>
  </section>

  <section id="search_column " class="search">
    <div class="container text-center">
      <div class="overlay p-5 bg-dark">
        <h1 class="display-4 mb-4 text-white">
          Property Searching Just Got So Easy
        </h1>
        <p class="lead text-white">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae
          quas, asperiores eveniet vel nostrum magnam voluptatum tempore!
          Consectetur, id commodi!
        </p>
        <form @submit.prevent="handleSubmit">
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
              <select
                name="category"
                class="form-control"
                v-model="data.category"
              >
                <option selected="true" disabled="disabled">
                  Select Category
                </option>
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
                v-model="data.year"
                class="form-control"
                placeholder="Year"
              />
            </div>
            <div class="col-md-4 mb-3">
              <label class="sr-only">Created Month</label>
              <input
                type="text"
                name="month"
                v-model="data.month"
                class="form-control"
                placeholder="Month"
              />
            </div>
            <div class="col-md-4 mb-3">
              <label class="sr-only">Created Day</label>
              <input
                type="text"
                name="day"
                v-model="data.day"
                class="form-control"
                placeholder="Day"
              />
            </div>
          </div>
          <button class="btn btn-primary btn-block mt-4" type="submit">
            Search
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<style scoped>
.lead {
  font-size: 1.25rem;
  font-weight: 300;
}

.overlay {
  background-color: rgba(51, 51, 51, 0.8);
}

button {
  background-color: #a4b2ff;
  color: white;
}
</style>
