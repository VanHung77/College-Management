from django.db import models
from django.contrib.auth.models import User
# Create your models here.

BranchType = [
    ('CS','CS'),
    ('DS','DS'),
    ('SE','SE'),
    ('IT','IT'),
    ('IS','IS'),
]
CourseType = [
    ('K15','K15'),
    ('K16','K16'),
    ('K17','K17'),
    ('K18','K18'),
    ('K19','K19'),
    ('K20','K20'),
]
date = [str(x) for x in range(2013,2050)]
# date=' '.join(date)
YearType = []
for x in date:
    YearType.append((x,x))

MonthType = [ ('Jan','Jan'), ('Feb','Feb'), ('Mar','Mar'), ('Apr','Apr'), ('May','May'), ('Jun','Jun'), ('Jul','Jul'), 
             ('Aug','Aug'), ('Sept','Sept'), ('Oct','Oct'), ('Nov','Nov'), ('Dec','Dec'),]
class Student(models.Model):

    BranchType = models.TextChoices('BranchType', 'CS DS SE IT IS')
    
    date = [str(x) for x in range(2013,2050)]
    date=' '.join(date)
    YearType = models.TextChoices('YearType', date)

    CourseType = models.TextChoices('CourseType', 'K15 K16 K17 K18 K19 K20')

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    roll = models.CharField('MSSV', max_length=8, primary_key=True, blank=False)
    firstname = models.CharField('First_Name', max_length=250, blank=False)
    middlename = models.CharField('Middle_Name', max_length=250, null=True, blank=True)
    lastname = models.CharField('Last_Name', max_length=250, null=True, blank=True)
    email = models.EmailField('Email', max_length=250, blank=False)
    phone = models.CharField('Phone', max_length=15, blank=False)
    branch = models.CharField('Chuyên ngành', max_length=15, blank=False, choices=BranchType.choices)
    Year = models.CharField('Year', max_length=4, blank=False, choices=YearType.choices)
    course = models.CharField('Khoá', max_length=8, blank=False, choices=CourseType.choices)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)

    
    template = '{} {}'
    def __str__(self):
        return self.roll
        return self.template.format(self.roll,self.firstname)



class Semester(models.Model):

    date = [str(x) for x in range(2013,2050)]
    date=' '.join(date)

    SemesterType = models.TextChoices('Học Kỳ', 'First Second Third Fourth Fifth Sixth Seventh Eighth')
    Monsoon_WinterType = models.TextChoices('Monsoon_WinterType', 'HKI HKII')
    PaidType = models.TextChoices('PaidType', 'NotPaid Paid')
    YearType = models.TextChoices('YearType', date)
    MonthType = models.TextChoices('MonthType', 'Jan Feb Mar Apr May Jun Jul Aug Sept Oct Nov Dec')

    roll = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False) 
    semestertype = models.CharField('Semester_type', max_length=50, blank=False, choices=SemesterType.choices)
    monsoon_wintertype = models.CharField('Học Kỳ trong năm', max_length=50, blank=False, choices=Monsoon_WinterType.choices)
    Year = models.CharField('Year', max_length=50, blank=False, choices=YearType.choices)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)


    # Tution Fee
    tution_fee = models.CharField('Phí BHYT', max_length=50, null=True, blank=True, default='0')
    # tution_fee_status = models.CharField('Tution_Fee_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)


    # Hostel Fee
    hostel_fee = models.CharField('Phí ký túc xá', max_length=50, null=True, blank=True, default='0')
    # hostel_fee_status = models.CharField('Hostel_Fee_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)
    

    #  mess section

    mon_choices = [
    ('Thị giác máy tính','Thị giác máy tính'),
    ('Học máy','Học máy'),
    ('Học sâu','Học sâu'),
    ('Xử lý ngôn ngữ tự nhiên','Xử lý ngôn ngữ tự nhiên'),
    ('Phát triển ứng dụng','Phát triển ứng dụng'),
    ('Nhập môn dữ liệu lớn','Nhập môn dữ liệu lớn'),
    ('Khai thác dữ liệu','Khai thác dữ liệu'),
    ('Khai phá đồ thị','Khai phá đồ thị'),
    ('Các nền tảng dữ liệu','Các nền tảng dữ liệu'),
    ('Công nghệ mới trong phát triển ứng dụng','Công nghệ mới trong phát triển ứng dụng'),
    ('Phân tích dữ liệu Bayesian','Phân tích dữ liệu Bayesian'),
    ('Trí tuệ nhân tạo','Trí tuệ nhân tạo'),
    ('Xử lý ảnh','Xử lý ảnh'),
    ('Cấu trúc dữ liệu và giải thuật','Cấu trúc dữ liệu và giải thuật'),
]
        
    mon_1 = models.CharField('Môn 1', max_length=50, null=True, choices=mon_choices, blank=True)
    mon_1_amount = models.CharField('Học phí', max_length=50, null=True, blank=True, default='0')
    # mon_1_status = models.CharField('Mon_1_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)

    mon_2 = models.CharField('Môn 2', max_length=50, null=True, choices=mon_choices, blank=True)
    mon_2_amount = models.CharField('Học phí', max_length=50, null=True, blank=True, default='0')
    # mon_2_status = models.CharField('Mon_2_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)

    mon_3 = models.CharField('Môn 3', max_length=50, null=True, choices=mon_choices, blank=True)
    mon_3_amount = models.CharField('Học phí', max_length=50, null=True, blank=True, default='0')
    # mon_3_status = models.CharField('Mon_3_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)

    mon_4 = models.CharField('Môn 4', max_length=50, null=True, choices=mon_choices, blank=True)
    mon_4_amount = models.CharField('Học phí', max_length=50, null=True, blank=True, default='0')
    # mon_4_status = models.CharField('Mon_4_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)

    mon_5 = models.CharField('Môn 5', max_length=50, null=True, choices=mon_choices, blank=True)
    mon_5_amount = models.CharField('Học phí', max_length=50, null=True, blank=True, default='0')
    # mon_5_status = models.CharField('Mon_5_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)

    mon_6 = models.CharField('Môn 6', max_length=50, null=True, choices=mon_choices, blank=True)
    mon_6_amount = models.CharField('Học phí', max_length=50, null=True, blank=True, default='0')
    # mon_6_status = models.CharField('Mon_6_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)

    
    # Extra charges
    extra_charges = models.TextField("Khoảng thu khác", null=True, blank=True, default='None')
    extra_charges_amount = models.CharField('Chi phí', max_length=50, default = '0', blank=True)
    # extra_charges_status = models.CharField('Extra_Fee_status', max_length=50, null=True, choices=PaidType.choices, blank=True, default=PaidType.NotPaid)


    # for the total payment and dues
    total_payment = models.CharField('Tổng học phí', max_length=50, null=True, blank=True, default='0')
    total_paid = models.CharField('Tổng học phí đã đóng',max_length=50, null=True, blank=True, default='0')
    dues = models.CharField('Công nợ', max_length=50, null=True, blank=True, default='0')

    template = '{} {} {} {}'
    def __str__(self):
        return self.template.format(self.roll, self.semestertype, self.monsoon_wintertype, self.Year)
    


