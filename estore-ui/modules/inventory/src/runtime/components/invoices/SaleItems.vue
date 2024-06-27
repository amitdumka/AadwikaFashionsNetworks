<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/padding-line-between-blocks -->
<!-- eslint-disable @stylistic/no-multiple-empty-lines -->
<!-- eslint-disable vue/max-attributes-per-line -->
<script setup lang="ts">
import { defineProps } from 'vue'
import { computed, reactive, ref } from '#imports'

defineProps({
  state: {
    type: Object,
    default: () => ({}),
  },
  title: {
    type: String,
    default: 'Sale Items',
  },
})
const localState = reactive({
  items: [],
  payments: [],
  item: {
    barcode: undefined,
    qty: undefined,
    rate: undefined,
    amount: undefined,
    discountAmount: undefined,
    tax: 0,
  },
})

function addItem() {
  console.log(localState.items)
  localState.items.push({ ...localState.item })
  console.log(localState.items)
  localState.item = {
    barcode: undefined,
    qty: 0,
    rate: 0,
    amount: 0,
    discountAmount: 0,
    tax: 0,
  }
}
function searchItem() {
  localState.item.qty = 1
  localState.item.amount = 1
  localState.item.tax = 1
  localState.item.discountAmount = 1
  localState.item.rate = 1
}
const page = ref(1)
const pageCount = 5

const rows = computed(() => {
  return localState.items.slice(
    (page.value - 1) * pageCount,
    page.value * pageCount,
  )
})
</script>

<template>
  <UCard ui="{ body: { base: 'grid grid-cols-5' } }">
    <template #header>
      <p>{{ $props.title }}</p>
    </template>
    <div class="grid grid-cols-6 mb-2">
      <UFormGroup
        name="barcode"
        required="true"
      >
        <UInput
          v-model=" localState.item.barcode"
          placeholder="Barcode"
          @keydown.tab.space="searchItem()"
        />
      </UFormGroup>
      <UFormGroup
        name="qty"
        required="true"
      >
        <UInput
          v-model="localState.item.qty"
          placeholder="Qty"
        />
      </UFormGroup>
      <UFormGroup
        name="rate"
        required="true"
      >
        <UInput
          v-model="localState.item.rate"
          placeholder="Rate"
        />
      </UFormGroup>
      <UFormGroup name="discountamt">
        <UInput
          v-model="localState.item.discountAmount"
          placeholder="Discount"
        />
      </UFormGroup>
      <UFormGroup
        name="Amount"
        required="true"
      >
        <UInput
          v-model="localState.item.amount"
          placeholder="Amount"
        />
      </UFormGroup>
      <UButton
        class="ml-10 mr-6"
        :trailing="true"
        color="violet"
        variant="outline"
        label="Add"
        size="sm"
        :ui="{ rounded: 'rounded-full' }"
        icon="i-heroicons-pencil-square"
        @click="addItem"
      />
    </div>
    <div class="mb-2 mr-4">
      <UDivider
        label="Items"
        class="mb-2 mr-2"
      />
      <UTable :rows="rows" />
      <div class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
        <UPagination
          v-model="page"
          :page-count="pageCount"
          :total="localState.items.length"
        />
      </div>
    </div>
    <template #footer>
      <p>Count:{{ localState.items.length }}</p>
    </template>
  </UCard>
</template>
