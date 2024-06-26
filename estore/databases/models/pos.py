import uuid
from django.utils import timezone
from django.db import models
from core.globalEnums import Unit, TaxType, InvoiceType, PayMode, CARD, CARDType,PaymentMode
from databases.models.core import Customer
from databases.models.base import BaseGlobalModel, BaseGroupModel, BaseModel
from databases.models.accounting import Salesman, EDCTerminal
from databases.models.inventory import Product

# Create your models here.
# class ProductSale(BaseModel):
#     InvoiceNo = models.CharField(max_length=255, primary_key=True, editable=False, db_index=True)
#     OnDate = models.DateTimeField(default= timezone.now)
#     InvoiceType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  InvoiceType])
#     BilledQty = models.DecimalField(max_digits=10, decimal_places=2)
#     FreeQty = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalMRP = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalDiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalBasicAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalTaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     RoundOff = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     Taxed = models.BooleanField()
#     Adjusted = models.BooleanField()
#     Items = models.ManyToManyField('SaleItem')
#     Paid = models.BooleanField()
    
#     ServiceBill = models.BooleanField()
#     Salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE, null=True, blank=True)
#     class Meta:
#         unique_together = (('InvoiceNo', 'OnDate'),)
#         verbose_name = "ProductSale"
#         verbose_name_plural = "ProductSales"

#     def __str__(self):
#         return self.InvoiceNo

#  #Customer Sale   Model

# #SaleItem model
# class SaleItem(models.Model):
#     Id = models.IntegerField(primary_key=True, auto_created=True, editable=False, db_index=True, unique=True, null=False )
#     InvoiceNumber = models.ForeignKey(ProductSale, on_delete=models.CASCADE, null=True, blank=True)
#     Barcode = models.ForeignKey(ProductItem, on_delete=models.DO_NOTHING, null=True, blank=True)
#     BilledQty = models.DecimalField(max_digits=10, decimal_places=2)
#     FreeQty = models.DecimalField(max_digits=10, decimal_places=2)
#     Unit =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  Unit])
#     DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     BasicAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     Value = models.DecimalField(max_digits=10, decimal_places=2)
#     TaxType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  TaxType])
#     InvoiceType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  InvoiceType])
#     Adjusted = models.BooleanField()
#     LastPcs = models.BooleanField()

#     def __str__(self):
#         return self.Barcode
#     class Meta:
#         unique_together = (('Id', 'InvoiceNumber'),)
#         verbose_name = "SaleItem"
#         verbose_name_plural = "SaleItems"

# #Sale Payment Detail
# class SalePaymentDetail(BaseGlobalModel):
#     Id =  models.IntegerField(primary_key=True, auto_created=True, editable=False, db_index=True, unique=True, null=False )
#     InvoiceNumber = models.ForeignKey(ProductSale, on_delete=models.CASCADE, null=True, blank=True)
#     PaidAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     PayMode =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  PayMode])
#     RefId = models.CharField(max_length=255)
     
#     def __str__(self):
#         return self.InvoiceNumber+"-"+str(self.PaidAmount)
#     class Meta:
#         #unique_together = (('Id', 'InvoiceNumber'),)
#         verbose_name = "SalePaymentDetail"
#         verbose_name_plural = "SalePaymentDetails"

# #Card Payment detail model
# class CardPaymentDetail(BaseGlobalModel):
#     Id =  models.IntegerField(primary_key=True, auto_created=True, editable=False, db_index=True, unique=True, null=False )
#     InvoiceNumber = models.ForeignKey(ProductSale, on_delete=models.CASCADE, null=True, blank=True)
#     PaidAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     Card =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  CARD])
#     CardType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  CARDType])
#     CardLastDigit = models.IntegerField()
#     AuthCode = models.IntegerField()
#     PosMachine = models.ForeignKey(EDCTerminal, on_delete=models.DO_NOTHING, null=True, blank=True)

