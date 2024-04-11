from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from User.models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def LoadingHomePage(request):
    return render(request,"Administrator/HomePage.html")


def add(request):
    return render(request,"Administrator/Add.html")
def add2(request):
     #sum = 0
     if request.method=="POST":
        FirstNumber= int(request.POST.get('num_FirstValue'))
        SecondNumber=int(request.POST.get('num_SecondValue'))
        #btn=request.POST.get('btnAdd')
        #print(btn)
        sum= SecondNumber + FirstNumber
       
        return render(request,"Administrator/add2.html",{'sum':sum})
     else:
        return render(request,"Administrator/add2.html")

def greater(request):
    largest = 0
    if request.method=="POST":
        FirstNumber= int(request.POST.get('num_FirstValue'))
        SecondNumber=int(request.POST.get('num_SecondValue'))
        ThirdNumber=int(request.POST.get('num_ThirdValue'))
        if FirstNumber > SecondNumber and FirstNumber > ThirdNumber:
            largest = FirstNumber
        elif SecondNumber > FirstNumber and SecondNumber > ThirdNumber:
            largest = SecondNumber
        else:
            largest=ThirdNumber
        

        return render(request,"Administrator/Greater.html",{'largest':largest})
    else: 
        return render(request,"Administrator/Greater.html")
    
def calculator(request):
     #sum = 0
     if request.method=="POST":
        FirstNumber= int(request.POST.get('num_FirstValue'))
        SecondNumber=int(request.POST.get('num_SecondValue'))
        btn=request.POST.get('btnAdd')
        if btn=="Add":
            result=FirstNumber + SecondNumber
        elif btn=="Sub":
            result=FirstNumber - SecondNumber
        elif btn=="Multi":
            result=FirstNumber * SecondNumber
        else:
            result=FirstNumber / SecondNumber
        return render(request,"Administrator/Calculator.html",{'result':result})
     else:
        return render(request,"Administrator/Calculator.html")
     
def personal(request):
    if request.method=="POST":
        name=""
        Fname= request.POST.get('txtfname')
        Lname=request.POST.get('txtlname')
        bgender=request.POST.get('gender')
        bmartial=request.POST.get('mar')
        print(Fname)
        print(Lname)
        print(bgender)
        print(bmartial)
        if bgender=="Male":
                name="Mr "+Fname+" "+Lname
                
        elif bgender=="Female" and bmartial=="Single":
                name="Ms "+Fname+" "+Lname
        elif bgender=="Female" and bmartial=="Married":
                name="Mrs "+Fname+" "+Lname
        return render(request,"Administrator/Personal.html",{'name':name})
       
    else:
        return render(request,"Administrator/Personal.html")


def salary(request):
    if request.method=="POST":
        name=""
        TA=DA=HRA=LIC=PF=DEDUCTION=NET=0
        Fname= request.POST.get('txtfname')
        Lname=request.POST.get('txtlname')
        bgender=request.POST.get('gender')
        bmartial=request.POST.get('mar')
        bdept=request.POST.get('dept')
        bsal=int(request.POST.get('numsalary'))
        if bgender=="Male":
                name="Mr "+Fname+" "+Lname
                
        elif bgender=="Female" and bmartial=="Single":
                name="Ms "+Fname+" "+Lname
        elif bgender=="Female" and bmartial=="Married":
                name="Mrs "+Fname+" "+Lname
        
        if(bsal>=10000):
             TA=0.4*bsal
             DA=0.35*bsal
             HRA=0.3*bsal
             LIC=0.25*bsal
             PF=0.2*bsal
        elif(bsal>=5000):
             TA=0.35*bsal
             DA=0.3*bsal
             HRA=0.25*bsal
             LIC=0.2*bsal
             PF=0.15*bsal
        else:
             TA=0.3*bsal
             DA=0.25*bsal
             HRA=0.2*bsal
             LIC=0.15*bsal
             PF=0.1*bsal
        DEDUCTION=LIC+PF
        NET=bsal+TA+DA+HRA-(LIC+PF)


        return render(request,"Administrator/Salary.html",{'name':name,'bgender':bgender,'bmartial':bmartial,'bdept':bdept,'bsal':bsal,'TA':TA,'DA':DA,'HRA':HRA,'LIC':LIC,'PF':PF,'DEDUCTION':DEDUCTION,'NET':NET})
       
    else:
        return render(request,"Administrator/Salary.html")
    

