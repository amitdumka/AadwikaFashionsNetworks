# <project>/<app>/management/commands/seed.py
from datetime import datetime, timezone
from django.core.management.base import BaseCommand
from databases.models.accounting import EDCTerminal, LedgerGroup, Ledger, Salesman, TranscationMode
from databases.models.banking import Bank, BankAccount
from databases.models.hrms import Employee
from databases.models.clients import Client, StoreGroup, Store
import random

#TODO - add seed data Check for missing and changed field name and data, and check any table need seeder is required

class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('Aadwika Fashions Database Seeding... ')
        self.stdout.write('Basic data is added to the database. ')
        run_seed(self)
        self.stdout.write('Sedding is completed!')

def run_seed(self):
    # Clear existing data
    Client.objects.all().delete()
    StoreGroup.objects.all().delete()
    Store.objects.all().delete()
    Bank.objects.all().delete()
    TranscationMode.objects.all().delete()
    Employee.objects.all().delete()
    LedgerGroup.objects.all().delete()
    Ledger.objects.all().delete()
    BankAccount.objects.all().delete()
    
    # Create new instances
    

    sbi= Bank.objects.create(Name="State Bank of India")
    icici= Bank.objects.create(Name="ICICI Bank")
    hdfc= Bank.objects.create(Name="HDFC Bank")
    pnb= Bank.objects.create(Name="Punjab National Bank")
    idfc= Bank.objects.create(Name="IDFC Bank")
    bom= Bank.objects.create(Name="Bank Of Maharashtra")
    bob= Bank.objects.create(Name="Bank of Baroda")
    kotak=Bank.objects.create(Name="Kotak Mahindra Bank")
    
    
    
    client = Client.objects.create(
        Name="Aadwika Fashion",
        City="Dumka",
        Email="aadwikafashion@gmail.com",
        Phone='06434224461',
        ContactPerson='Alok Kumar',
        Status='Active',
        StartDate=datetime.now(timezone.utc).astimezone(),
        EndDate=None,
        Remarks="Main Client",
        PAN_Number="AJHPA7396P",
        GST_Number="20AJHPA7396P1ZV",
        Address="Bhagalpur Road Dumka",
    )

    store_group = StoreGroup.objects.create(
        Remarks="Main Client",
        PAN_Number="AJHPA7396P",
        GST_Number="20AJHPA7396P1ZV",
        Id="MBO",
        Status='Active',
        PhoneNumber='06434224461',
        ContactPerson='Alok Kumar',
        Email='aadwikafashion.mbo@gmail.com',
        Name="Aadwika Fashion-MBO",
        Client=client,
        
    )

    store=Store.objects.create(
        Name="Aadwika Fashion Dumka",
        Address="Bhagalpur Road Dumka",
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
        EmailId='aadwikafashion.mbo@gmail.com',
        PhoneNumber='06434224461',
        StoreManager='Alok Kumar',
        StoreManegerContactNo='NA',
    )
    TranscationMode.objects.create(TransactionName="Home Expenses", Client=client)
    TranscationMode.objects.create(TransactionName="Mukesh(Home)", Client=client)
    TranscationMode.objects.create(TransactionName="Petty Cash Expenses", Client=client)
    TranscationMode.objects.create(TransactionName="Anit Kumar", Client=client)
    TranscationMode.objects.create(TransactionName="Cash-In", Client=client)
    TranscationMode.objects.create(TransactionName="Cash-Out", Client=client)
    
    BankAccount.objects.create(
        AccountNumber="SBI CC",
        AccountHolderName="Amit Kumar", OpeningBalance=0,CurrentBalance=0,
        Bank=sbi, BranchName="Lic Coloney, Dumka",IFSCCode="SBIN1740",AccountType=1,IsActive=True , 
        OpeningDate=datetime.now(timezone.utc).astimezone(),
        ClosingDate=None,SharedAccount=True, DefaultBank=True , Client=client, StoreGroup=store_group    
              
    )
    
    ledger= LedgerGroup.objects.create(
       GroupName="Expenses", Client=client, 
       Category = 'Direct Expenses',StoreGroup=store_group,
       Remarks="NA")
    
    party= Ledger.objects.create(Name="No Party", Client=client,
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
        AccountNumber = 'SBI CC',
        ProviderName = "State Bank Of India",
        CloseDate = None,
        Active = True ,  
        IsReadOnly=True    
    )
    

