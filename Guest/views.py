from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *

# Create your views here.

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        username=request.POST.get("txtname")
        usergender=request.POST.get("gender")
        usercontact=request.POST.get("txtcontact")
        userdob=request.POST.get("txtdate")
        useremail=request.POST.get("txtemail")
        userpassword=request.POST.get("txtpwd")
        useraadhar=request.POST.get("txtaadhar")
        userphoto=request.FILES.get("fileImage")
        userproof=request.FILES.get("fileProof")
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        useraddress=request.POST.get("txtaddr")
        tbl_user.objects.create(user_name=username,user_gender=usergender,user_contact=usercontact,user_dob=userdob,user_email=useremail,user_password=userpassword,user_aadhar=useraadhar,user_photo=userphoto,user_proof=userproof,place=place,user_address=useraddress)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})   
    
def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})



def hotelRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        hotelname=request.POST.get('txtname')
        hotelratings=request.POST.get('txtratings')
        hotelcontact=request.POST.get('txtcontact')
        hotelemail=request.POST.get('txtemail')
        hotelpass=request.POST.get('txtpwd') 
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        hoteladdr=request.POST.get('txtaddress')
        hotelphoto=request.FILES.get('filephoto')
        hotellicense=request.POST.get('txtlicense')
        hotelproof=request.FILES.get('fileproof')
        hotelfloor=request.POST.get('txtfloor')
        
        tbl_newhotel.objects.create(hotel_name=hotelname,hotel_ratings=hotelratings,hotel_contact=hotelcontact,hotel_email=hotelemail,hotel_pass=hotelpass,place=place,hotel_addr=hoteladdr,hotel_photo=hotelphoto,hotel_license=hotellicense,hotel_proof=hotelproof,hotel_floor=hotelfloor)
        return redirect("Guest:hotelRegistration")
    else:
        return render(request,"Guest/NewHotel.html",{"districtdata":district})
    

def Login(request):
    if request.method == "POST":
        
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        usercount = tbl_user.objects.filter(user_status='1',user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        hotelcount = tbl_newhotel.objects.filter(hotel_vstatus='1',hotel_email=request.POST.get("txt_email"),hotel_pass=request.POST.get("txt_password")).count()
        
        if admincount > 0:
            user = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["adminid"] = user.id
            request.session["adminname"] = user.admin_name
            return redirect("Administrator:LoadingHomePage")
        elif usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:homepage")
        elif hotelcount > 0:
            user = tbl_newhotel.objects.get(hotel_email=request.POST.get("txt_email"),hotel_pass=request.POST.get("txt_password"))
            request.session["hid"] = user.id
            request.session["hname"] = user.hotel_name
            return redirect("Hotel:homepages")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")