#     def __str__(self):
#         return self.InvoiceNumber+"-"+str(self.PaidAmount)
#     class Meta:
#         #unique_together = (('Id', 'InvoiceNumber'),)
#         verbose_name = "CardPaymentDetail"
#         verbose_name_plural = "CardPaymentDetails"

   
class Invoice(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    InvoiceNumber= models.CharField(max_length=255, unique=True)
    InvoiceDate= models.DateTimeField(default= timezone.now)
    CustomerMobileNumber=models.CharField(max_length=255)
    CustomerName=models.CharField(max_length=255)
    GSTIN=models.CharField(max_length=255)
    
    BasicAmount= models.DecimalField(max_digits=10, decimal_places=2)
    DiscountAmount= models.DecimalField(max_digits=10, decimal_places=2)
    TaxAmount= models.DecimalField(max_digits=10, decimal_places=2)
    NetAmount= models.DecimalField(max_digits=10, decimal_places=2)
    RoundOff= models.DecimalField(max_digits=10, decimal_places=2)
    
    BillAmount= models.DecimalField(max_digits=10, decimal_places=2)
    
    Quantity= models.DecimalField(max_digits=10, decimal_places=2)
    Count= models.IntegerField()
    
    Salesman=models.ForeignKey(Salesman, on_delete=models.CASCADE)
    
    #Paid Refernce so It not be re fetch data
    Paid= models.BooleanField(default=False)
    PaidDate= models.DateTimeField(null=True, blank=True)
    PaidAmount= models.DecimalField(max_digits=10, decimal_places=2,default=0)
    
    PaymentMode= models.IntegerField(choices=[(tag.value, tag.name) for tag in  PaymentMode])
    
    class  Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
    def __str__(self):
        return self.InvoiceNumber+" - "+self.BillAmount
    
class SaleItem(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Barcode=models.CharField(max_length=255)
    Product=models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity=models.DecimalField(max_digits=10, decimal_places=2)
    Unit= models.IntegerField(choices=[(tag.value, tag.name) for tag in  Unit])
    MRP = models.DecimalField(max_digits=10, decimal_places=2)
    BasicAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
    TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    TaxRate = models.DecimalField(max_digits=10, decimal_places=2)
    TaxType= models.IntegerField(choices=[(tag.value, tag.name) for tag in TaxType])
    class  Meta:
        verbose_name = "SaleItem"
        verbose_name_plural = "SaleItems"
    def __str__(self):
        return self.Invoice.InvoiceNumber+" - "+self.Barcode+" - "+self.Amount
    
class InvoicePayment(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE)
    OnDate= models.DateTimeField(default= timezone.now)
    PaymentMode= models.IntegerField(choices=[(tag.value, tag.name) for tag in  PaymentMode])
    Amount= models.DecimalField(max_digits=10, decimal_places=2)
    ReferenceNumber= models.CharField(max_length=255)
    
    class  Meta:
        verbose_name = "InvoicePayment"
        verbose_name_plural = "InvoicePayments"
    def __str__(self):
        return self.Invoice.InvoiceNumber+" - "+self.PaymentMode+" - "+self.Amount
    
class CardPayment(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE)
    OnDate= models.DateTimeField(default= timezone.now)
    Amount= models.DecimalField(max_digits=10, decimal_places=2)
    LastFourDigit= models.IntegerField()
    AuthCode= models.IntegerField()
    CardType= models.IntegerField(choices=[(tag.value, tag.name) for tag in  CARDType])
    Card= models.IntegerField(choices=[(tag.value, tag.name) for tag in  CARD])
    BankName= models.CharField(max_length=255, default="Sate Bank Of India")
    
    class  Meta:
        verbose_name = "CardPayment"
        verbose_name_plural = "CardPayments"
    def __str__(self):
        return self.Invoice.InvoiceNumber+" - "+self.Amount
        
  
class CustomerSale(BaseGlobalModel):
    Id = models.IntegerField(primary_key=True, auto_created=True, editable=False, db_index=True, unique=True, null=False )
    InvoiceNumber = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True,   db_index=True)
    MobileNo = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    OnDate = models.DateTimeField(default= timezone.now)
    Amount= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.InvoiceNumber+"-"+self.MobileNo+"-"+self.Customer.CustomerName
    class Meta:
        unique_together = (('InvoiceNumber', 'MobileNo'),)
        verbose_name = "CustomerSale"
        verbose_name_plural = "CustomerSales"