<script setup lang="ts">
const router = useRoute()
console.log(router)
console.log(router.params)

const { data: client, pending, error } = await useFetch<Client>(`http://localhost:8000/api/clients/${router.params.id}/`)
</script>

<template>
  <UDashboardPanel grow>
    <UDashboardNavbar title="Client">
      <template #right>
        <UButton label="Back" trailing-icon="i-heroicons-backspace" color="gray" @click="$router.go(-1)" />
      </template>
    </UDashboardNavbar>
    <div v-if="pending">
      <p> Loading......</p>
    </div>
    <div v-else-if="error">
      <p>{{ error }}</p>
    </div>
    <div v-else class="row my-5 justify-content-center mx-10">
      <div class="col-md-6">
        <div class="client-details">
          <h2 class="mb-3 text-primary">{{ client.name }}</h2>
          <p class="row my-5 justify-content-center mx-10"> Address : {{ client.address }}</p>
          <p class="row my-5 justify-content-center mx-10"> Email : {{ client.email }}</p>
          <p class="row my-5 justify-content-center mx-10"> Phone : {{ client.phone }}</p>
        </div>
      </div>
    </div>
  </UDashboardPanel>
</template>

<style scoped></style>
