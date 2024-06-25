# <project>/<app>/management/commands/seed.py
from datetime import datetime, timezone
from django.core.management.base import BaseCommand
from dbs.models.accounting import EDCTerminal, LedgerGroup, Party, Salesman, TransactionMode
from dbs.models.banking import Bank, BankAccount
from dbs.models.hrms import Employee
from dbs.models.clients import Client, StoreGroup, Store
import random

class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('Aprajita Retails Database Seeding... ')
        self.stdout.write('Basic data is added to the database. ')
        run_seed(self)
        self.stdout.write('Sedding is completed!')

def run_seed(self):
    # Clear existing data
    Client.objects.all().delete()
    StoreGroup.objects.all().delete()
    Store.objects.all().delete()
    Bank.objects.all().delete()
    TransactionMode.objects.all().delete()
    Employee.objects.all().delete()
    LedgerGroup.objects.all().delete()
    Party.objects.all().delete()
    BankAccount.objects.all().delete()
    
    

    
    # Create new instances
    

    sbi= Bank.objects.create(BankName="State Bank of India")
    icici= Bank.objects.create(BankName="ICICI Bank")
    bank= Bank.objects.create(BankName="HDFC Bank")
    bank= Bank.objects.create(BankName="Punjab National Bank")
    bank= Bank.objects.create(BankName="IDFC Bank")
    bank= Bank.objects.create(BankName="Bank Of Maharashtra")
    bank= Bank.objects.create(BankName="Bank of Baroda")
    
    
    
    client = Client.objects.create(
        ClientName="Aprajita Retails",
        ClientCity="Dumka",
        ClientEmail="aprajitaretailsgroup@gmail.com",
        ClientPhone='06434224461',
        ClientContactPerson='Alok Kumar',
        ClientStatus='Active',
        StartDate=datetime.now(timezone.utc).astimezone(),
        EndDate=None,
        Remarks="Main Client",
        PAN_Number="AJHPA7396P",
        GST_Number="20AJHPA7396P1ZV",
        ClientAddress="Bhagalpur Road Dumka",
    )

    store_group = StoreGroup.objects.create(
        Remarks="Main Client",
        PAN_Number="AJHPA7396P",
        GST_Number="20AJHPA7396P1ZV",
        Id="MBO",
        Status='Active',
        PhoneNumber='06434224461',
        ContactPerson='Alok Kumar',
        Email='aprajitaretails.mbo@gmail.com',
        GroupName="Aprajita Retails-MBO",
        Client=client,
        
    )

    store=Store.objects.create(
        StoreName="Aprajita Retails Dumka",
        StoreAddress="Bhagalpur Road Dumka",
        City="Dumka",
        Id='MBO',
        StoreCode='MBO001',
        IsActive=True,
        BeginDate=datetime.now(timezone.utc).astimezone(),
        EndDate=None,
        PAN_Number="AJHPA7396P",
        VatNo="NA",
        StoreGroup=store_group,
        Client=client,
        GST_Number="20AJHPA7396P1ZV",
        
        State='Jharkhand',
        Country='India',
        ZipCode='814101',
        StoreEmailId='aprajitaretails.mbo@gmail.com',
        StorePhoneNumber='06434224461',
        StoreManager='Alok Kumar',
        StoreManegerContactNo='NA',
    )
    TransactionMode.objects.create(TransactionName="Home Expenses", Client=client)
    TransactionMode.objects.create(TransactionName="Mukesh(Home)", Client=client)
    TransactionMode.objects.create(TransactionName="Petty Cash Expenses", Client=client)
    TransactionMode.objects.create(TransactionName="Anit Kumar", Client=client)
    TransactionMode.objects.create(TransactionName="Cash-In", Client=client)
    TransactionMode.objects.create(TransactionName="Cash-Out", Client=client)
    
    BankAccount.objects.create(
        AccountNumber="ICICI Bank",
        AccountHolderName="Aprajita Retails", OpeningBalance=0,CurrentBalance=0,
        Bank=icici, BranchName="Dumka",IFSCCode="ICIC0000001",AccountType=1,IsActive=True , 
        OpeningDate=datetime.now(timezone.utc).astimezone(),
        ClosingDate=None,SharedAccount=True, DefaultBank=True , Client=client, StoreGroup=store_group    
              
    )
    
    ledger= LedgerGroup.objects.create(
       GroupName="Expenses", Client=client, 
       Category = 'Direct Expenses',StoreGroup=store_group,
       Remarks="NA")
    
    party= Party.objects.create(PartyName="No Party", Client=client,
        OpeningDate = datetime.now(timezone.utc).astimezone(),
        ClosingDate = None,
        OpeningBalance =0,
        ClosingBalance = 0,
        Category = 'Expenses',
        GSTIN = 'NA',
        PANNo = 'NA',
        Address = 'NA',
        MobileNo='NA',
        EmailId='NA',
        Remarks = 'NA',
        LedgerGroup = ledger, StoreGroup=store_group
        )
    
    emp=Employee.objects.create(
        FirstName="Alok",
        LastName="Kumar", EmailId="alokkumar@gmail", MobileNo="06434224461", 
        Leavingdate=None,
        JoiningDate=datetime.now(timezone.utc).astimezone(),
        Client=client, 
        StoreGroup=store_group, Location=store,
        EmpId=2, Id='ARD-2016-SM-001', Category = 1,Working=True, 
        Gender =0,
        Address = 'Dumka',
        City = 'Dumka',
        State = 'Jharkhand',
        Country = 'India',
        PinCode = '814101'        

    )
    
    Salesman.objects.create(
        Name="Alok Kumar", Employee=emp, Id='ARD-2016-SM-001', Client=client ,
        StoreGroup=store_group, Location=store,Active=True        
    )
    EDCTerminal.objects.create(
        Client=client, StoreGroup=store_group, Location=store   ,
        Name = 'SBI POS',
        OnDate = datetime.now(timezone.utc).astimezone(),
        TID = 'Missing-1111',
        MID = 'Missing-2222',
        Bank = sbi,
        ProviderName = "State Bank Of India",
        CloseDate = None,
        Active = True ,  
        IsReadOnly=True    
    )
    

