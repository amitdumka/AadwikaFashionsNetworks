import uuid
from django.db import models
from databases.models.base import BaseGlobalModel, BaseGroupModel, BaseModel
from core.globalEnums import AccountType
from databases.models.clients import Store, StoreGroup, Client
from databases.models.inventory import Vendor
from django.utils import timezone
# Create your models here.




#Bank Model 
class Bank (models.Model):
    Id = models.AutoField(primary_key=True, db_index=True, editable=False)
    Name=models.CharField(max_length=255)

    class Meta:
        verbose_name="Bank"
        verbose_name_plural="Banks"
    def __str__(self) -> str:
        return self.Name

class BankAccountBase(BaseGlobalModel):

    AccountNumber = models.CharField(max_length=255, primary_key=True, null=False, db_index=True, unique=True)
    
    AccountHolderName = models.CharField(max_length=255)
    
    Bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    
    IFSCCode = models.CharField(max_length=10)
    BranchName = models.CharField(max_length=255)
    AccountType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in AccountType]    )
    OpeningBalance = models.DecimalField(max_digits=10, decimal_places=2)
    ClosingBalance = models.DecimalField(max_digits=10, decimal_places=2)
    OpeningDate= models.DateTimeField(auto_now_add=True)
    ClosingDate = models.DateTimeField(null=True, blank=True)
    Active = models.BooleanField(default=True)
   
    class Meta:
        abstract = True
        
    def __self__(self) -> str:
        return self.AccountNumber+" - "+self.AccountHolderName       

class BankAccount(BankAccountBase):
    
    DefaultBank = models.BooleanField(default=False)
    class Meta:
        verbose_name = "BankAccount"
        verbose_name_plural = "BankAccounts"

class BankSecureDetail(models.Model):
    Id = models.AutoField(primary_key=True, db_index=True, editable=False)
    AccountNumber=models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    UserName=models.CharField(max_length=255,null=True,blank=True)
    Password=models.CharField(max_length=255,null=True,blank=True)
    TaxPassword=models.CharField(max_length=255,null=True,blank=True)
    CustomerId=models.CharField(max_length=255,null=True,blank=True)
    ExtraPassword=models.CharField(max_length=255, null=True, blank=True)
    ATMPin=models.CharField(max_length=255, null=True, blank=True)
    MPin=models.CharField(max_length=255, null=True, blank=True)
    TPin = models.CharField(max_length=255, null=True, blank=True)
    ATMCard=models.CharField(max_length=255, null=True, blank=True)
    ExpiryDate=models.DateField(null=True,blank=True)
    Status=models.CharField(max_length=255,null=True,blank=True)

    class Meta:
        verbose_name="BankSecureDetail"
        verbose_name_plural="BankSecureDetails"
    def __str__(self) -> str:
        return self.AccountNumber+" "+self.UserName
class VendorBankAccount(BankAccountBase):
    
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)   
    class Meta:
        verbose_name = "VendorBankAccount"
        verbose_name_plural = "VendorBankAccounts"
    def __str__(self) -> str:
        return self.Vendor.Name+" - "+ self.AccountNumber+", "+self.AccountHolderName

class BankAccountList(BankAccountBase):
    SharedAccount = models.BooleanField(default=False)
   
    class Meta:
        verbose_name = "BankAccountList"
        verbose_name_plural = "BankAccountLists"
    
    def __str__(self) -> str:
        return self.AccountNumber+", "+self.AccountHolderName