def districtInsertSelect(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtdistirct')
        tbl_district.objects.create(district_name=disName)
        return redirect("Administrator:districtInsertSelect")
    else:
        return render(request,"Administrator/District.html",{'data':data})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Administrator:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtdistirct")
        editdata.save()
        return redirect("Administrator:districtInsertSelect")
    else:
        return render(request,"Administrator\District.html",{"editdata":editdata})


def admindetails(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        adminName=request.POST.get('txtname')
        adminContact=request.POST.get('txtcontact')
        adminEmail=request.POST.get('txtemail')
        adminPassword=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=adminName,admin_contact=adminContact,admin_email=adminEmail,admin_password=adminPassword)
        return redirect("Administrator:admindetails")
    else:
        return render(request,"Administrator/AdminRegistration.html",{'data':data})
    
def deladmindetails(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("Administrator:admindetails")


def updadmindetails(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("Administrator:admindetails")
    else:
        return render(request,"Administrator\AdminRegistration.html",{"editdata":editdata})
    



def roomtype(request):
    data=tbl_roomtype.objects.all()
    if request.method=="POST":
        roomType=request.POST.get('txtroom')
        tbl_roomtype.objects.create(roomtype_type=roomType)
        return redirect("Administrator:roomtype")
    else:
        return render(request,"Administrator/RoomType.html",{'data':data})

def delRoomType(request,did):
    tbl_roomtype.objects.get(id=did).delete()
    return redirect("Administrator:roomtype")

def updRoomType(request,eid):
    editdata=tbl_roomtype.objects.get(id=eid)
    if request.method=="POST":
        editdata.roomtype_type=request.POST.get("txtroom")
        editdata.save()
        return redirect("Administrator:roomtype")
    else:
        return render(request,"Administrator/RoomType.html",{"editdata":editdata})
    

def placeInsertSelect(request):
    district = tbl_district.objects.all() 
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return redirect("Administrator:placeInsertSelect")
    else:
        return render(request,"Administrator/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Administrator:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("Administrator:placeInsertSelect")
    else:
        return render(request,"Administrator\Place.html",{"editdata":editdata,"districtdata":district})


def deptInsertSelect(request):
    data=tbl_dept.objects.all()
    if request.method=="POST":
        deptname=request.POST.get('txtname')
        tbl_dept.objects.create(dept_name=deptname)
        return redirect("Administrator:deptInsertSelect")
    else:
        return render(request,"Administrator/Department.html",{'data':data})

def delDept(request,did):
    tbl_dept.objects.get(id=did).delete()
    return redirect("Administrator:deptInsertSelect")

def deptupdate(request,eid):
    editdata=tbl_dept.objects.get(id=eid)
    if request.method=="POST":
        editdata.dept_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Administrator:deptInsertSelect")
    else:
        return render(request,"Administrator/Department.html",{"editdata":editdata})
    

def desigInsertSelect(request):
    data=tbl_desig.objects.all()
    if request.method=="POST":
        designame=request.POST.get('txtname')
        tbl_desig.objects.create(desig_name=designame)
        return redirect("Administrator:desigInsertSelect")
    else:
        return render(request,"Administrator/Desigination.html",{'data':data})

def delDesig(request,did):
    tbl_desig.objects.get(id=did).delete()
    return redirect("Administrator:desigInsertSelect")

def desigupdate(request,eid):
    editdata=tbl_desig.objects.get(id=eid)
    if request.method=="POST":
        editdata.desig_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Administrator:desigInsertSelect")
    else:
        return render(request,"Administrator/Desigination.html",{"editdata":editdata})
    


def newhotel(request):
    data=tbl_newhotel.objects.all()
    return render(request,"Administrator/HotelList.html",{'data':data})

def speciInsertSelect(request):
    data=tbl_specification.objects.all()
    if request.method=="POST":
        speciname=request.POST.get('txtspeci')
        tbl_specification.objects.create(speci_name=speciname)
        return redirect("Administrator:speciInsertSelect")
    else:
        return render(request,"Administrator/Specification.html",{'data':data})

def delSpeci(request,did):
    tbl_specification.objects.get(id=did).delete()
    return redirect("Administrator:speciInsertSelect")

def speciupdate(request,eid):
    editdata=tbl_specification.objects.get(id=eid)
    if request.method=="POST":
        editdata.speci_name=request.POST.get("txtspeci")
        editdata.save()
        return redirect("Administrator:speciInsertSelect")
    else:
        return render(request,"Administrator/Specification.html",{"editdata":editdata})
    


def facilityInsertSelect(request):
    data=tbl_facility.objects.all()
    if request.method=="POST":
        facilityname=request.POST.get('txtfacility')
        tbl_facility.objects.create(facility_name=facilityname)
        return redirect("Administrator:facilityInsertSelect")
    else:
        return render(request,"Administrator/Facility.html",{'data':data})

def delFacility(request,did):
    tbl_facility.objects.get(id=did).delete()
    return redirect("Administrator:facilityInsertSelect")

def facilityupdate(request,eid):
    editdata=tbl_facility.objects.get(id=eid)
    if request.method=="POST":
        editdata.speci_name=request.POST.get("txtfacility")
        editdata.save()
        return redirect("Administrator:facilityInsertSelect")
    else:
        return render(request,"Administrator/Facility.html",{"editdata":editdata})
    

def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Administrator/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("Administrator:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("Administrator:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Administrator/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Administrator/UserListRejected.html",{"userdata":userdata})



def hotelListNew(request):
    hoteldata = tbl_newhotel.objects.filter(hotel_vstatus=0)
    return render(request,"Administrator/HotelListNew.html",{"hoteldata":hoteldata})

def accepthotel(request,aid):
    hotel = tbl_newhotel.objects.get(id=aid)
    hotel.hotel_vstatus = 1
    hotel.save()
    return redirect("Administrator:LoadingHomePage")

def rejecthotel(request,rid):
    hotel = tbl_newhotel.objects.get(id=rid)
    hotel.hotel_vstatus = 2
    hotel.save()
    return redirect("Administrator:LoadingHomePage")

def hotelListAccepted(request):
    hoteldata = tbl_newhotel.objects.filter(hotel_vstatus=1)
    return render(request,"Administrator/HotelListAccepted.html",{"hoteldata":hoteldata})

def hotelListRejected(request):
    hoteldata = tbl_newhotel.objects.filter(hotel_vstatus=2)
    return render(request,"Administrator/HotelListRejected.html",{"hoteldata":hoteldata})

def aadhar(request):
    data=tbl_aadhar.objects.all()
    if request.method=="POST":
        aadharname=request.POST.get('txtname')
        aadharno=request.POST.get('txtaadhar')
        tbl_aadhar.objects.create(aadhar_name=aadharname,aadhar_number=aadharno)
        return redirect("Administrator:aadhar")
    else:
        return render(request,"Administrator/Aadhar.html",{'data':data})
    

def delAadhar(request,did):
    tbl_aadhar.objects.get(id=did).delete()
    return redirect("Administrator:aadhar")

def userbooking(request):
    booking = tbl_booking.objects.all()
    return render(request,"Administrator/User_Booking.html",{"data":booking})

def sendmail(request,id):
    booking = tbl_booking.objects.get(id=id)
    user_email = booking.user.user_email
    user = booking.user.user_name
    hotal_name = booking.hotel.hotel_name
    amount = booking.booking_amount
    send_mail(
            f"Dear {user}",  # Subject
            (f"We are delighted to confirm your upcoming stay with us at {hotal_name}! Your adventure begins here.\r\n"
            "Below you will find all the important details of your reservation.\r\n"
            "Please review them to ensure everything is as per your plans:\r\n"
            "Reservation Details:\r\n"
            f"Hotel Name: {hotal_name}\r\n"
            f"Amount: {amount}\r\n"),
            settings.EMAIL_HOST_USER,
            [user_email],
        )
    booking.booking_status = 5
    booking.save()
    return redirect("Administrator:userbooking")

def viewcomplaint(request):
    user = tbl_user.objects.all()
    hotel = tbl_newhotel.objects.all()
    usercom = tbl_complaint.objects.filter(user__in=user,complaint_status=0)
    hotelcom = tbl_complaint.objects.filter(hotel__in=hotel,complaint_status=0)
    return render(request,"Administrator/View_complaint.html",{"user":usercom,"hotel":hotelcom})

def reply(request,id):
    com = tbl_complaint.objects.get(id=id)
    if request.method == "POST":
        com.complaint_status = 1
        com.complaint_reply = request.POST.get("txt_reply")
        com.save()
        return redirect("Administrator:viewcomplaint")
    else:
        return render(request,"Administrator/Reply.html")
    
def viewreplyedcomplaint(request):
    user = tbl_user.objects.all()
    hotel = tbl_newhotel.objects.all()
    usercom = tbl_complaint.objects.filter(user__in=user,complaint_status=1)
    hotelcom = tbl_complaint.objects.filter(hotel__in=hotel,complaint_status=1)
    return render(request,"Administrator/View_Replyed_Complaints.html",{"user":usercom,"hotel":hotelcom})

def logout(request):
    del request.session['adminid']
    return redirect("Guest:Login")