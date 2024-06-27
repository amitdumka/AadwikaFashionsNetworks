<!-- eslint-disable vue/max-attributes-per-line -->
<script setup lang="ts">
import { z } from 'zod'
import { defineProps } from 'vue'
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
})

const schema = z.object({
  ondate: z.date().min(new Date(), 'Must be at least today'),
  mobileNo: z
    .string()
    .min(10, 'Must be at least 10 digits')
    .max(14, 'Must be at most 14 digits'),
  totalAmount: z.number().min(1, 'Must be at least 1'),
  basicAmount: z.number().min(1, 'Must be at least 1'),
  taxAmount: z.number().min(1, 'Must be at least 1'),
  RoundOff: z.number().min(1, 'Must be at least 1'),
  discount: z.number().min(1, 'Must be at least 1'),
  quantity: z.number().min(1, 'Must be at least 1'),
  count: z.number().min(1, 'Must be at least 1'),
})

const paymentSchema = z.object({
  amount: z.number().min(1, 'Must be at least 1'),
  onDate: z.date().min(new Date(), 'Must be at least today'),
  paymentType: z.string().min(1, 'Must be at least 1'),
})

const cardPaymentSchema = z.object({
  cardNo: z.string().min(1, 'Must be at least 1'),
  cvv: z.string().min(1, 'Must be at least 1'),
  expiry: z.string().min(1, 'Must be at least 1'),
  amount: z.number().min(1, 'Must be at least 1'),
  onDate: z.date().min(new Date(), 'Must be at least today'),
  paymentType: z.string().min(1, 'Must be at least 1'),
})

const itemschema = z.object({
  barcode: z.string(),
  qty: z.number().min(1, 'Must be at least 1'),
  rate: z.number().min(1, 'Must be at least 1'),
  amount: z.number().min(1, 'Must be at least 1'),
  discount: z.number(),
  tax: z.number().min(1, 'Must be at least 1'),
})

type Schema = z.output<typeof schema>
const isOpen = ref(false)
const state = reactive({
  ondate: undefined,
  mobiileNo: undefined,
  customerName: undefined,
  totalAmount: 0,
  basicAmount: 0,
  taxAmount: 0,
  RoundOff: 0,
  discount: 0,
  quantity: 0,
  count: 0,
  invoiceType: false,
  items: [],
  item: {
    barcode: undefined,
    qty: undefined,
    rate: undefined,
    amount: undefined,
    discountAmount: undefined,
    tax: 0,
  },
  payments: [
    {
      amount: 0,
      onDate: undefined,
      paymentType: 'Cash',
    },
  ],
  cardpayments: [
    {
      cardNo: undefined,
      cvv: undefined,
      expiry: undefined,
      amount: 0,
      onDate: undefined,
      paymentType: 'Card',
    },
  ],
})

async function onSubmit(event: FormSubmitEvent<Schema>) {
  // Do something with data
  console.log(event.data)
}
</script>

<template>
  <UForm
    :schema="schema"
    :state="state"
    class="space-y-4 h-32"
    @submit="onSubmit"
  >
    <UCard
      :ui="{ header: { base: 'justify-right ' } }"
    >
      <template #header>
        <h3>{{ $props.title }}</h3>
      </template>
      <UContainer>
        <Slot name="inv" />
      </UContainer>
      <UContainer>
        <Slot name="details" />
        <div v-if="$props.isSaleInvoice" class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700 mt-4 mr-4">
          <br>
          <h1>Payment(s)</h1>
          <br>
          <ul
            v-for="payment in state.payments"
            :key="payment"
            class=" mt-4 ml-4"
          >
            <li v-if="payment.amount>0">
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
      :is-open="isOpen"
    />
  </UForm>
</template>
