<script lang="ts" setup>
import type { Client, AppClient } from '~/types'

const router = useRouter()

function editClient(id: number) {
  console.log('Edit', id)
  router.push(`/clients/${id}/edit/`)
}
function detailsClient(id: number) {
  console.log('Details', id)
  router.push(`/clients/${id}/`)
}
function deleteClient(id: number) {
  console.log('Delete', id)
  router.push('/clients/')
}
const defaultColumns = [
  {
    key: 'id',
    label: '#'
  },
  {
    key: 'name',
    label: 'Name',
    sortable: true
  },
  {
    key: 'phone',
    label: 'Phone',
    sortable: true
  },
  {
    key: 'email',
    label: 'Email',
    sortable: true
  },
  {
    key: 'address',
    label: 'Address',
    sortable: true
  }, {
    key: 'actions'
  }]

const onSelect = (rows: any) => {
  console.log('Select', rows)
}
const { data: clients, pending } = await useFetch<Client[]>('http://localhost:8000/api/clients/', { default: () => [] })

const items = (row: any) => [
  [{
    label: 'Edit',
    icon: 'i-heroicons-pencil-square-20-solid',
    click: () => editClient(row.id)
  }, {
    label: 'Details',
    icon: 'i-heroicons-document-duplicate-20-solid',
    click: () => detailsClient(row.id)
  }, {
    label: 'Delete',
    icon: 'i-heroicons-trash-20-solid',
    click: () => deleteClient(row.id)
  }]
]
</script>

<template>
  <UDashboardPanel grow>
    <UDashboardNavbar title="Clients" :badge="clients.length">
      <template #right>
        <UButton label="New client" trailing-icon="i-heroicons-plus" color="gray"
          @click="$router.push('/clients/add')" />
      </template>
    </UDashboardNavbar>
    <UTable :rows="clients" :columns="defaultColumns" :loading="pending" class="w-full"
      :ui="{ divide: 'divide-gray-200 dark:divide-gray-800' }" @select="onSelect">
      <template #name-data="{ row }">
        <div class="flex items-center gap-3">
          <UAvatar v-bind="row.avatar" :alt="row.name" size="xs" />

          <span class="text-gray-900 dark:text-white font-medium">{{ row.name }}</span>
        </div>
      </template>

      <template #address-data="{ row }">
        <UBadge :label="row.address" :color="row.address === 'Bhagalpur Road Dumka'
          ? 'green'
          : row.address === 'Dumka' ? 'orange' : 'red'" variant="subtle" class="capitalize" />
      </template>
      <template #actions-data="{ row }">
        <UDropdown :items="items(row)">
          <UButton color="gray" variant="ghost" icon="i-heroicons-ellipsis-horizontal-20-solid" />
        </UDropdown>
      </template>
    </UTable>
  </UDashboardPanel>
</template>
