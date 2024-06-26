#Core Database Models for AprajitaRetails
#Main Modules Must be includes
#Date: 15/03/2022
#Author: Amit Kumar (Aks Labs(India))

import uuid
from django.db import models 
from core.globalEnums import Gender
from django.utils import timezone

from databases.models.clients import StoreGroup
from databases.models.base import BaseModel, BaseGlobalModel, BaseGroupModel
from databases.models.hrms import Employee

#Customer Model
class Customer(models.Model):
    MobileNo = models.CharField(max_length=255, primary_key=True, db_index=True, unique=True, null=False, editable=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255, null=True, blank=True)
    Age = models.IntegerField()
    DateOfBirth = models.DateTimeField(default= timezone.now)
    City = models.CharField(max_length=255)
    Gender = models.CharField(max_length=11, choices=[(tag.name, tag.value) for tag in Gender])
    NoOfBills = models.IntegerField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    OnDate = models.DateTimeField(default= timezone.now)
    IsReadOnly=models.BooleanField(default=False)

    @property
    def CustomerName(self):
        return f"{self.FirstName} {self.LastName}"
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return self.CustomerName+", "+self.MobileNo
        
#Pos/ EDC Terminal  model



#Contact model 
class Contact(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    EmailId = models.EmailField()
    MobileNo = models.CharField(max_length=14)
    PhoneNo = models.CharField(max_length=14)
    Remarks = models.CharField(max_length=255)
    Address= models.CharField(max_length=100, default="Dumka")
    City=models.CharField(max_length=100, default="Dumka")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.FirstName+" "+self.LastName
    

class Salesman(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=255)
    Employee =models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, blank=True)  
    Active = models.BooleanField()

    class Meta:
        verbose_name = "Salesman"
        verbose_name_plural = "Salesmen"
    def __str__(self):
        return self.Name 