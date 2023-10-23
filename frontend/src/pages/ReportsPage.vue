<script setup>
import { ref } from "vue";
const formCategory = ref(null);
const categorys = ref([
  { id: 1, category: "Testing" },
  { id: 2, category: "Meeting" },
  { id: 3, category: "Others" },
]);
const reports = ref([
  {
    id: 1,
    category_id: 1,
    title: "Testing 1",
    description: "admin added 1.",
    create_at: "2023-10-15",
  },
  {
    id: 2,
    category_id: 2,
    title: "Meeting 1",
    description: "admin added 1.",
    create_at: "2023-10-15",
  },
  {
    id: 3,
    category_id: 2,
    title: "Meeting 2",
    description: "admin added 2.",
    create_at: "2023-10-15",
  },
]);

const showHide = (e) => {
  const list = e.target.nextElementSibling;

  if (list.style.display === "block") {
    list.style.display = "none";
  } else {
    list.style.display = "block";
  }
};

const dowloadReport = () => {
  return "123";
};
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
        <template v-for="category in categorys">
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
              >{{ "category.count" }}</span
            >
          </li>
          <ol class="list-group" style="display: none">
            <template v-for="report in reports">
              <li
                class="list-group-item d-flex justify-content-between align-items-start"
              >
                <div class="ms-2 me-auto">
                  <div
                    class="fw-bold"
                    style="font-weight: bold; font-size: 20px"
                  >
                    <a href="#" :download="dowloadReport">{{ report.title }}</a>
                  </div>
                  <br />
                  {{ report.description }}
                </div>
                <span
                  class="badge bg-primary rounded-pill"
                  style="color: antiquewhite"
                >
                  {{ report.create_at }}
                </span>
              </li></template
            >
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

    <form
      action="{% url 'reports' %}"
      method="post"
      enctype="multipart/form-data"
      class=""
    >
      <!-- {% csrf_token %} -->
      <div class="container">
        <div class="input-group flex-nowrap mb-3" style="display: none">
          <span class="input-group-text">@</span>
          <input
            type="text"
            class="form-control"
            placeholder="Author"
            name="author"
            aria-describedby="addon-wrapping"
            value="{{user.username}}"
          />
        </div>

        <div class="mb-3">
          <label for="category" class="form-label">Category : </label>
          <select
            name="category"
            class="form-control"
            v-model="formCategory"
            placeholder="Select Report Category"
          >
            <option selected disabled="disabled">Select Report Category</option>
            <template v-for="category in categorys">
              <option :value="category.category">
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
