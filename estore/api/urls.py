from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("clients/((?P<pk>\d+)/)?", csrf_exempt(ClientView.as_view())),
	re_path("stores/((?P<pk>\d+)/)?", csrf_exempt(StoreView.as_view())),
	re_path("storegroups/((?P<pk>\d+)/)?", csrf_exempt(StoreGroupView.as_view())),
	re_path("bankaccounts/((?P<pk>\d+)/)?", csrf_exempt(BankAccountView.as_view())),
	re_path("vendorbankaccounts/((?P<pk>\d+)/)?", csrf_exempt(VendorBankAccountView.as_view())),
	re_path("vouchers/((?P<pk>\d+)/)?", csrf_exempt(VoucherView.as_view())),
	re_path("cashvouchers/((?P<pk>\d+)/)?", csrf_exempt(CashVoucherView.as_view())),
	re_path("dailysales/((?P<pk>\d+)/)?", csrf_exempt(DailySaleView.as_view())),
	re_path("customerdues/((?P<pk>\d+)/)?", csrf_exempt(CustomerDueView.as_view())),
	re_path("salesmen/((?P<pk>\d+)/)?", csrf_exempt(SalesmanView.as_view())),
	re_path("employees/((?P<pk>\d+)/)?", csrf_exempt(EmployeeView.as_view())),
	re_path("attendances/((?P<pk>\d+)/)?", csrf_exempt(AttendanceView.as_view())),

]