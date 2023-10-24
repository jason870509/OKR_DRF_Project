<script setup>
import { onMounted, ref } from "vue";
import useAxios from "../composables/useAxios";

const axios = useAxios();
const formCategory = ref(null);
const categorys = ref({});
const reports = ref({});
const nowTime = ref(new Date());

const showHide = (e) => {
  const list = e.target.nextElementSibling;

  if (list.style.display === "block") {
    list.style.display = "none";
  } else {
    list.style.display = "block";
  }
};

const data = ref({
  author: "",
  category: "",
  description: "",
  title: "",
  file_path: null,
});

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

const getReportsData = async () => {
  console.log("123");
  const data = await axios.get("http://localhost:8000/reports/list_create/");
  reports.value = data.data;
};

const getCategory = async () => {
  const response = await axios.get(
    "http://localhost:8000/reports/category/list_create/"
  );
  categorys.value = response.data;

  Object.keys(categorys.value).forEach((key) => {
    categorys.value[key].count = 0;
  });

  for (const report of reports.value) {
    categorys.value[report.category.id - 1].count += 1;
  }
};

const handleSumbit = async () => {
  console.log(data.value);
  const response = await axios.post("api/reports/list_create/", data.value, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  console.log(response);
};

const onFileChange = (e) => {
  const files = e.target.files || e.dataTransfer.files;
  if (!files.length) return;
  data.value.file_path = files[0];
  console.log(data.value);
};

onMounted(async () => {
  await getReportsData();

  await getCategory();
  // nowTime.value = getNowTime();
});
</script>
<template>
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
          <li class="breadcrumb-item active">Reports</li>
        </ol>
      </nav>
    </div>
  </section>

  <section id="reports" class="py-4">
    <div class="container">
      <ol class="list-group">
        <template v-for="(category, index) in categorys">
          <li
            @click="showHide"
            class="list-group-item d-flex justify-content-between align-items-start"
            style="
              background-color: #4ca4fd;
              color: black;
              cursor: pointer;
              padding: 20px;
            "
          >
            <div class="ms-2 me-auto">
              <div class="fw-bold">{{ category.category }}</div>
            </div>
            <span
              class="badge bg-primary rounded-pill"
              style="color: antiquewhite"
              >{{ category.count }}</span
            >
          </li>
          <ol class="list-group" style="display: none">
            <template v-for="report in reports">
              <template v-if="index + 1 == report.category.id">
                <li
                  class="list-group-item d-flex justify-content-between align-items-start"
                >
                  <div class="ms-2 me-auto">
                    <div
                      class="fw-bold"
                      style="font-weight: bold; font-size: 20px"
                    >
                      <a :href="report.file_path" download target="_blank">{{
                        report.title
                      }}</a>
                    </div>
                    <br />
                    {{ report.description }}
                  </div>
                  <span
                    class="badge bg-primary rounded-pill"
                    style="color: antiquewhite"
                  >
                    {{ getDateTime(new Date(report.create_time)) }}
                  </span>
                </li>
              </template>
            </template>
          </ol>
        </template>
      </ol>
    </div>
  </section>

  <!-- Work -->
  <!-- {% if user.is_authenticated %} -->
  <section id="work" class="bg-dark text-white">
    <div class="text-center">
      <h2 class="display-4">Complete Form & Upload</h2>
      <h4>Upload your Report files</h4>
    </div>

    <form enctype="multipart/form-data" @submit.prevent="handleSumbit">
      <!-- {% csrf_token %} -->
      <div class="container">
        <div class="input-group flex-nowrap mb-3">
          <span class="input-group-text">@</span>
          <input
            type="text"
            class="form-control"
            placeholder="Author"
            name="author"
            aria-describedby="addon-wrapping"
            v-model="data.author"
          />
        </div>

        <div class="mb-3">
          <label for="category" class="form-label">Category : </label>
          <select
            name="category"
            class="form-control"
            v-model="data.category"
            placeholder="Select Report Category"
          >
            <option selected disabled="disabled">Select Report Category</option>
            <template v-for="category in categorys">
              <option :value="category.id">
                {{ category.category }}
              </option>
            </template>
          </select>
        </div>

        <div class="mb-3">
          <label for="title" class="form-label">Title : </label>
          <div class="input-group flex-nowrap mb-3">
            <span class="input-group-text">@</span>
            <input
              type="text"
              class="form-control"
              placeholder="Title"
              name="title"
              aria-describedby="addon-wrapping"
              v-model="data.title"
            />
          </div>
        </div>
        <div class="mb-3">
          <label for="description" class="form-label">Description : </label>
          <div class="input-group flex-nowrap mb-3">
            <span class="input-group-text">@</span>
            <textarea
              type="text"
              class="form-control"
              placeholder="Description"
              name="description"
              aria-describedby="addon-wrapping"
              v-model="data.description"
            />
          </div>
        </div>
        <div class="mb-3">
          <label class="input-group flex-nowrap mb-3" for="file"
            >Upload :
          </label>
          <div class="input-group mb-3">
            <input
              type="file"
              class="form-control"
              id="inputGroupFile02"
              name="file"
              @change="onFileChange"
            />
          </div>
        </div>
      </div>
      <hr />
      <div class="text-center">
        <button
          class="submit-button btn btn-primary text-white btn-lg"
          type="submit"
        >
          Upload
        </button>
      </div>
    </form>
  </section>
</template>

<style scoped>
#work {
  padding-bottom: 6rem;
}
.submit-button {
  background-color: #796fff;
}

ol {
  transition: all 0.3s ease;
}
</style>
