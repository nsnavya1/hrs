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
    dataall=tbl_roomdetails.objects.all() 
    #data=tbl_roomdetails.objects.get(id=request.session["hid"])
    if request.method=="POST":
        roomfloor=request.POST.get('txtfloor')
        roomcount=request.POST.get('txtcount')
        roomdis = tbl_roomtype.objects.get(id=request.POST.get('sel_roomtype'))
        roomdata=tbl_newhotel.objects.get(id=request.session["hid"])
        roomamount=request.POST.get('txtamount')
        roomoccupancy=request.POST.get('txtoccupancy')
        tbl_roomdetails.objects.create(roomdetails_floor=roomfloor,roomdetails_count=roomcount,roomtype=roomdis,hotel=roomdata,roomdetails_amount=roomamount,roomdetails_occupancy=roomoccupancy)
        return redirect("Hotel:roomInsertSelect")
    else:
        return render(request,"Hotel/RoomDetails.html",{'dataall':dataall,"roomtypedata":roomtype})

'''def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Hotel:roomInsertSelect")

def placeupdate(request,eid):
    room = tbl_roomtype.objects.all()
    editdata=tbl_roomDetails.objects.get(id=eid)
    if request.method=="POST":
        editdata.room_floor=request.POST.get('txtfloor')
        editdata.room_count=request.POST.get('txtcount')
        roomdis = tbl_roomtype.objects.get(id=request.POST.get('sel_room'))
        editdata.room = roomdis
        editdata.room_amount=request.POST.get('txtamount')
        editdata.room_occupancy=request.POST.get('txtoccupancy')   
        
        editdata.save()
        return redirect("Hotel:roomInsertSelect")
    else:
        return render(request,"Hotel\RoomDetails.html",{"editdata":editdata,"districtdata":district})'''
