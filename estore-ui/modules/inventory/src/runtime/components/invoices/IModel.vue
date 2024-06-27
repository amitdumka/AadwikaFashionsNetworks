<script setup lang="ts">
import { defineProps } from 'vue'

defineProps({
  state: {
    type: Object,
    default: () => ({}),
  },
  isOpen: {
    type: Boolean,
    default: false,
  },
  title: {
    type: String,
    default: 'Payment',
  },
})

// create a function to cancle payment and function to save payment and close modal
</script>

<template>
  <UModal
    v-model="$props.isOpen"
    prevent-close
  >
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <template #header>
        <div class="flex items-center justify-between">
          <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-white">
            {{$props.title}}
          </h3>

          <UButton
            color="gray"
            variant="ghost"
            icon="i-heroicons-x-mark-20-solid"
            class="-my-1"
            @click="$props.isOpen = false"
          />
        </div>
      </template>

      <PaymentForm
        :invoice-number="state.invoiceNumber"
        :total-amount="state.totalAmount"
      />
      <template #footer>
        <UButton
          label="Save & Close"
          @click="$props.isOpen = false"
        />
      </template>
    </UCard>
  </UModal>
</template>
