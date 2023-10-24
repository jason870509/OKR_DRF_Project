<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import useAxios from "../composables/useAxios";

const axios = useAxios();
const route = useRoute();
const report = ref({});

onMounted(async () => {
  console.log("123");
  const response = await axios.get(
    `http://localhost:8000/reports/${route.params.reportId}`
  );
  report.value = response.data;
  console.log(report.value);
});
</script>
<template>
  <section id="showcase-inner" class="py-5 text-white">
    <div class="container">
      <div class="row text-center">
        <div class="col-md-12">
          <h1 class="display-4">{{ report.title }}</h1>
          <p class="lead">
            <template v-if="report.category">{{
              report.category.category
            }}</template>
          </p>
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
            <router-link to="/search">Listings</router-link>
          </li>
          <li class="breadcrumb-item active">{{ report.title }}</li>
        </ol>
      </nav>
    </div>
  </section>

  <!-- Listing -->
  <section id="listing" class="py-4">
    <div class="container">
      <router-link to="/search" class="btn btn-light mb-4"
        >Back To Listings</router-link
      >

      <div class="row">
        <div class="col-md-9">
          <!-- Fields -->
          <!-- <div class="row mb-5 fields">
            <div class="col-md-6">
              <ul class="list-group list-group-flush">
                <li class="list-group-item text-secondary">
                  <i class="fas fa-money-bill-alt"></i> Asking Price:
                  <span class="float-right"
                    >${{ listing.price | intcomma }}</span
                  >
                </li>
                <li class="list-group-item text-secondary">
                  <i class="fas fa-bed"></i> Bedrooms:
                  <span class="float-right">{{ listing.bedrooms }}</span>
                </li>
                <li class="list-group-item text-secondary">
                  <i class="fas fa-bath"></i> Bathrooms:
                  <span class="float-right">{{ listing.bathrooms }}</span>
                </li>
                <li class="list-group-item text-secondary">
                  <i class="fas fa-car"></i> Garage:
                  <span class="float-right">{{ listing.garage }} </span>
                </li>
              </ul>
            </div>
            <div class="col-md-6">
              <ul class="list-group list-group-flush">
                <li class="list-group-item text-secondary">
                  <i class="fas fa-th-large"></i> Square Feet:
                  <span class="float-right">{{ listing.sqft }}</span>
                </li>
                <li class="list-group-item text-secondary">
                  <i class="fas fa-square"></i> Lot Size:
                  <span class="float-right">{{ listing.lot_size }} Acres </span>
                </li>
                <li class="list-group-item text-secondary">
                  <i class="fas fa-calendar"></i> Listing Date:
                  <span class="float-right">{{ listing.list_date }}</span>
                </li>
                <li class="list-group-item text-secondary">
                  <i class="fas fa-bed"></i> Realtor:
                  <span class="float-right">{{ listing.realtor }} </span>
                </li>
              </ul>
            </div>
          </div> -->

          <!-- Description -->
          <div class="row mb-5">
            <div class="col-md-12">
              {{ report.description }}
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="card mb-3">
            <img class="card-img-top" src="/img/user.png" alt="" />
            <div class="card-body">
              <h5 class="card-title">Author</h5>
              <template v-if="report.author">
                <h6 class="text-secondary">{{ report.author.username }}</h6>
              </template>
            </div>
          </div>
          <a :href="report.file_path" download target="_blank"
            ><button
              class="btn-primary btn-block btn-lg"
              data-toggle="modal"
              data-target="#inquiryModal"
            >
              Downloads
            </button></a
          >
        </div>
      </div>
    </div>
  </section>

  <!-- Inquiry Modal -->
  <!-- <div class="modal fade" id="inquiryModal" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="inquiryModalLabel">Make An Inquiry</h5>
          <button type="button" class="close" data-dismiss="modal">
            <span>&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form action="{% url 'contact' %}" method="POST">
            {% csrf_token %} {% if user.is_authenticated %}
            <input type="hidden" name="user_id" value="{{ user.id }}" />
            {% else %}
            <input type="hidden" name="user_id" value="0" />
            {% endif %}
            <input
              type="hidden"
              name="realtor_email"
              value="{{ listing.realtor.email }}"
            />
            <input type="hidden" name="listing_id" value="{{ listing.id }}" />
            <div class="form-group">
              <label for="property_name" class="col-form-label"
                >Property:</label
              >
              <input
                type="text"
                name="listing"
                class="form-control"
                value="{{ listing.title }}"
              />
            </div>
            <div class="form-group">
              <label for="name" class="col-form-label">Name:</label>
              <input
                type="text"
                name="name"
                class="form-control"
                {%
                if
                user.is_authenticated
                %}
                value="{{ user.first_name }} {{ user.last_name }}"
                {%
                endif
                %}
                required
              />
            </div>
            <div class="form-group">
              <label for="email" class="col-form-label">Email:</label>
              <input
                type="email"
                name="email"
                class="form-control"
                {%
                if
                user.is_authenticated
                %}
                value="{{ user.email }}"
                {%
                endif
                %}
                required
              />
            </div>
            <div class="form-group">
              <label for="phone" class="col-form-label">Phone:</label>
              <input type="text" name="phone" class="form-control" />
            </div>
            <div class="form-group">
              <label for="message" class="col-form-label">Message:</label>
              <textarea name="message" class="form-control"></textarea>
            </div>
            <hr />
            <input
              type="submit"
              value="Send"
              class="btn btn-block btn-secondary"
            />
          </form>
        </div>
      </div>
    </div>
  </div> -->
</template>

<style scoped>
#showcase-inner {
  position: relative;
  overflow: hidden;
  min-height: 200px;
  background-color: rgba(51, 51, 51, 1);
}
</style>
