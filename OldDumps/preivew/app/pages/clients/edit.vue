<template>
  <UDashboardPanel grow>
    <UDashboardNavbar title="Client">
      <template #right>
        <UButton label="Back" trailing-icon="i-heroicons-backspace" color="gray" @click="$router.go(-1)" />
      </template>
    </UDashboardNavbar>
    <div class="col-md-4">
      <form @submit.prevent="submitclient">
        <div class="form-group">
          <label for>client Name</label>
          <input type="text" class="form-control" v-model="client.name">
        </div>
        <div class="form-group">
          <label for>Address</label>
          <input type="text" v-model="client.address" class="form-control" name="Ingredients">
        </div>
        <div class="form-group">
          <label for>Phone</label>
          <input type="text" v-model="client.phone" class="form-control" name="Ingredients">
        </div>
        <div class="form-group">
          <label for>Email</label>
          <input type="text" v-model="client.email" class="form-control" name="Ingredients">
        </div>
        <button type="submit" class="btn btn-success">Save</button>
      </form>
    </div>
  </UDashboardPanel>
</template>

<script>
export default {
  async asyncData({ params }) {
    try {
      // let client = await $axios.$get(`/clients/${params.id}`)
      const { data: client } = await useFetch < Client > (`http://localhost:8000/api/clients/${params.id}`)
      return { client }
    } catch (e) {
      return { client: {} }
    }
  },

  data() {
    return {
      client: {
        name: '',
        address: '',
        phone: '',
        email: ''

      },
      preview: ''
    }
  },
  head() {
    return {
      title: 'Edit client'
    }
  },
  methods: {

    async saveClient() {
      const editedclient = this.client
      const formData = new FormData()
      for (const data in this.client) {
        formData.append(data, this.client[data])
      }
      try {
        const cln = await $fetch(`http://localhost:8000/api/clients/${editedclient.id}/`, {
          method: 'PATCH',
          body: formData
        })
        this.$router.push('/clients/')
      } catch (e) {
        console.log(e)
      }
    },
    async submitclient() {
      saveClient()
    }
  }
}
</script>

<style scoped></style>
