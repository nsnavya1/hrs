from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Hotel.models import *
from Administrator.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    if 'uid' in request.session:
        return render(request,"User/HomePage.html")
    else:
        return redirect("Guest:Login")

def my_pro(request):
 if 'uid' in request.session:
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})
 else:
    return redirect("Guest:Login")

def editprofile(request):
    if 'uid' in request.session:
        prodata=tbl_user.objects.get(id=request.session["uid"])
        if request.method=="POST":
            prodata.user_name=request.POST.get('txtname')
            prodata.user_contact=request.POST.get('txtcon')
            prodata.user_email=request.POST.get('txtemail')
            prodata.save()
            return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
        else:
            return render(request,"User/EditProfile.html",{'prodata':prodata})
    else:
        return redirect("Guest:Login")

def changepassword(request):
    if 'uid' in request.session:
        if request.method=="POST":
            ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
            if ccount>0:
                if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                    userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                    userdata.user_password=request.POST.get('txtnewpass')
                    userdata.save()
                    return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
                else:
                    return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return redirect("Guest:Login")
    

def searchhotel(request):
    if 'uid' in request.session:
        spe = tbl_specification.objects.all()
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        district = tbl_district.objects.all()
        data = tbl_newhotel.objects.filter(hotel_vstatus='1')
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        if request.method=="POST":
            place = tbl_place.objects.get(id=request.POST.get('sel_place'))
            rating = request.POST.get("txt_rating")
            filterdata = tbl_newhotel.objects.filter(place=place,hotel_vstatus='1',hotel_ratings=rating)
            return render(request,"User/SearchHotel.html",{"districtdata":district,'data':filterdata,"ar":ar})
        else:
            return render(request,"User/SearchHotel.html",{"districtdata":district,'data':datas,"ar":ar,"spe":spe})
    else:
        return redirect("Guest:Login")
    
def ajaxplace2(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"User/AjaxPlace.html",{"placedata":place})


