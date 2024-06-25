# Aprajita Retaiils - Network
# Date: 14/03/2024
# Author: Amit Kumar (AKS Labs(India))

#base.py Base Models


from django.db import models

from databases.models.clients import Store,StoreGroup, Client

class BaseModel(models.Model):
        
    Location=models.ForeignKey(Store, on_delete=models.CASCADE)
    StoreGroup=models.ForeignKey(StoreGroup, on_delete=models.CASCADE)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseGroupModel(models.Model):
        
    #Location=models.ForeignKey(Store, on_delete=models.CASCADE)
    StoreGroup=models.ForeignKey(StoreGroup, on_delete=models.CASCADE)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
class BaseGlobalModel(models.Model):
        
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True