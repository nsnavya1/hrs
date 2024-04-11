from django.urls import path,include
from Administrator import views

app_name="Administrator"
urlpatterns = [

    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),


    path('Add/',views.add,name="Add"),
    path('Add2/',views.add2,name="add2"),
    path('Greater/',views.greater,name="Greater"),
    path('Calculator/',views.calculator,name="Calculator"),
    path('Personal/',views.personal,name="Personal"),
    path('Salary/',views.salary,name="Salary"),

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),

   
    path('AdminRegistration/',views.admindetails,name="admindetails"),
    path('delAdminRegistration/<int:did>', views.deladmindetails,name="deladmindetails"),
    path('updAdminRegistration/<int:eid>', views.updadmindetails,name="updadmindetails"),
    
    path('RoomType/',views.roomtype,name="roomtype"),
    path('delRoomType/<int:did>', views.delRoomType,name="delRoomType"),
    path('updRoomType/<int:eid>',views.updRoomType,name="updRoomType"),

    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),




    path('Deptartment/', views.deptInsertSelect,name="deptInsertSelect"),
    path('delDept/<int:did>', views.delDept,name="delDept"),
    path('deptupdate/<int:eid>',views.deptupdate,name="deptupdate"),

    path('Desigination/', views.desigInsertSelect,name="desigInsertSelect"),
    path('delDesig/<int:did>', views.delDesig,name="delDesig"),
    path('desigupdate/<int:eid>',views.desigupdate,name="desigupdate"),

   
    
    #path('HotelList/',views.newhotel,name="newhotel"),


    path('Specification/', views.speciInsertSelect,name="speciInsertSelect"),
    path('delSpeci/<int:did>', views.delSpeci,name="delSpeci"),
    path('Speciupdate/<int:eid>',views.speciupdate,name="speciupdate"),

    path('Facility/', views.facilityInsertSelect,name="facilityInsertSelect"),
    path('delFacility/<int:did>', views.delFacility,name="delFacility"),
    path('Facilityupdate/<int:eid>',views.facilityupdate,name="facilityupdate"),


    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),

    path('HotelListNew/',views.hotelListNew,name="hotelListNew"),
    path('accepthotel/<int:aid>',views.accepthotel,name="accepthotel"),
    path('rejecthotel/<int:rid>',views.rejecthotel,name="rejecthotel"),
    path('HotelListAccepted/',views.hotelListAccepted,name="hotelListAccepted"),
    path('HotelListRejected/',views.hotelListRejected,name="hotelListRejected"),


    path('Aadhar/',views.aadhar,name="aadhar"),
    path('delAadhar/<int:did>', views.delAadhar,name="delAadhar"),

    path('userbooking/', views.userbooking,name="userbooking"),
    path('sendmail/<int:id>', views.sendmail,name="sendmail"),

    path('viewcomplaint/', views.viewcomplaint,name="viewcomplaint"),
    path('reply/<int:id>', views.reply,name="reply"),
    path('viewreplyedcomplaint/', views.viewreplyedcomplaint,name="viewreplyedcomplaint"),

    path("logout/",views.logout,name="logout"),


]