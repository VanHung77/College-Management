# Generated by Django 3.1.5 on 2021-04-05 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=250, verbose_name='Subject')),
                ('Query', models.TextField(verbose_name='Query')),
                ('Status', models.CharField(choices=[('Normal', 'Normal'), ('Urgent', 'Urgent')], default='Normal', max_length=10, verbose_name='Status')),
                ('Show', models.CharField(choices=[('Show', 'Show'), ('Remove', 'Remove')], default='Show', max_length=7, verbose_name='Show')),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Automate_Create_Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestertype', models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eighth', 'Eighth')], max_length=50, verbose_name='Semester_type')),
                ('monsoon_wintertype', models.CharField(choices=[('Monsoon', 'Monsoon'), ('Winter', 'Winter')], max_length=50, verbose_name='Monsoon_or_Winter')),
                ('Year', models.CharField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040'), ('2041', '2041'), ('2042', '2042'), ('2043', '2043'), ('2044', '2044'), ('2045', '2045'), ('2046', '2046'), ('2047', '2047'), ('2048', '2048'), ('2049', '2049')], max_length=50, verbose_name='College Joining Year')),
                ('branch', models.CharField(choices=[('CSE', 'Cse'), ('ECE', 'Ece')], max_length=3, verbose_name='Branch')),
                ('course', models.CharField(choices=[('B_Tech', 'B Tech'), ('M_Tech', 'M Tech'), ('Phd', 'Phd')], max_length=7, verbose_name='Course')),
                ('tution_fee', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Tution_Fee')),
                ('hostel_fee', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Hostel_Fee')),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=7, verbose_name='Roll_No')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('branch', models.CharField(choices=[('CSE', 'Cse'), ('ECE', 'Ece')], max_length=3, verbose_name='Branch')),
                ('Enquiry', models.TextField(verbose_name='Enquiry')),
                ('Enquiry_status', models.CharField(blank=True, choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, null=True, verbose_name='Enquiry_status')),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('uploaded_file', models.FileField(upload_to='uploads/', verbose_name='Uploaded File')),
                ('password', models.TextField(verbose_name='Password')),
                ('roll_no', models.TextField(verbose_name='Roll_No')),
                ('email', models.TextField(verbose_name='email')),
                ('email_sent', models.CharField(choices=[('NO', 'No'), ('YES', 'Yes')], default='NO', max_length=3, null=True, verbose_name='Show')),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='Roll_No')),
                ('firstname', models.CharField(max_length=250, verbose_name='First_Name')),
                ('middlename', models.CharField(blank=True, max_length=250, null=True, verbose_name='Middle_Name')),
                ('lastname', models.CharField(blank=True, max_length=250, null=True, verbose_name='Last_Name')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('branch', models.CharField(choices=[('CSE', 'Cse'), ('ECE', 'Ece')], max_length=3, verbose_name='Branch')),
                ('Year', models.CharField(choices=[('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040'), ('2041', '2041'), ('2042', '2042'), ('2043', '2043'), ('2044', '2044'), ('2045', '2045'), ('2046', '2046'), ('2047', '2047'), ('2048', '2048'), ('2049', '2049')], max_length=4, verbose_name='Year')),
                ('course', models.CharField(choices=[('B_Tech', 'B Tech'), ('M_Tech', 'M Tech'), ('Phd', 'Phd')], max_length=7, verbose_name='Course')),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestertype', models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eighth', 'Eighth')], max_length=50, verbose_name='Semester_type')),
                ('monsoon_wintertype', models.CharField(choices=[('Monsoon', 'Monsoon'), ('Winter', 'Winter')], max_length=50, verbose_name='Monsoon_or_Winter')),
                ('Year', models.CharField(choices=[('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040'), ('2041', '2041'), ('2042', '2042'), ('2043', '2043'), ('2044', '2044'), ('2045', '2045'), ('2046', '2046'), ('2047', '2047'), ('2048', '2048'), ('2049', '2049')], max_length=50, verbose_name='Year')),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('tution_fee', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Tution_Fee')),
                ('hostel_fee', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Hostel_Fee')),
                ('mon_1', models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=50, null=True, verbose_name='Mon_1')),
                ('mon_1_amount', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Mon_1_amount')),
                ('mon_2', models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=50, null=True, verbose_name='Mon_2')),
                ('mon_2_amount', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Mon_2_amount')),
                ('mon_3', models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=50, null=True, verbose_name='Mon_3')),
                ('mon_3_amount', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Mon_3_amount')),
                ('mon_4', models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=50, null=True, verbose_name='Mon_4')),
                ('mon_4_amount', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Mon_4_amount')),
                ('mon_5', models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=50, null=True, verbose_name='Mon_5')),
                ('mon_5_amount', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Mon_5_amount')),
                ('mon_6', models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=50, null=True, verbose_name='Mon_6')),
                ('mon_6_amount', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Mon_6_amount')),
                ('extra_charges', models.TextField(blank=True, default='None', null=True, verbose_name='Extra Charges')),
                ('extra_charges_amount', models.CharField(blank=True, default='0', max_length=50, verbose_name='Extra Charge Amount')),
                ('total_payment', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Total Payment')),
                ('total_paid', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Total paid')),
                ('dues', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Dues')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.student')),
            ],
        ),
    ]