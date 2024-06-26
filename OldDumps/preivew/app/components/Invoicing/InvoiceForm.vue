<!-- eslint-disable vue/max-attributes-per-line -->
<script setup lang="ts">
import { z } from 'zod'
import type { FormSubmitEvent } from '#ui/types'

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
  count: z.number().min(1, 'Must be at least 1')
})
const paymentSchema = z.object({
  amount: z.number().min(1, 'Must be at least 1'),
  onDate: z.date().min(new Date(), 'Must be at least today'),
  paymentType: z.string().min(1, 'Must be at least 1')
})
const cardPaymentSchema = z.object({
  cardNo: z.string().min(1, 'Must be at least 1'),
  cvv: z.string().min(1, 'Must be at least 1'),
  expiry: z.string().min(1, 'Must be at least 1'),
  amount: z.number().min(1, 'Must be at least 1'),
  onDate: z.date().min(new Date(), 'Must be at least today'),
  paymentType: z.string().min(1, 'Must be at least 1')
})

const itemschema = z.object({
  barcode: z.string(),
  qty: z.number().min(1, 'Must be at least 1'),
  rate: z.number().min(1, 'Must be at least 1'),
  amount: z.number().min(1, 'Must be at least 1'),
  discount: z.number(),
  tax: z.number().min(1, 'Must be at least 1')
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
    tax: 0
  },
  payments: [
    {
      amount: 0,
      onDate: undefined,
      paymentType: 'Cash'
    }
  ],
  cardpayments: [
    {
      cardNo: undefined,
      cvv: undefined,
      expiry: undefined,
      amount: 0,
      onDate: undefined,
      paymentType: 'Card'
    }
  ]
})
const page = ref(1)
const pageCount = 5

const rows = computed(() => {
  return state.items.slice(
    (page.value - 1) * pageCount,
    page.value * pageCount
  )
})

async function onSubmit(event: FormSubmitEvent<Schema>) {
  // Do something with data
  console.log(event.data)
}

function addItem() {
  console.log(state.items)
  state.items.push({ ...state.item })
  console.log(state.items)
  state.item = {
    barcode: undefined,
    qty: 0,
    rate: 0,
    amount: 0,
    discountAmount: 0,
    tax: 0
  }
}
function searchItem() {
  state.item.qty = 1
  state.item.amount = 1
  state.item.tax = 1
  state.item.discountAmount = 1
  state.item.rate = 1
}
</script>

<template>
  <UForm
    :schema="schema"
    :state="state"
    class="space-y-4 h-32"
    @submit="onSubmit"
  >
    <UCard :ui="{ header: { base: 'justify-right ' } }">
      <template #header>
        <h3>Invocing</h3>
      </template>
      <UContainer>
        <UCard :ui="{ body: { base: 'grid grid-cols-4' } }">
          <div class="space-y-4 mr-4">
            <UFormGroup
              label="OnDate"
              name="ondate"
              required="true"
              size="xs"
            >
              <UInput
                v-model="state.ondate"
                type="date"
              />
            </UFormGroup>
            <UFormGroup
              label="MobileNo"
              name="mobileNo"
              required="true"
              size="xs"
            >
              <UInput v-model="state.mobileNo" />
            </UFormGroup>
            <UFormGroup
              label="Customer Name"
              name="customerName"
              required="false"
              size="xs"
            >
              <UInput v-model="state.customerName" />
            </UFormGroup>
          </div>

          <div class="space-y-4 mr-4">
            <UFormGroup
              label="TotalAmount"
              name="totalAmount"
              required="true"
            >
              <UInput v-model="state.totalAmount" />
            </UFormGroup>
            <UFormGroup
              label="BasicAmount"
              name="basicAmount"
              required="true"
            >
              <UInput v-model="state.basicAmount" />
            </UFormGroup>
            <UFormGroup
              label="TaxAmount"
              name="taxAmount"
              required="true"
            >
              <UInput v-model="state.taxAmount" />
            </UFormGroup>
          </div>

          <div class="mr-4">
            <UFormGroup
              label="RoundOff"
              name="RoundOff"
              required="true"
            >
              <UInput v-model="state.RoundOff" />
            </UFormGroup>
            <UDivider
              label=""
              orientation="vertical"
            />
            <UFormGroup
              label="Discount"
              name="discount"
              required="true"
            >
              <UInput v-model="state.discount" />
            </UFormGroup>
          </div>

          <div class="mr-4">
            <UFormGroup
              label="Quantity"
              name="quantity"
              required="true"
            >
              <UInput v-model="state.quantity" />
            </UFormGroup>
            <UFormGroup
              label="Count"
              name="count"
              required="true"
            >
              <UInput v-model="state.count" />
            </UFormGroup>
            <UFormGroup
              label="Invoice Return"
              name="rate"
              class="mt-10"
            >
              <UToggle v-model="state.invoiceType" />
            </UFormGroup>
          </div>
        </UCard>
      </UContainer>
      <UContainer>
        <UCard ui="{ body: { base: 'grid grid-cols-5' } }">
          <template #header>
            <p>Items</p>
          </template>
          <div class="grid grid-cols-6 mb-2">
            <UFormGroup
              name="barcode"
              required="true"
            >
              <UInput
                v-model="state.item.barcode"
                placeholder="Barcode"
                @keydown.tab.space="searchItem()"
              />
            </UFormGroup>
            <UFormGroup
              name="qty"
              required="true"
            >
              <UInput
                v-model="state.item.qty"
                placeholder="Qty"
              />
            </UFormGroup>
            <UFormGroup
              name="rate"
              required="true"
            >
              <UInput
                v-model="state.item.rate"
                placeholder="Rate"
              />
            </UFormGroup>
            <UFormGroup name="discountamt">
              <UInput
                v-model="state.item.discountAmount"
                placeholder="Discount"
              />
            </UFormGroup>
            <UFormGroup
              name="Amount"
              required="true"
            >
              <UInput
                v-model="state.item.amount"
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
                :total="state.items.length"
              />
            </div>
          </div>
          <template #footer>
            <p>Count:{{ state.items.length }}</p>
          </template>
        </UCard>
        <div class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700 mt-4 mr-4">
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
        <UButton
          type="submit"
          class="mr-4"
          color="primary"
        >
          Save
        </UButton>
        <UButton
          class="mr-4"
          color="rose"
          @click="isOpen = true"
        >
          Payment
        </UButton>
        <UButton
          class="mr-4"
          color="violet"
          @click="$router.go(-1)"
        >
          Cancel
        </UButton>
      </template>
    </UCard>
    <UModal
      v-model="isOpen"
      prevent-close
    >
      <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <div class="flex items-center justify-between">
            <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-white">
              Payment
            </h3>

            <UButton
              color="gray"
              variant="ghost"
              icon="i-heroicons-x-mark-20-solid"
              class="-my-1"
              @click="isOpen = false"
            />
          </div>
        </template>

        <FormsPaymentForm
          :invoice-number="state.customerName"
          :total-amount="state.totalAmount"
        />
        <template #footer>
          <UButton
            label="Save & Close"
            @click="isOpen = false"
          />
        </template>
      </UCard>
    </UModal>
  </UForm>
</template>
