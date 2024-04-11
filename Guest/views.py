from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from Administrator.models import *
from User.models import *

# Create your views here.

def Home(request):
    return render(request,"Guest/Home.html")

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
    hotel_spe=tbl_specification.objects.all()
    #speci=None
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
        hotelurl=request.POST.get('txturl')
        #hotelspe = tbl_place.objects.get(id=request.POST.get('sel_place'))
        #hotel_spe=request.POST.get('sel_speci')
        #speci = tbl_specification.objects.get(id=request.POST.get('sel_speci'))
        hotel_spe=request.POST.get('sel_spe')
        
        
        Hdata = tbl_newhotel.objects.create(hotel_name=hotelname,hotel_ratings=hotelratings,hotel_contact=hotelcontact,hotel_email=hotelemail,hotel_pass=hotelpass,place=place,hotel_addr=hoteladdr,hotel_photo=hotelphoto,hotel_license=hotellicense,hotel_proof=hotelproof,hotel_floor=hotelfloor,hotel_url=hotelurl,hotel_spe=tbl_specification.objects.get(id=hotel_spe))                                     
         #hotel_spe=tbl_specification.objects.get(id=hotelspe))

        for i in range(int(hotelfloor)):
            tbl_floor.objects.create(floor_count=i,hotel=Hdata)


        return redirect("Guest:hotelRegistration")
    else:
        return render(request,"Guest/NewHotel.html",{"districtdata":district,"spefication":hotel_spe})
    

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
            request.session["floor"]=user.hotel_floor
            return redirect("Hotel:homepages")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")
    
def searchhotel(request):
    if 'uid' in request.session:
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
            return render(request,"Guest/SearchHotel.html",{"districtdata":district,'data':filterdata,"ar":ar})
        else:
            return render(request,"Guest/SearchHotel.html",{"districtdata":district,'data':datas,"ar":ar})
    else:
        return redirect("Guest:Login")
    
def viewmore(request,hid):
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
    return render(request,"Guest/HotelDetailViewMore.html",{'data':data,'data1':data1,"id":hid,"facility":facility,"roomdetails":rm_details,"common":common_fac})