from django.contrib import admin

# Register your models here.
from databases.models.clients import Client, Store, StoreGroup
from databases.models.accounting import  LedgerGroup
from databases.models.pos import SaleItem
from databases.models.inventory import Brand
from databases.models.hrms import Employee
from databases.models.core import Customer
from databases.models.banking import BankAccount, Bank

admin.site.register(Bank)
admin.site.register(BankAccount)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Client)
admin.site.register(Store)
admin.site.register(StoreGroup)
admin.site.register(LedgerGroup)
admin.site.register(SaleItem)
admin.site.register(Brand)
