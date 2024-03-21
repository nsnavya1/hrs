from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from Hotel.models import *
# Create your views here.
def homepages(request):
    return render(request,"Hotel/HomePage.html")

def my_pros(request):
    data=tbl_newhotel.objects.get(id=request.session["hid"])
    return render(request,"Hotel/MyProfile.html",{'data':data})

def editprofiles(request):
    prodata=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        prodata.hotel_name=request.POST.get('txtname')
        prodata.hotel_contact=request.POST.get('txtcon')
        prodata.hotel_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Hotel/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Hotel/EditProfile.html",{'prodata':prodata})

def changepasswords(request):
    if request.method=="POST":
        ccount=tbl_newhotel.objects.filter(id=request.session["hid"],hotel_pass=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                hoteldata=tbl_newhotel.objects.get(id=request.session["hid"],hotel_pass=request.POST.get('txtcurpass'))
                hoteldata.hotel_pass=request.POST.get('txtnewpass')
                hoteldata.save()
                return render(request,"Hotel/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Hotel/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Hotel/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Hotel/ChangePassword.html")
    




def roomInsertSelect(request):
    roomtype = tbl_roomtype.objects.all()
    data=tbl_roomdetails.objects.filter(hotel=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        roomfloor=request.POST.get('txtfloor')
        roomcount=request.POST.get('txtcount')
        roomtype = tbl_roomtype.objects.get(id=request.POST.get('sel_roomtype'))
        roomamount=request.POST.get('txtamount')
        roomoccupancy=request.POST.get('txtoccupancy')
        tbl_roomdetails.objects.create(roomdetails_floor=roomfloor,roomdetails_count=roomcount,roomtype=roomtype,hotel=hotelid,roomdetails_amount=roomamount,roomdetails_occupancy=roomoccupancy)
        return redirect("Hotel:roomInsertSelect")
    else:
        return render(request,"Hotel/RoomDetails.html",{'data':data,"roomtypedata":roomtype})

def delRoomDetails(request,did):
    tbl_roomdetails.objects.get(id=did).delete()
    return redirect("Hotel:roomInsertSelect")


def HotelFacilitiesInsertSelect(request):
    data=tbl_hotelfacility.objects.filter(hotel=request.session["hid"])
    facilityid=tbl_facility.objects.get(id=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        facilityid=tbl_facility.objects.get(id=request.session["hid"])
        facilityname=request.POST.get('txtfacility')
        tbl_hotelfacility.objects.create(hotelfacility_name=facilityname,facility=facilityid,hotel=hotelid)
        return redirect("Hotel:HotelFacilitiesInsertSelect")
    else:
        return render(request,"Hotel/HotelFacilities.html",{'data':data})

def delHotelFacilities(request,did):
    tbl_hotelfacility.objects.get(id=did).delete()
    return redirect("Hotel:HotelFacilitiesInsertSelect")


def MealPackagesInsertSelect(request):
    data=tbl_mealpackages.objects.filter(hotel=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        mealpackagename=request.POST.get('txtname')
        mealpackagedesc=request.POST.get('txtdesc')
        mealpackageamount=request.POST.get('txtamount')
        tbl_mealpackages.objects.create(mealpackages_name=mealpackagename,mealpackages_description=mealpackagedesc,mealpackages_amount=mealpackageamount,hotel=hotelid)
        return redirect("Hotel:MealPackagesInsertSelect")
    else:
        return render(request,"Hotel/MealPackages.html",{'data':data})

def delMealPackages(request,did):
    tbl_mealpackages.objects.get(id=did).delete()
    return redirect("Hotel:MealPackagesInsertSelect")

def TourPackagesInsertSelect(request):
    data=tbl_tourpackages.objects.filter(hotel=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        tourpackagename=request.POST.get('txtname')
        tourpackagedesc=request.POST.get('txtdesc')
        tourpackageamount=request.POST.get('txtamount')
        tbl_tourpackages.objects.create(tourpackages_name=tourpackagename,tourpackages_description=tourpackagedesc,tourpackages_amount=tourpackageamount,hotel=hotelid)
        return redirect("Hotel:TourPackagesInsertSelect")
    else:
        return render(request,"Hotel/TourPackages.html",{'data':data})

def delTourPackages(request,did):
    tbl_tourpackages.objects.get(id=did).delete()
    return redirect("Hotel:TourPackagesInsertSelect")

