<script setup>
import { ref } from "vue";

const contacts = ref([{ id: 1, listing: [1, 2, 3] }]);
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
          <h2>Welcome admin</h2>
          <template v-if="contacts">
            <p>Here are the property listing reports that you have uploaded.</p>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Property</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="contact in contacts">
                  <td>{{ contact.id }}</td>
                  <td>{{ contact.listing }}</td>
                  <td>
                    <a class="btn btn-light" href="/">View Listing</a>
                  </td>
                </tr>
              </tbody>
            </table>
          </template>
          <template v-else><p>You have not made any inquiries</p></template>
        </div>
      </div>
    </div>
  </section>
</template>
