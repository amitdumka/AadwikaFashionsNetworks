from enum import Enum
from django.utils import timezone
import uuid
from django.db import models
from databases.models.base import BaseGroupModel, BaseModel,BaseGlobalModel
from databases.models.banking import BankAccount, Bank
 
from core.globalEnums import PayMode, VoucherType, PaymentMode, LedgerType
from databases.models.clients import Client, Store, StoreGroup
from databases.models.core import Salesman
from databases.models.hrms import Employee
from django.utils import timezone

#SECTION - Accounting Models
class LedgerGroup(BaseGlobalModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    Name = models.CharField(max_length=100)
    Category = models.IntegerField(choices=[(tag.value, tag.name) for tag in LedgerType])
    Remarks = models.CharField(max_length=255, null=True,blank=True)
    class Meta:
        verbose_name = "LedgerGroup"
        verbose_name_plural = "LedgerGroups"
    def __str__(self):
        return self.Name+", "+self.Category
     
class Ledger(BaseGlobalModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    Name = models.CharField(max_length=100)
    Address= models.CharField(max_length=255, null=True,blank=True)
    EmailId= models.CharField(max_length=255, null=True,blank=True)
    PhoneNumber= models.CharField(max_length=255, null=True,blank=True)
    LedgerGroup= models.ForeignKey(LedgerGroup, on_delete=models.CASCADE)
    LedgerType= models.IntegerField(choices=[(tag.value, tag.name) for tag in LedgerType]) 
    
    OpeningDate = models.DateTimeField(default= timezone.now)
    OpeningBalance = models.DecimalField(decimal_places=2, max_digits=10)
    
    PANNumber= models.CharField(max_length=10, null=True,blank=True)
    GSTIN= models.CharField(max_length=15, null=True,blank=True)
    class Meta:
        verbose_name = "Ledger"
        verbose_name_plural = "Ledgers"
    def __str__(self):
        return self.Name
class VoucherBase(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    VoucherNumber= models.CharField(max_length=255)
    OnDate= models.DateTimeField(default= timezone.now)
    PartyName= models.CharField(max_length=255)
    Particulars= models.CharField(max_length=255)
    VoucherType= models.IntegerField(choices=[(tag.value, tag.name) for tag in VoucherType])
    Amount= models.DecimalField(decimal_places=2, max_digits=10)
    
    Remarks= models.CharField(max_length=255, null=True,blank=True) 
    IssuedBy= models.ForeignKey(Employee, on_delete=models.CASCADE) 
    SlipNumber= models.CharField(max_length=255, default="", null=True,blank=True)
    LedgerId= models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        abstract = True
class TranscationMode(models.Model):
    class Meta:
        verbose_name = "TranscationMode"
        verbose_name_plural = "TranscationModes"

    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    Name = models.CharField(max_length=100)
    def  __str__(self):
        return self.Name

class Voucher(VoucherBase):
    PaymentMode= models.IntegerField(choices=[(tag.value, tag.name) for tag in PaymentMode])
    PayemntDetails= models.CharField(max_length=255, null=True,blank=True)
    AccountNumber= models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Voucher"
        verbose_name_plural = "Vouchers"
    def __str__(self):
        return self.VoucherNumber+"-"+self.PartyName+"-"+str(self.OnDate)+"-"+str(self.Amount)

class CashVoucher(VoucherBase):
    TranscationMode= models.ForeignKey(TranscationMode, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "CashVoucher"
        verbose_name_plural = "CashVouchers"
    def __str__(self):
        return self.VoucherNumber+"-"+self.PartyName+"-"+str(self.OnDate)+"-"+str(self.Amount)

#Cash Details
class CashDetail(BaseModel):
    Id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    OnDate = models.DateTimeField(default= timezone.now)
    Count = models.IntegerField()
    TotalAmount = models.IntegerField()
    N2000 = models.IntegerField()
    N1000 = models.IntegerField()
    N500 = models.IntegerField()
    N200 = models.IntegerField()
    N100 = models.IntegerField()
    N50 = models.IntegerField()
    N20 = models.IntegerField()
    N10 = models.IntegerField()
    C10 = models.IntegerField()
    C5 = models.IntegerField()
    C2 = models.IntegerField()
    C1 = models.IntegerField()
    
    
    class Meta:
        verbose_name = "CashDetail"
        verbose_name_plural = "CashDetails"

    def __str__(self):
        return str(self.OnDate)+" - "+str(self.TotalAmount)


#!SECTION:Models


# EDCTerminal model , moved from Core to here due to circular import
class EDCTerminal(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=255)
    OnDate = models.DateTimeField(default= timezone.now)
    TID = models.CharField(max_length=255)
    MID = models.CharField(max_length=255)
    Bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, null=True, blank=True)
    AccountNumber= models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True)
    ProviderName = models.CharField(max_length=255)
    CloseDate = models.DateTimeField(null=True, blank=True)
    Active = models.BooleanField()        
    IsReadOnly=models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "EDCTerminal"
        verbose_name_plural = "EDCTerminals"
    
    def __str__(self):
        return self.Name+", "+self.ProviderName
  
class DailySale(BaseModel):
    InvoiceNumber =  models.CharField(max_length=255, primary_key=True, editable=True, unique=True, db_index=True, null=False)
    OnDate = models.DateTimeField(default= timezone.now)
    Amount = models.DecimalField (max_digits=10, decimal_places=2)
    CashAmount = models.DecimalField(max_digits=10, decimal_places=2)
    NonCashAmount = models.DecimalField(max_digits=10, decimal_places=2)
    PayMode =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  PayMode])
    
    IsDue = models.BooleanField(default=False)
    ManualBill = models.BooleanField(default=False)
    SalesReturn = models.BooleanField(default=False)
    ServiceBill = models.BooleanField(default=False)
    Remarks = models.CharField(max_length=255, null=True,blank=True)
   
    Salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE, null=True, blank=True)     
    EDCTerminal = models.ForeignKey(EDCTerminal, on_delete=models.CASCADE, null=True, blank=True)
    
    IsReadOnly = models.BooleanField(default=False)
    class Meta:
        verbose_name = "DailySale"
        verbose_name_plural = "DailySales"

#Customer Due model
class CustomerDue(BaseModel):
    InvoiceNumber =  models.CharField(max_length=150, primary_key=True, editable=True, unique=True, db_index=True, null=False)
    OnDate = models.DateTimeField(default= timezone.now)
    Amount = models.DecimalField (max_digits=10, decimal_places=2)
    Paid = models.BooleanField()
    ClearingDate = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "CustomerDue"
        verbose_name_plural = "CustomerDues"
    
    def __str__(self):
        return self.InvoiceNumber+"- "+str(self.OnDate)+"__"+str(self.Amount)
#Customer Due Recovery
class DueRecovery(BaseModel):
    Id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    OnDate = models.DateTimeField(default= timezone.now)
    InvoiceNumber =models.ForeignKey(DailySale, on_delete=models.CASCADE)
    Amount = models.DecimalField (max_digits=10, decimal_places=2)
    PayMode =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  PayMode])
    Remarks = models.CharField(max_length=255, null=True,blank=True)
    PartialPayment = models.BooleanField()
    Due = models.ForeignKey(CustomerDue, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "DueRecovery"
        verbose_name_plural = "DueRecoveries"
    
    def __str__(self):
        return str(self.OnDate)+" - "+str(self.Amount)+ " - "+str(self.InvoiceNumber)
