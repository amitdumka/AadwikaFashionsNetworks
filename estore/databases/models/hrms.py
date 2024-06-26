

#Create your models here.
import calendar
import datetime
 
import uuid
from django.db import models
 
from databases.models.base import BaseGroupModel, BaseModel
from databases.models.clients import Store, StoreGroup, Client
from core.globalEnums import EmpType, Gender, AttUnit, SalaryComponent, PayMode, PaymentMode
 
import logging
 
from django.utils import timezone

logger = logging.getLogger(__name__)

class Person(BaseModel):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Gender =models.IntegerField(choices=[(tag.value, tag.name) for tag in Gender]    )
    MobileNo = models.CharField(max_length=255)
    EmailId = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    PinCode = models.CharField(max_length=255)
    class Meta:
        abstract = True
    def FullName(self):
        return self.FirstName + " " + self.LastName
        




class Employee(Person):
    Id = models.CharField(max_length=255, primary_key=True, null=False,editable=False, unique=True, db_index=True,)
    EmpId = models.IntegerField()  # Temp Till full migration is done.
    JoiningDate = models.DateTimeField(default= timezone.now)
    Leavingdate = models.DateTimeField(null=True, blank=True)
    Working = models.BooleanField(default=True)    
    Category =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  EmpType]    )
    
    def StaffName(self):
        return self.FirstName + " " + self.LastName
    def __str__(self):
        return self.Id+" - "+self.StaffName

    class Meta:
       verbose_name = "Employee"
       verbose_name_plural = "Employees"


class EmployeeDetails(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE,primary_key=True,null=False, unique=True, db_index=True, editable=True)
    DateOfBirth = models.DateTimeField(default= timezone.now)
    AdharNumber = models.CharField(max_length=255)
    PanNo = models.CharField(max_length=255)
    OtherIdDetails = models.CharField(max_length=255)
    FatherName = models.CharField(max_length=255)
    MaritalStatus = models.CharField(max_length=255)
    SpouseName = models.CharField(max_length=255, null=True)
    HighestQualification = models.CharField(max_length=255)
    BankAccountNumber = models.CharField(max_length=255)
    BankNameWithBranch = models.CharField(max_length=255)
    IFSCCode = models.CharField(max_length=255)

    class Meta:
        verbose_name = "EmployeeDetails"
        verbose_name_plural = "EmployeeDetails"
    def __str__(self):
        return self.Employee.FirstName + " " + self.Employee.LastName+" - "+ self.DateOfBirth+", "+self.AdharNumber
    

class Attendance(BaseModel):
    Id = models.CharField(max_length=30, primary_key=True, db_index=True, unique=True, null=False, editable=False)   
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)   
    OnDate = models.DateTimeField(default= timezone.now)
    Status =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  AttUnit]    )
    EntryTime = models.CharField(max_length=255, null=True)
    Remarks = models.CharField(max_length=255, null=True)
    IsReadOnly=models.BooleanField(default=False)  
 
    #Check For Duplicate attendance
    def checkAttendance(self, id):
        check_exist= Attendance.objects.filter(AttendanceId=id).count()
        if check_exist>0 :
            return True
        else :
            return False

    
    class Meta:
        unique_together = (('Employee', 'OnDate'),)
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
    def __str__(self):
        return self.Employee.FirstName + " " + self.Employee.LastName+" - "+ str(self.OnDate)+" - "+str(self.Status)
    
#Monthly Attendance
class MonthlyAttendance(BaseModel):
   
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)   
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
   
    OnDate = models.DateTimeField(default= timezone.now)
    Present = models.IntegerField(default=0)
    HalfDay = models.IntegerField(default=0)
    Sunday = models.IntegerField(default=0)
    PaidLeave = models.IntegerField(default=0)
    Holidays = models.IntegerField(default=0)
    CasualLeave = models.IntegerField(default=0)
    Absent = models.IntegerField(default=0)
    WeeklyLeave = models.IntegerField(default=0)
    Remarks = models.CharField(max_length=255)
    NoOfWorkingDays = models.IntegerField(default=0)
    IsReadOnly=models.BooleanField(default=False)
   
    @property
    def DayInMonths(self):
        return calendar.monthrange(self.OnDate.year, self.OnDate.month)

    @property
    def Count(self):
        return self.present + self.HalfDay + self.Sunday + self.PaidLeave + self.CasualLeave + self.Absent + self.WeeklyLeave + self.Holidays

    @property
    def BillableDays(self):
        return (self.HalfDay / 2.0) + self.Present + self.Sunday + self.PaidLeave + self.Holidays

    @property
    def Valid(self):
        return self.count == self.day_in_months
    class Meta:
        verbose_name = "MonthlyAttendance"
        verbose_name_plural = "MonthlyAttendances"



