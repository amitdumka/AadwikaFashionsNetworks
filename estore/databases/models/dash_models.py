#Dashboard Models  to hold data from different database. 
#Date: 20/02/2024
#Author: Amit Kumar (Aks Labs(India))

from django.db import models

# Create your models here.


class DashModel(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    storegroup = models.ForeignKey('StoreGroup', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class SaleInfo(DashModel):
    TodaySale=models.DecimalField(max_digits=10, decimal_places=2)
    WeeklySale=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlySale=models.DecimalField(max_digits=10, decimal_places=2)
    YearlySale=models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name_plural = "SaleInfos"
        verbose_name="SaleInfo"



class VoucherInfo(DashModel):
    TodayExpenes=models.DecimalField(max_digits=10, decimal_places=2)
    TodayPayments=models.DecimalField(max_digits=10, decimal_places=2)
    TodayReceipts=models.DecimalField(max_digits=10, decimal_places=2)
    WeeklyExpenes=models.DecimalField(max_digits=10, decimal_places=2)
    WeeklyPayments=models.DecimalField(max_digits=10, decimal_places=2)
    WeeklyReceipts=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyExpenes=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyPayments=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyReceipts=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyExpenes=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyPayments=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyReceipts=models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name_plural = "VoucherInfos"
        verbose_name="VoucherInfo"


class BankingInfo(DashModel):
    TodayBankDeopist=models.DecimalField(max_digits=10, decimal_places=2)
    TodayBySales=models.DecimalField(max_digits=10, decimal_places=2)
    TodayBankWithdraw=models.DecimalField(max_digits=10, decimal_places=2)    
    MonthlyBankDeopist=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyBySales=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyBankWithdraw=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyBankDeopist=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyBySales=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyBankWithdraw=models.DecimalField(max_digits=10, decimal_places=2)
    BankBalance=models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name_plural = "BankingInfos"
        verbose_name="BankingInfo"

class InventoryInfo(DashModel):
    TodayStock=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyStock=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyStock=models.DecimalField(max_digits=10, decimal_places=2)
    TodaySaleQty=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlySaleQty=models.DecimalField(max_digits=10, decimal_places=2)
    YearlySaleQty=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyReturnQty=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyReturnQty=models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyPurchaseReturnQty=models.DecimalField(max_digits=10, decimal_places=2)
    YearlyPurchaseReturnQty=models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name_plural = "InventoryInfos"
        verbose_name="InventoryInfo"

class HRMInfo(DashModel):
    EmployeeName=models.CharField(max_length=255)
    Today=models.CharField(max_length=255)
    Attendance=models.DecimalField(max_digits=10, decimal_places=2)
    SaleAverage=models.DecimalField(max_digits=10, decimal_places=2)
    Sale=models.DecimalField(max_digits=10, decimal_places=2)
    Salesman=models.BooleanField()
    
    class Meta:
        verbose_name_plural = "HRMInfos"
        verbose_name="HRMInfo"

# create class to hold list of HRM info data.



    