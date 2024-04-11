from django.db import models
from Administrator.models import *
# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_doj=models.DateField(auto_now_add=True)
    user_dob=models.DateField()
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_aadhar=models.CharField(max_length=50)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_address=models.CharField(max_length=50)
    user_status = models.IntegerField(default="0")
    
class tbl_newhotel(models.Model):
    hotel_name=models.CharField(max_length=50)
    hotel_ratings=models.CharField(max_length=50)
    hotel_contact=models.CharField(max_length=50)
    hotel_email=models.CharField(max_length=50)
    hotel_pass=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    hotel_addr=models.CharField(max_length=50)
    hotel_vstatus= models.IntegerField(default="0")
    hotel_photo = models.FileField(upload_to='Assets/HotelPhoto/')
    hotel_proof = models.FileField(upload_to='Assets/HotelProof/')                           
    hotel_license=models.CharField(max_length=50)                            
    hotel_floor=models.CharField(max_length=50,null=True)
    hotel_doj=models.DateField(auto_now_add=True)
    hotel_url = models.CharField(max_length=150,null=True)
    #speci = models.ForeignKey(tbl_specification,on_delete=models.SET_NULL,null=True)
    hotel_spe = models.ForeignKey(tbl_specification,on_delete=models.SET_NULL,null=True)
    
class tbl_floor(models.Model):
    floor_count=models.CharField(max_length=50)
    hotel = models.ForeignKey(tbl_newhotel, on_delete=models.CASCADE)
   