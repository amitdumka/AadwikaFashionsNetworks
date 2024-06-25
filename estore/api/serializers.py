from rest_framework import serializers


try:

    from databases.models.clients import Client
    from databases.models.clients import Store
    from databases.models.clients import StoreGroup
    from databases.models.banking import BankAccount
    from databases.models.banking import VendorBankAccount
    from databases.models.accounting import Voucher
    from databases.models.accounting import CashVoucher
    from databases.models.accounting import DailySale
    from databases.models.accounting import CustomerDue
    from databases.models.accounting import Salesman
    from databases.models.hrms import Employee
    from databases.models.hrms import Attendance

except:
    pass 

class ClientSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Client
        except:
            pass    
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Store
        except:
            pass    
        fields = '__all__'

class StoreGroupSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = StoreGroup
        except:
            pass    
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = BankAccount
        except:
            pass    
        fields = '__all__'

class VendorBankAccountSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = VendorBankAccount
        except:
            pass    
        fields = '__all__'

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Voucher
        except:
            pass    
        fields = '__all__'

class CashVoucherSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = CashVoucher
        except:
            pass    
        fields = '__all__'

class DailySaleSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = DailySale
        except:
            pass    
        fields = '__all__'

class CustomerDueSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = CustomerDue
        except:
            pass    
        fields = '__all__'

class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Salesman
        except:
            pass    
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Employee
        except:
            pass    
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Attendance
        except:
            pass    
        fields = '__all__'

