from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)

class tbl_roomtype(models.Model):
    roomtype_type=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

class tbl_dept(models.Model):
    dept_name=models.CharField(max_length=50)

class tbl_desig(models.Model):
    desig_name=models.CharField(max_length=50)

class tbl_employee(models.Model):
    emp_name=models.CharField(max_length=50)
    dept =models.ForeignKey(tbl_dept, on_delete=models.CASCADE)
    desig =models.ForeignKey(tbl_desig, on_delete=models.CASCADE)
    emp_salary=models.CharField(max_length=50)
    emp_contact=models.CharField(max_length=50)
    emp_address=models.CharField(max_length=50)

class tbl_specification(models.Model):
    speci_name=models.CharField(max_length=50)

class tbl_facility(models.Model):
    facility_name=models.CharField(max_length=50)

class tbl_aadhar(models.Model):
    aadhar_name=models.CharField(max_length=50)
    aadhar_number=models.CharField(max_length=50)