def ajaxsearchhotel(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    if ((request.GET.get("pid")!="") & (request.GET.get("rate")!="") & (request.GET.get("spe")!="")):
        data = tbl_newhotel.objects.filter(place=tbl_place.objects.get(id=request.GET.get("pid")),hotel_vstatus='1',hotel_ratings=request.GET.get("rate"),hotel_spe=request.GET.get("spe"))
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    elif ((request.GET.get("did")!="") & (request.GET.get("rate")!="") & (request.GET.get("spe")!="")):
        data = tbl_newhotel.objects.filter(place__district=tbl_district.objects.get(id=request.GET.get("did")),hotel_vstatus='1',hotel_ratings=request.GET.get("rate"),hotel_spe=request.GET.get("spe"))
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    elif ((request.GET.get("pid")!="") & (request.GET.get("spe")!="")):
        data = tbl_newhotel.objects.filter(place=tbl_place.objects.get(id=request.GET.get("pid")),hotel_vstatus='1',hotel_spe=request.GET.get("spe"))
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    elif ((request.GET.get("did")!="") & (request.GET.get("spe")!="")):
        data = tbl_newhotel.objects.filter(place__district=tbl_district.objects.get(id=request.GET.get("did")),hotel_vstatus='1',hotel_spe=request.GET.get("spe"))
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    elif ((request.GET.get("rate")!="") & (request.GET.get("spe")!="")):
        data = tbl_newhotel.objects.filter(hotel_ratings=request.GET.get("rate"),hotel_vstatus='1',hotel_spe=request.GET.get("spe"))
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    elif request.GET.get("spe")!="":
        data = tbl_newhotel.objects.filter(hotel_spe=request.GET.get("spe"))
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    elif request.GET.get("pid")!="":
        data = tbl_newhotel.objects.filter(place=tbl_place.objects.get(id=request.GET.get("pid")),hotel_vstatus='1')
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    elif request.GET.get("did")!="":
        data = tbl_newhotel.objects.filter(place__district=tbl_district.objects.get(id=request.GET.get("did")),hotel_vstatus='1')
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})
    else:
        data = tbl_newhotel.objects.filter(hotel_ratings=request.GET.get("rate"),hotel_vstatus='1')
        for i in data:
            tot=0
            ratecount=tbl_rating.objects.filter(hotel=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(hotel=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(data,parry)
        return render(request,"User/Ajax_Search_Hotel.html",{"data":datas,"ar":ar})

def viewmore(request,hid):
 if 'uid' in request.session:
    data=tbl_newhotel.objects.get(id=hid) 
    data1= tbl_specialized.objects.filter(hotel=hid)
    facility = tbl_hotelfacility.objects.filter(hotel=hid)
    roomdetails = tbl_roomdetails.objects.filter(hotel=hid)
    common_fac = tbl_facility.objects.all()
    roomdetails_id = []
    for i in roomdetails:
        roomdetails_id.append(i.id)
    # print(roomdetails_id)
    rm_details = tbl_roomdetails.objects.filter(id__in=roomdetails_id)
    return render(request,"User/HotelDetailViewMore.html",{'data':data,'data1':data1,"id":hid,"facility":facility,"roomdetails":rm_details,"common":common_fac})
 else:
    return redirect("Guest:Login")

def mealpackage(request,hid):
    meal= tbl_mealpackages.objects.filter(hotel=hid)
    return render(request,"User/ViewMealPackage.html",{'data':meal,"hotel":hid})

def tourpackage(request,hid):
    tour= tbl_tourpackages.objects.filter(hotel=hid)
    return render(request,"User/ViewTourPackage.html",{'data':tour,"hotel":hid})

def  vpickanddrop(request,hid):
    pick= tbl_pickanddrophead.objects.filter(hotel=hid)
    return render(request,"User/ViewPickAndDrop.html",{'data':pick,"hotel":hid})

def booking(request,hid):
    roomtype = tbl_roomtype.objects.all()
    floorcount=int(request.session["floor"])
    floorlist=[ i for i in range(0,floorcount)]
    request.session["hotels"]=hid
    tourpackages = tbl_tourpackages.objects.filter(hotel=hid)
    mealpackages = tbl_mealpackages.objects.filter(hotel=hid)
    pickanddrophead = tbl_pickanddrophead.objects.filter(hotel=hid)
    book= tbl_booking.objects.filter(hotel=hid)
    if request.method=="POST":
        roomtypes = request.POST.get("sel_roomtype")
        floor = request.POST.get("txtfloor")
        roomcount = tbl_roomdetails.objects.get(roomtype=roomtypes,roomdetails_floor=floor,hotel=hid)
        rmcount = roomcount.roomdetails_count
        bkcount = tbl_booking.objects.filter(roomtype=roomtypes,booking_floor=floor,hotel=hid,booking_status=0,booking_checkin=request.POST.get('txtcheckin'),booking_checkout=request.POST.get('txtcheckout')).count()
        if int(rmcount) <= bkcount:
            return render(request,"User/Booking.html",{"msg1":"Your Suggested Room in the Floor is Already Booked..","hid":hid})
        else:
            checkin=request.POST.get('txtcheckin')
            checkout=request.POST.get('txtcheckout')
            noofguest=request.POST.get('txtguest')
            
            roomtype = tbl_roomtype.objects.get(id=request.POST.get('sel_roomtype'))
            floornumber = request.POST.get('txtfloor')
            
            userid=tbl_user.objects.get(id=request.session["uid"])
            hotelid=tbl_newhotel.objects.get(id=hid)
            
            
            mealpackages = tbl_mealpackages.objects.get(id=request.POST.get('sel_mealpackages'))
            tourpackages = tbl_tourpackages.objects.get(id=request.POST.get('sel_tourpackages'))
            pickanddrophead = tbl_pickanddrophead.objects.get(id=request.POST.get('sel_pickanddrophead'))
            sumofcount=0
            roomdata=tbl_roomdetails.objects.filter(hotel=hotelid,roomtype=roomtype,roomdetails_floor=floornumber)
            for i in roomdata:
                sumofcount=sumofcount+int(i.roomdetails_occupancy)
            # print(sumofcount)
            if(int(noofguest)<=sumofcount):           
                tbl_booking.objects.create(booking_checkin=checkin,
                                       booking_checkout=checkout,
                                       booking_noofguest=noofguest,
                                       booking_floor=floornumber,
                                       hotel=hotelid,
                                       roomtype=tbl_roomtype.objects.get(id=request.POST.get('sel_roomtype')),
                                       user=userid,
                                       mealpackages=mealpackages,
                                       tourpackages=tourpackages,
                                       pickanddrophead=pickanddrophead)
                return render(request,"User/Booking.html",{"msg":"Sucessfully Booked.."})
            else:
                return render(request,"User/Booking.html",{"msg":"Due to More No of Guests its Not Booked "})
    else:
       return render(request,"User/Booking.html",{'data':book,"hotel":hid,"mealpackagesdata":mealpackages,"tourpackagesdata":tourpackages,"pickanddropheaddata":pickanddrophead,"roomtypedata":roomtype,"floornumberdata":floorlist})

def mybooking(request):
    if 'uid' in request.session:
        booking = tbl_booking.objects.filter(user=request.session["uid"])
        return render(request,"User/My_booking.html",{"data":booking})
    else:
        return redirect("Guest:Login")

def occupants(request,id):
    bk = tbl_booking.objects.get(id=id)
    oc = tbl_occupants.objects.filter(booking=id).count()
    if request.method=="POST":
        # print(bk.booking_noofguest)
        # print(oc)
        if int(bk.booking_noofguest) <= oc:
            return render(request,"User/Occupants.html",{"msg":"Limite Exede"})
        else:

            username=request.POST.get("txtname")
            userdob=request.POST.get("txtdate")
            usergender=request.POST.get("gender")
            usercontact=request.POST.get("txtcontact")
            userproof=request.FILES.get("fileProof")
            useraadhar=request.POST.get("txtaadhar")
            ladarn=request.POST.get("txtaadhar").lower()
            laname=request.POST.get("txtname").lower()
            aadharcheck = tbl_aadhar.objects.all()
            flag=0
            for i in aadharcheck:
                ldnumber=i.aadhar_number.lower()
                upnumber=i.aadhar_number.upper()
                uldnumber=request.POST.get("txtaadhar").lower()
                uudnumber=request.POST.get("txtaadhar").upper()
                ldname=i.aadhar_name.lower()
                upname=i.aadhar_name.upper()
                uldname=request.POST.get("txtname").lower()
                uudname=request.POST.get("txtname").upper()
                if((ldnumber==uldnumber or upnumber==uudnumber)  and  (ldname==uldname or upname==uudname)):
                    flag=1
                    break
            if(flag==1):
                 tbl_occupants.objects.create(occupants_name=username,occupants_dob=userdob,occupants_gender=usergender,occupants_contact=usercontact,occupants_proof=userproof,occupants_aadhar=useraadhar,booking=tbl_booking.objects.get(id=id))
                 return redirect("User:occupants",id)
            else:
                return render(request,"USER/Occupants.html",{"msg":"Invalid"})
    else:
        return render(request,"User/Occupants.html")
    

def complaint(request):
    if 'uid' in request.session:
        data=tbl_user.objects.get(id=request.session["uid"])

        if request.method=="POST":
            complainttitle=request.POST.get("txttitle")
            complaintdescription=request.POST.get("txtcomplaint")
            
            tbl_complaint.objects.create(complaint_title=complainttitle,complaint_description=complaintdescription,user=tbl_user.objects.get(id=request.session['uid']))
            return redirect("User:complaint")
        else:
            return render(request,"User/Complaints.html",{"data":data})   
    else:
        return redirect("Guest:Login")
    
def mycomplaints(request):
    if 'uid' in request.session:
        data=tbl_user.objects.get(id=request.session["uid"])
        complaint=tbl_complaint.objects.filter(user=data)
        return render(request,"User/Mycomplaints.html",{"complaint":complaint})
    else:
        return redirect("Guest:Login")  

def logout(request):
    del request.session['uid']
    return redirect("Guest:Login")

def ajaxroomtype(request):
    hoteldata=tbl_newhotel.objects.get(id=request.session["hotels"])
    floordata=request.GET.get('did')
    srooms=tbl_roomdetails.objects.filter(hotel=hoteldata,roomdetails_floor=floordata)
    parray=[]
    for i in srooms:
        parray.append(i.roomtype.id)
    stype=tbl_roomtype.objects.filter(id__in=parray)
    return render(request,"User/AjaxRoomtype.html",{'stype':stype})

def payment(request,bid):
    data=tbl_booking.objects.get(id=bid)
    email = data.user.user_email
    if request.method=="POST":
        data.booking_status=3
        data.save()
        send_mail(
                            'Respected Sir/Madam ',#subject
                            "\rYour order was cancelled becacuse of"
                            "\r1, You didn't collect the product from the outlet within 24 hours. "
                            "\r2, if it is online payment, your amount will be refunded within two or three days."
                            "\r By"
                            "\r D MARKET" ,#body
                            settings.EMAIL_HOST_USER,
                            [email],
                        )
        return redirect("User:homepage")
    else:
        return render(request,"User/Payment.html",{'data':data})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(hotel=wdata.hotel_id).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(hotel=wdata.hotel_id).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_booking.objects.get(id=workid)
    tbl_rating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,hotel=tbl_newhotel.objects.get(id=wdata.hotel_id))
    stardata=tbl_rating.objects.filter(hotel=wdata.hotel_id).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(hotel=cdata.hotel_id)
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        r_len = r_len + int(i.rating_data)
    rlen = r_len // 5
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":rlen}
    return JsonResponse(result)

def ViewRooms(request,id):
    rm = tbl_room_description.objects.filter(room=id)
    return render(request,"User/View_Rooms_Details.html",{"data":rm})

def cancelbooking(request,id):
    bk = tbl_booking.objects.get(id=id)
    bk.booking_status = 6
    bk.save()
    email = bk.user.user_email
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rYour Booking is cancelled"
        # "\r1, You didn't collect the product from the outlet within 24 hours. "
        "\r2, The amount will be refunded within two or three days."
        "\r By"
        "\r HIROTO" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return redirect("User:mybooking")