class EnquiryForm(models.Model):

    BranchType = models.TextChoices('BranchType', 'CS DS SE IT IS')
    EnquiryStatus = models.TextChoices('EnquiryStatus', 'No Yes')

    roll = models.CharField('MSSV', max_length=8, blank=False)
    name = models.CharField('Tên', max_length=250, blank=False)
    email = models.EmailField('Email', max_length=250, blank=False)
    branch = models.CharField('Chuyên ngành', max_length=15, blank=False, choices=BranchType.choices)
    
    Enquiry = models.TextField("Yêu cầu", blank=False)
    Enquiry_status = models.CharField('Trạng thái', max_length=3, null=True, choices=EnquiryStatus.choices, blank=True, default=EnquiryStatus.No)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)

    
    template = '{} {} {}'
    def __str__(self):
        # return self.roll, self.firstname
        return self.template.format(self.roll,self.name,self.email)

class Announcement(models.Model):

    Ann_Status = models.TextChoices('Ann_Status', 'Thường Khẩn')
    Show_Status = models.TextChoices('Show_Status', 'Hiện Ẩn')
    
    Subject = models.CharField('Tiêu đề', max_length=250, blank=False)
    Query = models.TextField('Thông báo', blank=False)
    Status = models.CharField('Trạng thái thông báo', max_length=10, blank=False, choices=Ann_Status.choices, default='Normal')
    Show = models.CharField('Trạng thái hiển thị', max_length=8, blank=False, choices=Show_Status.choices, default='Show')
    datecreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Subject
    


class Automate_Create_Semester(models.Model):
    date = [str(x) for x in range(2017,2050)]
    date=' '.join(date)

    SemesterType = models.TextChoices('SemesterType', 'first second third fourth fifth sixth seventh eighth')
    Monsoon_WinterType = models.TextChoices('Monsoon_WinterType', 'HKI HKII')
    YearType = models.TextChoices('YearType', date)
    BranchType = models.TextChoices('BranchType', 'CS DS SE IT IS')
    CourseType = models.TextChoices('CourseType', 'K15 K16 K17 K18 K19 K20')

    semestertype = models.CharField('Học kì', max_length=50, blank=False, choices=SemesterType.choices)
    monsoon_wintertype = models.CharField('Học kỳ trong năm', max_length=50, blank=False, choices=Monsoon_WinterType.choices)
    Year = models.CharField('Năm nhập học', max_length=50, blank=False, choices=YearType.choices)
    branch = models.CharField('Chuyên ngành', max_length=3, blank=False, choices=BranchType.choices)
    course = models.CharField('Khoá', max_length=8, blank=False, choices=CourseType.choices)
    tution_fee = models.CharField('BHYT', max_length=50, null=True, blank=True, default='0')
    hostel_fee = models.CharField('Phí kí túc xá', max_length=50, null=True, blank=True, default='0')
    datecreated = models.DateTimeField(auto_now_add=True, null=True)

    template = '{} {} {}'
    def __str__(self):
        return self.template.format(self.Year,self.branch,self.course)
    

# saving registered files
class RegisterFile(models.Model):

    Email_Status = models.TextChoices('Email_Status', 'NO YES')

    title = models.CharField('Title', max_length=150, blank=False)
    uploaded_file = models.FileField('Uploaded File', upload_to='uploads/')
    password = models.TextField('Password', blank=False)
    Roll_No = models.TextField('Roll_No', blank=False)
    email = models.TextField('email', blank=False)

    #  fo the satatus whether the email have been send or not
    email_sent = models.CharField('Show', max_length=3, null=True, choices=Email_Status.choices, default='NO')
    datecreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

