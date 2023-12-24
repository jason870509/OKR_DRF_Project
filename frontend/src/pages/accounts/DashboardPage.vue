<script setup>
import { onMounted, ref } from "vue";
import { useUserStore } from "../../stores/user";
import useAxios from "../../composables/useAxios";

const axios = useAxios();
const userStore = useUserStore();
const reports = ref({});
const categorys = ref({});

const showHide = (e) => {
  const list = e.target.nextElementSibling;

  try {
    if (list.style.display === "block") {
      list.style.display = "none";
    } else {
      list.style.display = "block";
    }
  } catch (err) {}
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

const getReportsData = async () => {
  const data = await axios.get("/api/reports/list_create/");
  reports.value = data.data;
};

const getCategory = async () => {
  const response = await axios.get("/api/reports/category/list_create/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  categorys.value = response.data;

  if (categorys.value) {
    Object.keys(categorys.value).forEach((key) => {
      categorys.value[key].count = 0;
    });
  }

  if (reports.value) {
    for (const report of reports.value) {
      categorys.value[report.category.id - 1].count += 1;
    }
  }
};

onMounted(async () => {
  const response = await axios.get("/api/reports/list_personal/", {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("access")}`,
    },
  });
  reports.value = response.data;

  await getCategory();
});
</script>

<template>
  <section id="showcase-inner" class="py-5 text-white">
    <div class="container">
      <div class="row text-center">
        <div class="col-md-12">
          <h1 class="display-4">User Dashboard</h1>
          <p class="lead">Manage your reports upload website's account</p>
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
          <li class="breadcrumb-item active">Dashboard</li>
        </ol>
      </nav>
    </div>
  </section>

  <section id="dashboard" class="py-4">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h2>Welcome {{ userStore.username }}</h2>
          <template v-if="reports">
            <p>Here are the property listing reports that you have uploaded.</p>
            <ol class="list-group">
              <template v-for="(category, index) in categorys">
                <li
                  @click="showHide"
                  id="category-list"
                  class="list-group-item d-flex justify-content-between align-items-start"
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
                        id="report-list"
                        class="list-group-item d-flex justify-content-between align-items-start"
                      >
                        <div class="ms-2 me-auto">
                          <div
                            class="fw-bold"
                            style="font-weight: bold; font-size: 20px"
                          >
                            <a
                              :href="report.file_path"
                              download
                              target="_blank"
                              >{{ report.title }}</a
                            >
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
          </template>
          <template v-else><p>You have not made any inquiries</p></template>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
#dashboard {
  margin-bottom: 10rem;
}

#showcase-inner {
  background-color: rgb(52, 58, 64);
}

#category-list {
  background: linear-gradient(to right, #2f6ad0, rgba(194, 233, 206, 0.667));
  color: black;
  cursor: pointer;
  padding: 20px;
}

#report-list:hover {
  background: rgba(228, 228, 228, 0.667);
  color: black;
  cursor: pointer;
}

#category-list:hover {
  background: linear-gradient(to right, #095ef0, rgba(74, 243, 125, 0.667));
}
</style>
