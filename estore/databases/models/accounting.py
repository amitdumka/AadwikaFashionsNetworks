from django.utils import timezone
import uuid
from django.db import models
from databases.models.base import BaseGroupModel, BaseModel
from databases.models.banking import BankAccount, Bank
 
from core.globalEnums import PayMode, VoucherType, PaymentMode
from databases.models.clients import Client, Store, StoreGroup
from databases.models.hrms import Employee
from django.utils import timezone

# Create your models here.
class LedgerGroup(BaseGroupModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    GroupName = models.CharField(max_length=100)
    Category = models.CharField(max_length=20)
    Remarks = models.CharField(max_length=255, null=True,blank=True)
    
    #StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE)
    #ClientId=models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "LedgerGroup"
        verbose_name_plural = "LedgerGroups"
    def __str__(self):
        return self.GroupName+", "+self.Category

#Party model
class Party(BaseGroupModel):
    Id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    PartyName = models.CharField(max_length=100)
    OpeningDate = models.DateTimeField(default= timezone.now)
    ClosingDate = models.DateTimeField(null=True, blank=True)
    OpeningBalance = models.DecimalField(max_digits=10, decimal_places=2)
    ClosingBalance = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.CharField(max_length=20)
    GSTIN = models.CharField(max_length=15, null=True, blank=True)
    PANNo = models.CharField(max_length=10, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True,blank=True)
    MobileNo=models.CharField(max_length=14, null=True, blank=True)
    EmailId=models.CharField(max_length=50, null=True, blank=True)
    Remarks = models.CharField(max_length=255, null=True,blank=True)
    LedgerGroup = models.ForeignKey(LedgerGroup, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.PartyName

    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"
        
#Vouchers model
class Voucher(BaseModel):
    class Meta:
        verbose_name = "Voucher"
        verbose_name_plural = "Vouchers"

    VoucherNumber = models.CharField(max_length=150, primary_key=True, editable=False, unique=True, db_index=True, null=False) 
    VoucherType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in VoucherType])

    OnDate = models.DateTimeField(default= timezone.now)
    SlipNumber = models.CharField(max_length=100)
    PartyName= models.CharField(max_length=255)
    Particulars=models.CharField(max_length=255)
    Amount = models.DecimalField(decimal_places=2, max_digits=10)
    Remarks=models.CharField(max_length=255)   
    #Voucher Issued By EmployeeName
    Employee=models.ForeignKey(Employee, on_delete=models.CASCADE,)
    #Ledger Name
    Party=models.ForeignKey(Party, on_delete=models.CASCADE, null=True, blank=True)   
    #Paying or receiving Bank Account
    AccountNumber=models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True)
    
    #Payment Mode
    PaymentMode=models.IntegerField(choices=[(tag.value, tag.name) for tag in PaymentMode]    )
    PaymentDetails=models.CharField(max_length=255, null=True, blank=True)  
    IsReadOnly=models.BooleanField(default=False)

    def __str__(self):
        return self.VoucherNumber+"-"+self.PartyName+"-"+str(self.OnDate)+"-"+str(self.Amount)

#TranscationMode model
class TransactionMode(models.Model):
    class Meta:
        verbose_name = "TranscationMode"
        verbose_name_plural = "TranscationModes"

    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    TransactionName = models.CharField(max_length=100)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)

    def  __str__(self):
        return self.TransactionName

#CashVouchers model
class CashVoucher(BaseModel):
    class Meta:
        verbose_name = "CashVoucher"
        verbose_name_plural = "CashVouchers"

    VoucherNumber = models.CharField(max_length=150, primary_key=True, editable=False, unique=True, db_index=True, null=False)
   
    VoucherType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  VoucherType])
    OnDate = models.DateTimeField(default= timezone.now)
    TranscationMode=models.ForeignKey(TransactionMode, on_delete=models.CASCADE)      
    SlipNumber = models.CharField(max_length=100)
    PartyName = models.CharField(max_length=100)
    
    Particulars = models.CharField(max_length=100)
    Amount = models.DecimalField(decimal_places=2, max_digits=10) 
    Remarks = models.CharField(max_length=100)
    
    Employee =models.ForeignKey(Employee, on_delete=models.CASCADE,)
    #Ledger Name
    Party=models.ForeignKey(Party, on_delete=models.CASCADE, null=True, blank=True)
    IsReadOnly = models.BooleanField(default=False)
   

    def  __str__(self):
        return self.VoucherNumber+"-"+self.PartyName+"-"+self.OnDate+"-"+str(self.Amount)


class Salesman(BaseModel):
    Id = models.CharField(max_length=100, primary_key=True, editable=False, unique=True, db_index=True, null=False)
    Name = models.CharField(max_length=255)
    Employee =models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, blank=True)
    
    Active = models.BooleanField()


    class Meta:
        verbose_name = "Salesman"
        verbose_name_plural = "Salesmen"
    def __str__(self):
        return self.Name

# EDCTerminal model , moved from Core to here due to circular import
class EDCTerminal(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=255)
    OnDate = models.DateTimeField(default= timezone.now)
    TID = models.CharField(max_length=255)
    MID = models.CharField(max_length=255)
    Bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, null=True, blank=True)
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
    #StoreId=models.ForeignKey(Store, on_delete=models.CASCADE)
    #StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE)
    #ClientId=models.ForeignKey(Client, on_delete=models.CASCADE)


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

#Party Ledger Model
class LedgerMaster(models.Model):
    Id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=True, db_index=True, unique=True)
    PartyName= models.CharField(max_length=100)
    OpeningDate = models.DateTimeField(default= timezone.now)

    class Meta:
        verbose_name = "LedgerMaster"
        verbose_name_plural = "LedgerMasters"
    def __str__(self):
        return self.PartyName