class SalaryLedger(BaseGroupModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
   
    Employee=models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
   
    OnDate = models.DateTimeField(default= timezone.now)
    Particulars = models.CharField(max_length=255)
    InAmount = models.DecimalField(max_digits=10, decimal_places=2)
    OutAmount = models.DecimalField(max_digits=10, decimal_places=2)
   
    
    class Meta:
       #db_table SalaryLedger
        verbose_name = "SalaryLedger"
        verbose_name_plural = "SalaryLedgers"

class TimeSheet(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
   
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
   
    OutTime = models.DateTimeField(default= timezone.now)
    InTime = models.DateTimeField(null=True)
    Reason = models.CharField(max_length=255)

    @property
    def Duration(self):
        return (self.InTime if self.InTime else datetime.now()) - self.OutTime

    class Meta:
       #db_table TimeSheet
        verbose_name = "TimeSheet"  
        verbose_name_plural = "TimeSheets"

 
class Salary(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
   
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)   
    EffectiveDate = models.DateTimeField(default= timezone.now)
    
    BasicSalary = models.DecimalField(max_digits=10, decimal_places=2)
    ExtraSalary= models.DecimalField(max_digits=10, decimal_places=2)

    CloseDate = models.DateTimeField(null=True)
    Effective = models.BooleanField(default=True)
    
    WowBill = models.BooleanField(default=False)
    Incentive = models.BooleanField(default=False)
    LastPcs = models.BooleanField(default=False)
    SundayBillable = models.BooleanField(default=False)
    FullMonth = models.BooleanField(default=False)
   
    
    class Meta:
       #db_table Salary
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"


class SalaryPayment(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    SlipNo = models.PositiveIntegerField(  null=True, blank=True,   db_index=True, editable=False, auto_created=True)
    SalaryMonth = models.IntegerField()
    SalaryComponet =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  SalaryComponent]    )
    OnDate = models.DateTimeField(default= timezone.now)
    Amount = models.DecimalField (max_digits=10, decimal_places=2)
    PaymentMode = models.IntegerField(choices=[(tag.value, tag.name) for tag in PaymentMode]    )
    Details = models.CharField(max_length=255)
    
    class Meta:
       #db_table SalaryPayment
        verbose_name = "SalaryPayment"
        verbose_name_plural = "SalaryPayments"
        
    #TODO: Implements Custom Save this model , add negative value for receipts 
    #TODO: add Entry on Salary Ledger for payment and receipts so No need to handle seprately
    #TODO: User Function to add Salary Ledger for payment and receipts



#PaySlip model: This will be autogenrated always. on monthly basis

class PaySlip(BaseModel):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    OnDate = models.DateTimeField(default= timezone.now)
    Month = models.IntegerField()
    Year = models.IntegerField()
    
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    #SalaryId = models.ForeignKey(Salary, on_delete=models.CASCADE, null=True)

    CurrentSalary = models.ForeignKey(Salary, on_delete=models.CASCADE, null=True)
    BasicSalaryRate = models.DecimalField(max_digits=10, decimal_places=2)
    BasicSalary = models.DecimalField(max_digits=10, decimal_places=2)
    TotalPayableSalary = models.DecimalField(max_digits=10, decimal_places=2)
    NoOfDaysPresent = models.DecimalField(max_digits=10, decimal_places=2)
    WorkingDays = models.IntegerField()
    TotalSale = models.DecimalField(max_digits=10, decimal_places=2)
    SaleIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    WowBillAmount= models.DecimalField(max_digits=10, decimal_places=2)
    WowBillIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    LastPcsAmount = models.DecimalField(max_digits=10, decimal_places=2)
    LastPcsIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    OtherIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    GrossSalary = models.DecimalField(max_digits=10, decimal_places=2)
    TDSDeduction = models.DecimalField(max_digits=10, decimal_places=2)
    PFDeduction = models.DecimalField(max_digits=10, decimal_places=2)
    AdvanceDeducation= models.DecimalField(max_digits=10, decimal_places=2)
    Remarks = models.CharField(max_length=255, null=True,blank=True)
    
    class Meta:
       #db_table PaySlip
        verbose_name = "PaySlip"
        verbose_name_plural = "PaySlips"


# #Salary 
# class Salary(models.Model):
#     salaryId = models.IntegerField(primary_key=True)
#     employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     salaryBasicAmount = models.IntegerField()
#     salaryHRA = models.IntegerField()
#     salaryDA=models.IntegerField()
#     salaryPF = models.IntegerField()
#     salaryTDS = models.IntegerField()
#     salaryOhterAllowance = models.IntegerField()
#     salaryOtherDeduction = models.IntegerField()
#     salaryIncentive=models.IntegerField()
#     salaryTotalSalary = models.IntegerField()
#     noodworkingDays = models.IntegerField()
#     salarybonus = models.IntegerField()

# #Payslip model 
# class Payslip(models.Model):
#     payslipId = models.IntegerField(primary_key=True)
#     employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     payslipMonth = models.IntegerField()
#     payslipYear = models.IntegerField()
#     payslipBasicAmount = models.IntegerField()
#     payslipHRA = models.IntegerField()
#     payslipDA=models.IntegerField()
#     payslipPF = models.IntegerField()
#     payslipTDS = models.IntegerField()
#     payslipOhterAllowance = models.IntegerField()
#     payslipOtherDeduction = models.IntegerField()
#     payslipIncentive=models.IntegerField()
#     payslipTotalSalary = models.IntegerField()
#     payslipNetSalary = models.IntegerField()
#     payslipStatus=models.CharField(max_length=100)
#     payslipRemarks = models.CharField(max_length=100)
#     payslipDate = models.DateTimeField(default= timezone.now)
#     payslipPaymentDate = models.DateTimeField(default= timezone.now)
#     payslipPaymentMode = models.CharField(max_length=100)
#     payslipPaymentAmount = models.IntegerField()
#     payslipPaymentRemarks = models.CharField(max_length=100)