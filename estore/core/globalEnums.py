#Main Core 
# Global Enum for Aprajita Retails
# Date: 15/03/2022
# Author: Amit Kumar (Aks Labs(India))

from enum import Enum
class Gender(Enum):
    Male = 0
    Female = 1
    TransGender = 2
class Unit(Enum):
    Meters = 0
    Nos = 1
    Pcs = 2
    Packets = 3
    NoUnit = 4


class AttUnit(Enum):
    Present = 0
    Absent = 1
    HalfDay = 2
    Sunday = 3
    Holiday = 4
    StoreClosed = 5
    SundayHoliday = 6
    SickLeave = 7
    PaidLeave = 8
    CasualLeave = 9
    OnLeave = 10


class SalaryComponent(Enum):
    NetSalary = 0
    LastPcs = 1
    WOWBill = 2
    SundaySalary = 3
    Incentive = 4
    Others = 5
    Advance = 6
    PaidLeave = 7
    SickLeave = 8
    SalaryAdvance = 9
    Receipts = 10


class EmpType(Enum):
    Salesman = 0
    StoreManager = 1
    HouseKeeping = 2
    Owner = 3
    Accounts = 4
    TailorMaster = 5
    Tailors = 6
    TailoringAssistance = 7
    Others = 8


class TaxType(Enum):
    GST = 0
    SGST = 1
    CGST = 2
    IGST = 3
    VAT = 4
    CST = 5


class NotesType(Enum):
    DebitNote = 0
    CreditNote = 1


class InvoiceType(Enum):
    Sales = 0
    SalesReturn = 1
    ManualSale = 2
    ManualSaleReturn = 3


class PurchaseInvoiceType(Enum):
    Purchase = 0
    PurchaseReturn = 1


class EntryStatus(Enum):
    Added = 0
    Approved = 1
    Rejected = 2
    Updated = 3
    Deleted = 4
    DeleteApproved = 5


class LedgerEntryType(Enum):
    Expenses = 0
    Payment = 1
    Receipt = 2
    Salary = 3
    AdvancePayment = 4
    AdvanceReceipt = 5
    ArvindLimited = 6
    Others = 7


class VoucherType(Enum):
    Payment = 0
    Receipt = 1
    Contra = 2
    DebitNote = 3
    CreditNote = 4
    JV = 5
    Expense = 6
    CashReceipt = 7
    CashPayment = 8


class PayMode(Enum):
    Cash = 0
    Card = 1
    RTGS = 2
    NEFT = 3
    IMPS = 4
    Wallets = 5
    Cheque = 6
    DemandDraft = 7
    Others = 8
    Coupons = 9
    MixPayments = 10
    UPI = 11
    SaleReturn = 12


class PaymentMode(Enum):
    Cash = 0
    Card = 1
    RTGS = 2
    NEFT = 3
    IMPS = 4
    Wallets = 5
    Cheque = 6
    DemandDraft = 7
    Others = 8
    UPI = 9
    CreditNote = 10
    DebitNote = 11


class Size2(Enum):
    S = 0
    M = 1
    L = 2
    XL = 3
    XXL = 4
    XXXL = 5
    T28 = 6
    T30 = 7
    T32 = 8
    T34 = 9
    T36 = 10
    T38 = 11
    T40 = 12
    T41 = 13
    T42 = 14
    T44 = 15
    T46 = 16
    T48 = 17
    FreeSize = 18
    NS = 19
    NOTVALID = 20
    B36 = 21
    B38 = 22
    B40 = 23
    B42 = 24
    B44 = 25
    B46 = 26
    B96 = 27
    B100 = 28
    B104 = 29
    B108 = 30


class Size(Enum):
    S = 0
    M = 1
    L = 2
    XL = 3
    XXL = 4
    XXXL = 5
    C28 = 6
    C30 = 7
    C32 = 8
    C34 = 9
    C36 = 10
    C38 = 11
    C40 = 12
    C41 = 13
    C42 = 14
    C44 = 15
    C46 = 16
    C48 = 17
    C96 = 18
    C100 = 19
    C104 = 20
    C108 = 21
    FreeSize = 22
    NS = 23
    NOTVALID = 24
    C39 = 25
    C92 = 26


class ProductCategory(Enum):
    Fabric = 0
    Apparel = 1
    Accessories = 2
    Tailoring = 3
    Trims = 4
    PromoItems = 5
    Coupons = 6
    GiftVouchers = 7
    Others = 8
    SuitCovers = 9
    InnerWear = 10


class CARD(Enum):
    DebitCard = 0
    CreditCard = 1
    AmexCard = 2


class CARDType(Enum):
    Visa = 0
    MasterCard = 1
    Maestro = 2
    Amex = 3
    Dinners = 4
    Rupay = 5


class LedgerCategory(Enum):
    Credit = 0
    Debit = 1
    Income = 2
    Expenses = 3
    Assets = 4
    Bank = 5
    Loan = 6
    Purchase = 7
    Sale = 8
    Vendor = 9
    Customer = 10


class AccountType(Enum):
    Saving = 0
    Current = 1
    CashCredit = 2
    OverDraft = 3
    Others = 4
    Loan = 5
    CF = 6


class VendorType(Enum):
    EBO = 0
    MBO = 1
    Tailoring = 2
    NonSalable = 3
    OtherSaleable = 4
    Others = 5
    TempVendor = 6
    InHouse = 7
    Distributor = 8
    Brands = 9
    BrandAuth = 10


class DebitCredit(Enum):
    In = 0
    Out = 1


class UserType(Enum):
    Admin = 0
    SuperAdmin = 1
    SuperUser = 2
    PowerUser = 3
    User = 4
    Guest = 5


class RolePermission(Enum):
    Owner = 0
    GeneralManager = 1
    GroupManager = 2
    Accountant = 3
    CA = 4
    StoreManager = 5
    Salesmen = 6
    Guest = 7
    Other = 8


# For Mobile Client
class ConType(Enum):
    Local = 0
    Remote = 1
    RemoteDb = 2
    HybridApi = 3
    HybridDB = 4
    Hybrid = 5


class DBType(Enum):
    Local = 0
    Azure = 1
    API = 2
    Remote = 3
    Mango = 4
    Others = 5
