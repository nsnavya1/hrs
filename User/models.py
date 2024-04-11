from django.db import models
from Administrator.models import *
from Guest.models import *
from Hotel.models import *

# Create your models here.

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_checkin=models.DateField()
    booking_checkout=models.DateField()
    booking_noofguest=models.CharField(max_length=50)
    booking_amount=models.IntegerField(default="0")
    booking_status=models.IntegerField(default="0")
    booking_floor=models.CharField(max_length=50)
    roomtype =models.ForeignKey(tbl_roomtype, on_delete=models.CASCADE)
    user =models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    hotel =models.ForeignKey(tbl_newhotel,on_delete=models.CASCADE)
    tourpackages =models.ForeignKey(tbl_tourpackages, on_delete=models.SET_NULL,null=True)
    mealpackages =models.ForeignKey(tbl_mealpackages, on_delete=models.SET_NULL,null=True)
    pickanddrophead =models.ForeignKey(tbl_pickanddrophead, on_delete=models.SET_NULL,null=True)
   
class tbl_occupants(models.Model):
    occupants_name=models.CharField(max_length=50)
    occupants_dob=models.DateField()
    occupants_gender=models.CharField(max_length=50)
    occupants_contact=models.CharField(max_length=50)
    occupants_proof = models.FileField(upload_to='Assets/OccupantsProof/')
    occupants_aadhar=models.CharField(max_length=50)
    booking =models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    
    
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_description=models.CharField(max_length=200)
    complaint_reply=models.CharField(max_length=200)
    complaint_status = models.IntegerField(default="0")
    complaint_date=models.DateField(auto_now_add=True)
    user =models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    hotel =models.ForeignKey(tbl_newhotel,on_delete=models.CASCADE,null=True)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    hotel=models.ForeignKey(tbl_newhotel,on_delete=models.SET_NULL,null=True)
    datetime=models.DateTimeField(auto_now_add=True)