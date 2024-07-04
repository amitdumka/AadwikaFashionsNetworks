export const usePayment = (invoiceNumber: string) => {
  const title = computed(() => 'Payment of ' + invoiceNumber)
  const paymentSchema = z.object({
    amount: z.number().min(1, 'Must be at least 1'),
    description: z.string().min(1, 'Must be at least 1'),
    paymentDate: z.date().min(new Date(), 'Must be at least today'),
    invoiceNumber: z.string().min(1, 'Must be at least 1'),
    paymentType: z.string().min(1, 'Must be at least 1'),
    paymentStatus: z.string().min(1, 'Must be at least 1'),
    paymentMode: z.string().min(1, 'Must be at least 1'),
    paymentReference: z.string().min(1, 'Must be at least 1'),
    cardLastDigits:z.number().min(4, 'Must be at least 4'),
    authcode: z.number(),
    cardType: z.string(),
    card: z.string(),
  })

  type Schema=z.output<typeof paymentSchema>
  const savePayment = async (event: FormSubmitEvent<Schema>) => {
    // Do something with data
    console.log(event.data)
    // event.preventDefault()
    // check for Payment Mode type if card then need to check card details else submit
    // Fetch Invoice Number from database, check for amount, storecode etc.
  }
  const PaymentStatus = ['Pending', 'Success', 'Failed']

  return { title, paymentSchema, savePayment, PaymentStatus }
}
