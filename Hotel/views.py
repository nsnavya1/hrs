from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from Hotel.models import *
from User.models import *
import random
from django.conf import settings
from django.core.mail import send_mail
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
    
    floorcount=int(request.session["floor"])
    data=tbl_roomdetails.objects.filter(hotel=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    floorlist=[ i for i in range(0,floorcount)]
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        
        roomcount=request.POST.get('txtcount')
        roomtype = tbl_roomtype.objects.get(id=request.POST.get('sel_roomtype'))
        floornumber = request.POST.get('txtfloor')
        roomamount=request.POST.get('txtamount')
        roomoccupancy=request.POST.get('txtoccupancy')
        tbl_roomdetails.objects.create(roomdetails_floor=floornumber,roomdetails_count=roomcount,roomtype=roomtype,hotel=hotelid,roomdetails_amount=roomamount,roomdetails_occupancy=roomoccupancy)
        return redirect("Hotel:roomInsertSelect")
    else:
        return render(request,"Hotel/RoomDetails.html",{'data':data,"roomtypedata":roomtype,"floornumberdata":floorlist})

def delRoomDetails(request,did):
    tbl_roomdetails.objects.get(id=did).delete()
    return redirect("Hotel:roomInsertSelect")


def HotelFacilitiesInsertSelect(request):
    data=tbl_hotelfacility.objects.filter(hotel=request.session["hid"])
    # facilityid=tbl_facility.objects.get(id=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        # facilityid=tbl_facility.objects.get(id=request.session["hid"])
        facilityname=request.POST.get('txtfacility')
        tbl_hotelfacility.objects.create(hotelfacility_name=facilityname,hotel=hotelid)
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


def pickanddropinsertselect(request):
    data=tbl_pickanddrophead.objects.filter(hotel=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        pickanddropheadname=request.POST.get('txtname')
        pickanddropheadamount=request.POST.get('txtamount')
        tbl_pickanddrophead.objects.create(pickanddrophead_name=pickanddropheadname,pickanddrophead_amount=pickanddropheadamount,hotel=hotelid)
        return redirect("Hotel:pickanddropinsertselect")
    else:
        return render(request,"Hotel/PickAndDropHead.html",{'data':data})

def delpickanddrop(request,did):
    tbl_pickanddrophead.objects.get(id=did).delete()
    return redirect("Hotel:pickanddropinsertselect")


def floorinsertselect(request):
    data=tbl_floor.objects.filter(hotel=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        floorno=request.POST.get('txtfloor')
        tbl_floor.objects.create(floor_no=floorno,hotel=hotelid)
        return redirect("Hotel:floorinsertselect")
    else:
        return render(request,"Hotel/Floor.html",{'data':data})


def delfloor(request,did):
    tbl_floor.objects.get(id=did).delete()
    return redirect("Hotel:floorinsertselect")


def updfloor(request,eid):
    editdata=tbl_floor.objects.get(id=eid)
    if request.method=="POST":
        editdata.floor_no=request.POST.get("txtfloor")
        editdata.save()
        return redirect("Hotel:floorinsertselect")
    else:
        return render(request,"Hotel/Floor.html",{"editdata":editdata})
    

def specializedInsertSelect(request):
    speciname = tbl_specification.objects.all()
    data=tbl_specialized.objects.filter(hotel=request.session["hid"])
    hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
    if request.method=="POST":
        hotelid=tbl_newhotel.objects.get(id=request.session["hid"])
        speciname = tbl_specification.objects.get(id=request.POST.get('sel_speci'))
        tbl_specialized.objects.create(speci=speciname,hotel=hotelid)
        return redirect("Hotel:specializedInsertSelect")
    else:
        return render(request,"Hotel/Specialized.html",{'data':data,"specidata":speciname})

def delspecialized(request,did):
    tbl_specialized.objects.get(id=did).delete()
    return redirect("Hotel:specializedInsertSelect")

def userbooking(request):
    booking = tbl_booking.objects.filter(hotel=request.session["hid"])
    return render(request,"Hotel/UserBooking.html",{"data":booking})

def acceptbooking(request,aid):
    data=tbl_booking.objects.get(id=aid)
    meal=tbl_mealpackages.objects.get(id=data.mealpackages.id)
    pickup=tbl_pickanddrophead.objects.get(id=data.pickanddrophead.id)
    tour=tbl_tourpackages.objects.get(id=data.tourpackages.id)
    rtpe=tbl_roomtype.objects.get(id=data.roomtype.id)
    hotelid=tbl_newhotel.objects.get(id=data.hotel.id)

    rom=tbl_roomdetails.objects.filter(roomtype=rtpe,hotel=hotelid).last()
    
    amounts=int(meal.mealpackages_amount)+int(pickup.pickanddrophead_amount)+int(tour.tourpackages_amount)+int(rom.roomdetails_amount)
    data.booking_amount=amounts
    data.booking_status=1
    data.save()
    return redirect("Hotel:userbooking")
def rejectbooking(request,rid):
    data=tbl_booking.objects.get(id=rid)
    data.booking_status=2
    data.save()
    return redirect("Hotel:userbooking")

def sentconfirmation(request,id):
    booking = tbl_booking.objects.get(id=id)
    user = booking.user.user_name
    user_email = booking.user.user_email
    checkin = booking.booking_checkin
    checkout = booking.booking_checkout
    nfg = booking.booking_noofguest
    amount = booking.booking_amount
    mealpack = booking.mealpackages.mealpackages_name
    tourpack = booking.tourpackages.tourpackages_name
    pickpack = booking.pickanddrophead.pickanddrophead_name
    room = booking.roomtype.roomtype_type
    hotal_name = booking.hotel.hotel_name
    hotal_contact = booking.hotel.hotel_contact
    hotal_email = booking.hotel.hotel_email
    hotal_address = booking.hotel.hotel_addr
    hotel_url = booking.hotel.hotel_url
    bkno = random.randint(111111,999999)
    print(user_email)
    if pickpack:
        send_mail(
            f"Dear {user}",  # Subject
            (f"We are delighted to confirm your upcoming stay with us at {hotal_name}! Your adventure begins here.\r\n"
            "Below you will find all the important details of your reservation.\r\n"
            "Please review them to ensure everything is as per your plans:\r\n"
            "Reservation Details:\r\n"
            f"Guest Name: {user}\r\n"
            f"Check-in Date: {checkin}\r\n"
            f"Check-out Date: {checkout}\r\n"
            f"Number of Guests: {nfg}\r\n"
            f"Room Type: {room}\r\n"
            f"Meal Package: {mealpack}\r\n"
            f"Tour Package: {tourpack}\r\n"
            f"Total Amount: {amount}\r\n"
            f"Booking Number: {bkno}\r\n"
            "Please use this number in any communication with us regarding your stay.\r\n"
            "For Pick ups Contact\r\n"
            "Driver: Anoop\r\n"
            "Phone: 9876543210\r\n\n"
            "Warmest regards\r\n"
            f"Location : {hotel_url}\r\n"
            f"By\r\n{hotal_name}\r\n{hotal_address}\r\n{hotal_contact}\r\n{hotal_email}"),
            settings.EMAIL_HOST_USER,
            [user_email],
        )
    else:
        send_mail(
            f"Dear {user}",  # Subject
            (f"We are delighted to confirm your upcoming stay with us at {hotal_name}! Your adventure begins here.\r\n"
            "Below you will find all the important details of your reservation.\r\n"
            "Please review them to ensure everything is as per your plans:\r\n"
            "Reservation Details:\r\n"
            f"Guest Name: {user}\r\n"
            f"Check-in Date: {checkin}\r\n"
            f"Check-out Date: {checkout}\r\n"
            f"Number of Guests: {nfg}\r\n"
            f"Room Type: {room}\r\n"
            f"Meal Package: {mealpack}\r\n"
            f"Tour Package: {tourpack}\r\n"
            f"Total Amount: {amount}\r\n"
            f"Booking Number: {bkno}\r\n"
            "Please use this number in any communication with us regarding your stay.\r\n"
            "Warmest regards\r\n"
            f"By\r\n{hotal_name}\r\n{hotal_address}\r\n{hotal_contact}\r\n{hotal_email}"),
            settings.EMAIL_HOST_USER,
            [user_email],
        )
    booking.booking_status = 4
    booking.save()
    return redirect("Hotel:userbooking")

def adddetails(request,id):
    rm = tbl_room_description.objects.filter(room=id)
    if request.method == "POST":
        tbl_room_description.objects.create(room_photo=request.FILES.get("txtphoto"),room_desc=request.POST.get("txt_desc"),room=tbl_roomdetails.objects.get(id=id))
        return redirect("Hotel:roomInsertSelect")
    else:
        return render(request,"Hotel/Add_Room_Details.html",{"data":rm})
    
def complaint(request):

    if request.method=="POST":
        complainttitle=request.POST.get("txttitle")
        complaintdescription=request.POST.get("txtcomplaint")
        
        tbl_complaint.objects.create(complaint_title=complainttitle,complaint_description=complaintdescription,hotel=tbl_newhotel.objects.get(id=request.session["hid"]))
        return redirect("Hotel:complaint")
    else:
         return render(request,"Hotel/Complaints.html")  
    
def mycomplaints(request):
    complaint=tbl_complaint.objects.filter(hotel=request.session["hid"])
    return render(request,"Hotel/Mycomplaints.html",{"complaint":complaint}) 

def logout(request):
    del request.session['hid']
    return redirect("Guest:Login")