import uuid
from django.db import models
from django.utils import timezone
from databases.models.base import BaseGlobalModel, BaseModel , BaseGroupModel
from databases.models.clients import StoreGroup,Store
from databases.models.core import Customer,Salesman
from core.globalEnums import InvoiceType, Unit, TaxType, Size, ProductCategory,PaymentMode,PayMode, Gender,PurchaseInvoiceType,CARD,CARDType,TaxType, VendorType


#SECTION - Models

class Product(BaseGroupModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name= models.CharField(max_length=255)
    Barcode = models.CharField(max_length=255)
    Description= models.CharField(max_length=255)
    MRP= models.DecimalField(max_digits=10, decimal_places=2)
    BasicRate= models.DecimalField(max_digits=10, decimal_places=2)
    TaxRate= models.DecimalField(max_digits=10, decimal_places=2)
    TaxType= models.IntegerField(choices=[(tag.value, tag.name) for tag in TaxType])
    Unit= models.IntegerField(choices=[(tag.value, tag.name) for tag in Unit])
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    def __str__(self):
        return self.Name+" - "+self.Barcode
    
class Stock(BaseGroupModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Barcode = models.CharField(max_length=255)
    PurchaseQuantity = models.DecimalField(max_digits=10, decimal_places=2)
    SoldQuantity = models.DecimalField(max_digits=10, decimal_places=2)    
    CostPrice = models.DecimalField(max_digits=10, decimal_places=2)
    TaxAmount= models.DecimalField(max_digits=10, decimal_places=2)
    MRP= models.DecimalField(max_digits=10, decimal_places=2)
    TaxRate= models.DecimalField(max_digits=10, decimal_places=2)
    Unit= models.IntegerField(choices=[(tag.value, tag.name) for tag in Unit])
    
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
    def __str__(self):
        return self.Barcode+" - "+self.Product.Name
    def CurrentStock(self):
        return self.PurchaseQuantity - self.SoldQuantity
    def StockValue(self):
        return self.CurrentStock() * self.CostPrice
class ProductCategory(models.Model):
    Id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=255, unique=True)
    Description= models.CharField(max_length=255)
    class  Meta:
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategories"
    def __str__(self):
        return self.Name
class ProductSubCategory(models.Model):
    Id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=255, unique=True)
    Description= models.CharField(max_length=255)
    class  Meta:
        verbose_name = "ProductSubCategory"
        verbose_name_plural = "ProductSubCategories"
    def __str__(self):
        return self.Name
        
class ProductDetail(BaseGlobalModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Barcode = models.CharField(max_length=255)
    StyleCode = models.CharField(max_length=255)
    BaseColor = models.CharField(max_length=255)
    Brand= models.CharField(max_length=255)  # Add Ref Link
    SupplierId= models.CharField(max_length=255) # Add Ref Link
    Category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    SubCategory=models.ForeignKey(ProductSubCategory, on_delete=models.DO_NOTHING)


class Vendor(BaseGlobalModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=255) 
    Address= models.CharField(max_length=255)
    City= models.CharField(max_length=255)
    PhoneNo= models.CharField(max_length=255)
    GSTIN= models.CharField(max_length=255)
    PanNo= models.CharField(max_length=255)
    Email= models.CharField(max_length=255)
    VendorType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in VendorType])
    OnDate = models.DateTimeField(default= timezone.now)
    EndDate = models.DateTimeField(null=True, blank=True)
    Active = models.BooleanField()
    LedgerId=models.CharField(max_length=255) #TODO: Make Ledger or PartyId
    class  Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
    def __str__(self):
        return self.Name+" - "+self.GSTIN

class Purchase(BaseModel):
    
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    InwardNumber = models.CharField(max_length=255, unique=True)
    InwardDate = models.DateTimeField(default= timezone.now)
    Vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    InvoiceNumber = models.CharField(max_length=255)
    InvoiceDate = models.DateTimeField(default= timezone.now)
    
    OrderId = models.CharField(max_length=255)
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)
    Count=models.IntegerField()
    
    MRP = models.DecimalField(max_digits=10, decimal_places=2)
    DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
    
    BasicAmount = models.DecimalField(max_digits=10, decimal_places=2)
    TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
    RoundOff = models.DecimalField(max_digits=10, decimal_places=2)
    
    BillAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Frieght= models.DecimalField(max_digits=10, decimal_places=2)
    
    RefNumber= models.CharField(max_length=255)
    PaidDate= models.DateTimeField(null=True, blank=True)
    PaidAmount= models.DecimalField(max_digits=10, decimal_places=2,default=0)
    Paid = models.BooleanField(default=False)
    class  Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"
    def __str__(self):
        return self.InvoiceNumber+" - "+self.BillAmount+" - Paid - "+self.Paid
    
