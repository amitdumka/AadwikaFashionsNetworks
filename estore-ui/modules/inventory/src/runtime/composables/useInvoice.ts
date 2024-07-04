import { z } from 'zod'
import type { FormSubmitEvent } from '#ui/types'

export const useInvoice = (isSaleInvoice: boolean) => {

  // TODO: fetch vendor list, pos machine, payment type, payment status


  const title = computed(() => isSaleInvoice ? 'Sale Invoice' : 'Purchase Invoice')
  const saleInvoice = computed(() => isSaleInvoice)


  const purchaseHeadSchema = z.object({
    ondate: z.date().min(new Date(), 'Must be at least today'),
    gstin: z.string(),
    vendorId: z.guid(10, 'Must be at least 10 digits'),

    totalAmount: z.number().min(1, 'Must be at least 1'),
    basicAmount: z.number().min(1, 'Must be at least 1'),
    taxAmount: z.number().min(1, 'Must be at least 1'),
    RoundOff: z.number().min(1, 'Must be at least 1'),
    discount: z.number().min(1, 'Must be at least 1'),
    quantity: z.number().min(1, 'Must be at least 1'),
    count: z.number().min(1, 'Must be at least 1'),
    shippingCharges: z.number().min(1, 'Must be at least 1'),
    shippingTax: z.number().min(1, 'Must be at least 1'),
  })

  const saleHeadschema = z.object({
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

  const SalePaymentSchema = z.object({
    amount: z.number().min(1, 'Must be at least 1'),
    onDate: z.date().min(new Date(), 'Must be at least today'),
    paymentType: z.string().min(1, 'Must be at least 1'),
  })

  const saleCardPaymentSchema = z.object({
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

  // Only Head Schema matters.
  const headSchema = computed(() => isSaleInvoice ? saleHeadschema : purchaseHeadSchema)

  const invoiceState = reactive({
    ondate: undefined,
    invoiceType: isSaleInvoice ? 'Sales' : 'Purchase',
    isReturnInvoice: false,
    totalAmount: 0,
    basicAmount: 0,
    taxAmount: 0,
    RoundOff: 0,
    discount: 0,
    quantity: 0,
    count: 0,
    saleInvoiceType: false,
    customer: {
      name: undefined,
      mobileNo: undefined,
      gstin: undefined,
    },
    vendor: {
      gstin: undefined,
      vendorId: undefined,
    },
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
    vendorPayment: [
      {
        amount: 0,
        onDate: undefined,
        paymentType: 'NEFT',
        chequeNo: undefined,
        refNo: undefined,
        remarks: undefined,

      },
    ],
  })
  // const invoices = ref([])
  // const getInvoices = async () => {
  //     const response = await fetch('http://localhost:8000/api/invoices')
  //     const data = await response.json()
  //     invoices.value = data
  // }

  // return { invoices, getInvoices }

  type schema = z.output<typeof headSchema>
  type itemSchema = z.output<typeof itemschema>
  const onSubmit = async (event: FormSubmitEvent<schema, itemSchema>) => {
    // Do something with data
    console.log(event.data)
  }
  return {
    headSchema,
    invoiceState, itemschema, saleCardPaymentSchema, SalePaymentSchema, title, saleInvoice, onSubmit,
  }
}
