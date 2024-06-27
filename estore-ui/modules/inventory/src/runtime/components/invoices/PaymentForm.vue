<script setup lang="ts">
import { defineProps } from 'vue'

defineProps({
  state: {
    type: Object,
    default: () => ({}),
  },
  title: {
    type: String,
    default: 'Payment',
  }, invoiceNumber: {
    type: String,
    required: true,
  },
  totalAmount: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="mb-2 mr-4 ">
    <div>
      <h3>{{ $props.title }}</h3>
    </div>
    <div class="grid grid-cols-2 mb-4">
      <p>Invoice Number: {{ $props.invoiceNumber }},</p>
      <p>Bill Amount: {{ $props.totalAmount }}</p>
    </div>

    <div class="grid grid-cols-2 mb-4">
      <div class="mr-4">
        <UFormGroup
          name="paymentMode"
          lable="Mode"
        >
          <USelect
            placeholder="Mode"
            :items="['cash', 'card', 'upi']"
          />
        </UFormGroup>
        <UFormGroup
          name="amount"
          lable="Amount"
        >
          <UInput placeholder="Amount" />
        </UFormGroup>
        <UFormGroup
          name="remarks"
          lable="Reference"
        >
          <UInput placeholder="Reference" />
        </UFormGroup>
      </div>
      <div class="mr-4">
        <UFormGroup
          name="cardtype"
          lable="Card Type"
        >
          <USelect placeholder="Date" />
        </UFormGroup>
        <UFormGroup
          name="cardCategoyr"
          lable="Category"
        >
          <USelect
            placeholder="Mode"
            :items="['Debit', 'Credit', 'GiftCard']"
          />
        </UFormGroup>
        <UFormGroup
          name="cardno"
          lable="Card No"
        >
          <UInput placeholder="Card No" />
        </UFormGroup>
        <UFormGroup
          name="auth"
          lable="AuthCode"
        >
          <UInput placeholder="AuthCode" />
        </UFormGroup>
      </div>
    </div>
  </div>
</template>