class PurchaseItem(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Purchase=models.ForeignKey(Purchase, on_delete=models.CASCADE)
    
    InvoiceDate= models.DateTimeField(default= timezone.now)
    InvoiceNumber= models.CharField(max_length=255)
    
    Barcode=models.CharField(max_length=255)
    Quantity=models.DecimalField(max_digits=10, decimal_places=2)
    Unit= models.IntegerField(choices=[(tag.value, tag.name) for tag in  Unit])
    MRP = models.DecimalField(max_digits=10, decimal_places=2)
    
    BasicAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
    TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Amount = models.DecimalField(max_digits=10, decimal_places=2) 
    TaxRate = models.DecimalField(max_digits=10, decimal_places=2)
    
    class  Meta:
        verbose_name = "PurchaseItem"
        verbose_name_plural = "PurchaseItems"
    def __str__(self):
        return self.InvoiceNumber+" - "+self.Barcode+" - "+self.Amount
    
 
    

#!SECTION:Models




#Brand Model
class Brand(models.Model):
    BrandCode = models.CharField(max_length=255, primary_key=True)
    BrandName = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Brands"
        verbose_name="Brand"

    def __str__(self):
        return self.BrandName

class Tax(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
    Name = models.CharField(max_length=255 )
    TaxType = models.IntegerField(choices=[(tag.value, tag.name) for tag in TaxType])
    CompositeRate = models.DecimalField(max_digits=10, decimal_places=2,  )
    OutPutTax = models.BooleanField(default=False )

    class Meta:
        verbose_name_plural = "Taxs"
        verbose_name = "Tax"
    def  __str__(self):
        return self.Name+" - "+str(self.CompositeRate)


#Supplier Model
class Supplier(models.Model):
    SupplierName = models.CharField(max_length=255, primary_key=True)
    Warehouse = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Suppliers"
        verbose_name="Supplier"
    def  __str__(self):
        return self.SupplierName


# class PSale(models.Model):
#     InvoiceNo = models.CharField(max_length=255, primary_key=True)
#     InvoiceCode = models.CharField(max_length=255)
#     class Meta:
#         abstract=True

# class Sale(models.Model):
#     InvoiceNo = models.CharField(max_length=255, primary_key=True)
#     OnDate = models.DateTimeField(default= timezone.now)
#     RefInvoiceNo = models.CharField(max_length=255)
#     SaleReturn = models.BooleanField()
#     Qty = models.DecimalField(max_digits=10, decimal_places=2)
#     MRP = models.DecimalField(max_digits=10, decimal_places=2)
#     DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     BasicPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     RoundOff = models.DecimalField(max_digits=10, decimal_places=2)
#     BillAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     SalesmanId = models.CharField(max_length=255)
#     Paid = models.BooleanField()
#     ServiceBill = models.BooleanField()
#     SaleItems = models.ManyToManyField('SaleItem')


#

# #Product Sub Category model
# class ProductSubCategory(models.Model):
#     SubCategory = models.CharField(max_length=255, primary_key=True)
#     ProductCategory =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  ProductCategory])
#     class Meta:
#         verbose_name_plural = "ProductSubCategories"
#         verbose_name="ProductSubCategory"
#     def __str__(self):
#         return self.SubCategory
        

# #Product Type Model
# class ProductType(models.Model):
#     ProductTypeId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
#     ProductTypeName = models.CharField(max_length=255)
#     class Meta:
#         verbose_name_plural = "ProductTypes"
#         verbose_name="ProductType"
#     def __str__(self):
#         return self.ProductTypeName

# #Product Item model 
# class ProductItem(BaseGroupModel):
#     Barcode = models.CharField(max_length=255, primary_key=True, unique=True, null=False)
#     Name = models.CharField(max_length=255)
#     Description = models.CharField(max_length=255, null=True,blank=True)
#     StyleCode = models.CharField(max_length=255, null=True, blank=True)
#     Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
#     TaxType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  TaxType])
#     MRP = models.DecimalField(max_digits=10, decimal_places=2)
#     Size =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  Size])
#     ProductCategory =  models.IntegerField(choices=[(tag.value, tag.name) for tag in ProductCategory])
#     ProductSubCategory = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE, null=True, blank=True)
#     ProductType = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True)
#     HSNCode = models.CharField(max_length=255, null=True, blank=True)
#     Unit =  models.IntegerField(choices=[(tag.value, tag.name) for tag in Unit])
    
#     class Meta:
#         verbose_name_plural = "ProductItems"
#         verbose_name="ProductItem"

#     def  __str__(self):
#         return self.Barcode+" - "+self.Name+" - "+self.StyleCode
   
#Vendor Model
# # class Vendor(BaseGlobalModel):
# #     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
# #     VendorName = models.CharField(max_length=255)
# #     VendorType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in VendorType])
# #     OnDate = models.DateTimeField(default= timezone.now)
# #     EndDate = models.DateTimeField(null=True, blank=True)
# #     Active = models.BooleanField()
# #     class Meta:
# #         verbose_name_plural = "Vendors"
# #         verbose_name="Vendor"

# #     def __str__(self)  :
# #         return self.VendorName

# #ProductPurhcase Model
# class ProductPurchase(BaseModel):

#     InwardNumber = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
#     InwardDate = models.DateTimeField(default= timezone.now)
#     InvoiceNo = models.CharField(max_length=255)
     
#     InvoiceType = models.IntegerField(choices=[(tag.value, tag.name) for tag in  PurchaseInvoiceType])
#     TaxType =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  TaxType])
#     OnDate = models.DateTimeField(default= timezone.now)
#     BasicAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     ShippingCost = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     Count = models.IntegerField()
#     BillQty = models.DecimalField(max_digits=10, decimal_places=2)
#     FreeQty = models.DecimalField(max_digits=10, decimal_places=2)
#     TotalQty = models.DecimalField(max_digits=10, decimal_places=2)
#     Paid = models.BooleanField()
#     Warehouse = models.CharField(max_length=255, null=True, blank=True)
#     Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
#     #Items = models.ManyToManyField('PurchaseItem')
#     class Meta:
#         verbose_name_plural = "ProductPurchases"
#         verbose_name="ProductPurchase"

#     def __str__(self):
#         return self.InwardNumber+" - "+self.InvoiceNo+" - "+self.TotalAmount


# #Purchase Item
# class PurchaseItem(BaseModel):
#     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
#     InvoiceNumber = models.CharField(max_length=255)
#     Barcode = models.ForeignKey(ProductItem, on_delete=models.DO_NOTHING, null=True, blank=True)
#     Qty = models.DecimalField(max_digits=10, decimal_places=2)
#     FreeQty = models.DecimalField(max_digits=10, decimal_places=2)
#     CostPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     Unit =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  Unit])
#     DiscountValue = models.DecimalField(max_digits=10, decimal_places=2)
#     TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
#     CostValue = models.DecimalField(max_digits=10, decimal_places=2)
#     InwardNumber = models.ForeignKey(ProductPurchase, on_delete=models.CASCADE, null=True, blank=True)
    
#     class Meta:
#         verbose_name_plural = "PurchaseItems"
#         verbose_name="PurchaseItem"
#     def __str__(self):
#         return self.InvoiceNumber+" - "+self.Barcode+" - "+self.Qty
 
#Stock Model   
# # class Stock(BaseModel):
# #     Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  db_index=True, unique=True)
# #     Barcode = models.ForeignKey(ProductItem, on_delete=models.DO_NOTHING, null=True, blank=True)
# #     PurchaseQty = models.DecimalField(max_digits=10, decimal_places=2)
# #     SoldQty = models.DecimalField(max_digits=10, decimal_places=2)
# #     HoldQty = models.DecimalField(max_digits=10, decimal_places=2)
# #     CostPrice = models.DecimalField(max_digits=10, decimal_places=2)
# #     MRP = models.DecimalField(max_digits=10, decimal_places=2)
# #     Unit =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  Unit])
# #     MultiPrice = models.BooleanField(default=False)
    

#     @property
#     def CurrentQty(self):
#         return self.PurchaseQty - self.SoldQty - self.HoldQty

#     @property
#     def CurrentQtyWH(self):
#         return self.PurchaseQty - self.SoldQty

#     @property
#     def StockValue(self):
#         return self.CurrentQty * self.CostPrice

#     @property
#     def StockValueWH(self):
#         return self.CurrentQtyWH * self.CostPrice

#     class Meta:
#         verbose_name = "Stock"
#         verbose_name_plural = "Stocks"
    
#     def __str__(self):
#         return self.Barcode+" - "+str(self.MRP)+" - "+str(self.CurrentQty)
 
