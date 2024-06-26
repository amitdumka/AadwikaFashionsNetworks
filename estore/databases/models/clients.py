#Aprajita Retails - Network
# Date: 14/03/2024
# Author: Amit Kumar (AKS Labs(India))

#clients.py
# It is model for clients like Client , StoreGroup and Store.

import uuid
from django.db import models 
from django.utils import timezone
from core.globalEnums import StoreCategory


class ClientBase(models.Model):
  #  Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=100)
    Address= models.CharField(max_length=100, default="Dumka")
    City=models.CharField(max_length=100, default="Dumka")
    State=models.CharField(max_length=100, default="Jharkhand")
    Country=models.CharField(max_length=100, default="India")
    PinCode=models.CharField(max_length=100, default="814101")
    Email = models.EmailField()
    Phone = models.CharField(max_length=14)
    PANNumber=models.CharField(max_length=100)
    GSTIN=models.CharField(max_length=100)
    Active=models.BooleanField(default=True)
    Remarks=models.CharField(max_length=200, null=True, blank=True)
    StartDate = models.DateTimeField(default= timezone.now)
    EndDate = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True
    def __str__(self):
        return self.Name+", "+self.Address

#Client model
class Client(ClientBase):
            
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True) 
    OwnerName=models.CharField(max_length=100)
    OwnerContactNo=models.CharField(max_length=100)
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
     

#StoreGroup model
class StoreGroup(ClientBase):
    class Meta:
        verbose_name = "StoreGroup"
        verbose_name_plural = "StoreGroups"

    Id = models.CharField(max_length=15, primary_key=True, db_index=True, unique=True, null=False, editable=True)   
    StoreCategory=models.IntegerField(choices=[(tag.value, tag.name) for tag in  StoreCategory]    )
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)
    

    def __str__(self):        return self.Name
    def save(self, *args, **kwargs):       
        super(StoreGroup, self).save(*args, **kwargs)


#Store model
class Store(ClientBase):
        Id = models.CharField(primary_key=True, db_index=True, unique=True, null=False, editable=True, max_length=15)
        StoreCode= models.CharField(max_length=15,unique=True)
        StoreManager=models.CharField(max_length=100)
        StoreManegerContactNo=models.CharField(max_length=100)      
        StoreCategory=models.IntegerField(choices=[(tag.value, tag.name) for tag in  StoreCategory]    ) 
        StoreGroup=models.ForeignKey(StoreGroup, on_delete=models.CASCADE)
        Client=models.ForeignKey(Client, on_delete=models.CASCADE)
        
        class Meta:
            verbose_name = "Store"
            verbose_name_plural = "Stores"


class Address(models.Model):
    Address= models.CharField(max_length=100, default="Dumka")
    City=models.CharField(max_length=100, default="Dumka")
    State=models.CharField(max_length=100, default="Jharkhand")
    Country=models.CharField(max_length=100, default="India")
    ZipCode=models.CharField(max_length=100, default="814101")
 
class ContactInfo(Address):
    Email= models.EmailField(max_length=255)
    Phone= models.CharField(max_length=14)
    
     