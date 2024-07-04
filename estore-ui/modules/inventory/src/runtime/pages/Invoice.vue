<script setup lang="ts">
import type { z } from 'zod'
import { useInvoice } from '../composables/useInvoice'
import type { FormSubmitEvent } from '#ui/types'

defineProps({
  title: {
    type: String,
    default: 'Invoice',
  },
  isSaleInvoice: {
    type: Boolean,
    default: true,
  },
  isPaymentEnabled: {
    type: Boolean,
    default: true,
  },
  isPrintingEnabled: {
    type: Boolean,
    default: true,
  },
  noOfcopies: {
    type: Number,
    default: 1,
  },
})

const { headSchema, invoiceState, itemschema, title, onSubmit } = useInvoice(
  $props.isSaleInvoice,
)
// setting Custom title set by user

if ($props.title != 'Invoice') {
  title.value = $props.title
}
// TODO: Check if possible move to composable
type Schema = z.output<typeof headSchema>

// type itemSchema = z.output<typeof itemschema>

const isOpen = ref(false)

// async function onSubmit(event: FormSubmitEvent<schema>) {
//   // Do something with data
//   console.log(event.data)
// }
</script>

<template>
  <UForm
    :schema="schema"
    :state="invoiceState"
    class="space-y-4 h-32"
    @submit="onSubmit"
  >
    <UCard :ui="{ header: { base: 'justify-right ' } }">
      <template #header>
        <h3>{{ title }}</h3>
      </template>
      <UContainer>
        <Slot name="inv" />
      </UContainer>
      <UContainer>
        <Slot name="details" />
        <div
          v-if="$props.isSaleInvoice"
          class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700 mt-4 mr-4"
        >
          <br>
          <h1>Payment(s)</h1>
          <br>
          <ul
            v-for="payment in invoiceState.payments"
            :key="payment"
            class="mt-4 ml-4"
          >
            <li v-if="payment.amount > 0">
              {{ payment.amount }}, {{ payment.paymentType }}
            </li>
          </ul>
        </div>
      </UContainer>
      <template #footer>
        <Slot name="footer" />
      </template>
    </UCard>
    <!-- It will open Payment Model Form -->
    <IModel
      title="Payment"
      :is-sale-invoice="isSaleInvoice"
      :is-open="isOpen"
    />
  </UForm>
</template>
