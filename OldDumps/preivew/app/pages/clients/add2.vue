<template>
  <UDashboardPanel grow>
    <UDashboardNavbar title="Client">
      <template #right>
        <UButton label="Back" trailing-icon="i-heroicons-backspace" color="gray" @click="$router.go(-1)" />
      </template>
    </UDashboardNavbar>
    <div>
      <div class="col-md-4">
        <form @submit.prevent="submitclient">
          <div class="form-group">
            <label for>client Name</label>
            <input type="text" class="form-control" v-model="client.name" />
          </div>
          <div class="form-group">
            <label for>Address</label>
            <input v-model="client.address" type="text" class="form-control" />
          </div>
          <div class="form-group">
            <label for>Email</label>
            <input v-model="client.email" type="text" class="form-control" />
          </div>
          <div class="form-group">
            <label for>Phone</label>
            <input v-model="client.phone" type="text" class="form-control" />
          </div>

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </UDashboardPanel>
</template>

<script>
export default {
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
  methods: {

    async goBack() {
      this.$router.go(-1)
    },
    async addClient() {
      const formData = new FormData()
      for (const data in this.client) {
        formData.append(data, this.client[data])
      }
      try {
        const cln = await $fetch('http://localhost:8000/api/clients/', {
          method: 'POST',
          body: formData
        })
        this.$router.push('/clients/')
      } catch (e) {
        console.log(e)
      }
    },
    async submitclient() {
      this.addClient()
      // const config = {
      //   headers: { 'content-type': 'multipart/form-data' }
      // }
      // const formData = new FormData()
      // for (const data in this.client) {
      //   formData.append(data, this.client[data])
      // }
      // try {
      //   const response = await this.$axios.$post('/clients/', formData, config)
      //   this.$router.push('/clients/')
      // } catch (e) {
      //   console.log(e)
      // }
    }
  }
}
</script>

<style scoped></style>
