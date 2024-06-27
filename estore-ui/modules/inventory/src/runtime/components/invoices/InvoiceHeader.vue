<script setup lang="ts">
import { defineProps } from 'vue'

defineProps({
  state: {
    type: Object,
    default: () => ({}),
  },
  title: {
    type: String,
    default: 'Invoice',
  },
  isSaleInvoice: {
    type: Boolean,
    default: true,
  },
})
</script>

<template>
  <UCard :ui="{ body: { base: 'grid grid-cols-4' } }">
    <div class="space-y-4 mr-4">
      <UFormGroup
        label="OnDate"
        name="ondate"
        required="true"
        size="xs"
      >
        <UInput
          v-model="$props.state.ondate"
          type="date"
        />
      </UFormGroup>
      <UFormGroup
        label="MobileNo"
        name="mobileNo"
        required="true"
        size="xs"
      >
        <UInput v-model="$props.state.mobileNo" />
      </UFormGroup>
      <UFormGroup
        label="Customer Name"
        name="customerName"
        required="false"
        size="xs"
      >
        <UInput v-model="$props.state.customerName" />
      </UFormGroup>
    </div>

    <div class="space-y-4 mr-4">
      <UFormGroup
        label="TotalAmount"
        name="totalAmount"
        required="true"
      >
        <UInput v-model="$props.state.totalAmount" />
      </UFormGroup>
      <UFormGroup
        label="BasicAmount"
        name="basicAmount"
        required="true"
      >
        <UInput v-model="$props.state.basicAmount" />
      </UFormGroup>
      <UFormGroup
        label="TaxAmount"
        name="taxAmount"
        required="true"
      >
        <UInput v-model="$props.state.taxAmount" />
      </UFormGroup>
    </div>

    <div class="mr-4">
      <UFormGroup
        label="RoundOff"
        name="RoundOff"
        required="true"
      >
        <UInput v-model="$props.state.RoundOff" />
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
        <UInput v-model="$props.state.discount" />
      </UFormGroup>
    </div>

    <div class="mr-4">
      <UFormGroup
        label="Quantity"
        name="quantity"
        required="true"
      >
        <UInput v-model="$props.state.quantity" />
      </UFormGroup>
      <UFormGroup
        label="Count"
        name="count"
        required="true"
      >
        <UInput v-model="$props.state.count" />
      </UFormGroup>
      <UFormGroup
        label="Invoice Return"
        name="rate"
        class="mt-10"
      >
        <UToggle v-model="$props.state.invoiceType" />
      </UFormGroup>
    </div>
  </UCard>
</template>