#Bank Transcation model : just like internal statement
class BankTransaction(BaseGlobalModel):
    TRANSACTION_TYPE_CHOICES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('chequeIssued', 'ChequeIssued'),
        ('chequeDeposited', 'ChequeDeposited'),
    ]

    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    AccountNumber = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=False)
    
    OnDate = models.DateTimeField(default= timezone.now)
    BankDate=models.DateTimeField(null=True,blank=True)
    
    TransactionType = models.CharField(max_length=24, choices=TRANSACTION_TYPE_CHOICES)
    ChequeNumber = models.CharField(max_length=255)
    ReferanceNo = models.CharField(max_length=255)
    Narations = models.CharField(max_length=255)
    
    AmountId = models.DecimalField(max_digits=10, decimal_places=2)
    AmountOut = models.DecimalField(max_digits=10, decimal_places=2)
    
    Balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    Remarks= models.CharField(max_length=255)
    Verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "BankTransaction"
        verbose_name_plural = "BankTransactions"
    def __str__(self) -> str:
        return self.AccountNumber+", "+self.TransactionAmount


class ChequeLog(BaseGroupModel):
        Id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
        
        AccountNumber = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True)
        ChequeDate=models.DateTimeField(auto_now_add=True)
        BankDate=models.DateTimeField(null=True, blank=True)
        
        PartyName= models.CharField(max_length=100)
        PartyAccountNumber=models.CharField(max_length=255)
        ChequeNumber=models.IntegerField()

        Bank=models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
       
        Amount=models.DecimalField(max_digits=10, decimal_places=2)
        Status=models.CharField(max_length=100)
        
        ReasonOfPayment=models.CharField(max_length=255)
        Remarks=models.CharField(max_length=255) 
        
        Verified=models.BooleanField(default=False)
        
        class Meta:
            verbose_name = "ChequeLog" 
            verbose_name_plural = "ChequeLogs"
        def  __str__(self) -> str:
            return self.AccountNumber+" - "+ self.PartyName+", ["+self.ChequeNumber+"] "+self.Amount



class BankStatement(BaseGlobalModel):
        Id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
        
        OnDate=models.DateTimeField(default= timezone.now)
        
        FromAccountNumber = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True)
        ToAccountNumber=models.CharField(max_length=255)
        
        BankRefernceNumber=models.CharField(max_length=255)
        Naration=models.CharField(max_length=255)
        
        Amount=models.DecimalField(max_digits=10, decimal_places=2)
        
        Verified=models.BooleanField(default=False)
        Internal=models.BooleanField(default=False)
        
        class Meta:
            verbose_name = "BankStatement" 
            verbose_name_plural = "BankStatements"

        def  __str__(self) -> str:
            return self.FromAccountNumber.AccountNumber+", "+self.Naration+", "+self.Amount
        

# class ChequeBook(BaseGroupModel):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
#     AccountNumber = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
#     NoOfCheques = models.IntegerField()
#     IssuedDate = models.DateTimeField(auto_now_add=True)
#     StartingNumber = models.IntegerField()
#     EndingNumber = models.IntegerField()
#     NoOfChequesUsed = models.IntegerField()
#     NoOfPDC=models.IntegerField()
#     NoOfClearedCheques=models.IntegerField()

    
#     class Meta:
#         verbose_name = "ChequeBook" 
#         verbose_name_plural = "ChequeBooks"
    
#     def  __str__(self) -> str:
#         return self.BankAccountId.AccountNumber+", "+self.StartingNumber+" - "+self.EndingNumber
    

       
# class ChequeIssued(BaseGroupModel):
    
#     Id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    
#     ChequeBook = models.ForeignKey(ChequeBook, on_delete=models.CASCADE)
#     AccountNumber = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
#     OnDate=models.DateTimeField(auto_now_add=True)
#     InFavourOf=models.CharField(max_length=255)
#     Amount=models.DecimalField(max_digits=10, decimal_places=2)
#     ChequeNumber=models.IntegerField()
    
#     IsReadOnly=models.BooleanField(default=False)
    
#     class Meta:
#         verbose_name = "ChequeIssued"   
#         verbose_name_plural = "ChequeIssueds"

#     def  __str__(self) -> str:
#         return self.AccountId.AccountNumber+", "+self.ChequeNumber+", "+self.Amount
