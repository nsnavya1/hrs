from django.urls import path
from Hotel import views
app_name="Hotel"
urlpatterns = [
    path('homepage/',views.homepages,name="homepages"),
    path('My_profile/',views.my_pros,name="my_pros"),
    path('editprofile/',views.editprofiles,name="editprofiles"),
    path('changepassword/',views.changepasswords,name="changepasswords"),

    
    path('RoomDetails/', views.roomInsertSelect,name="roomInsertSelect"),
    path('delRoomDetails/<int:did>', views.delRoomDetails,name="delRoomDetails"),


    path('HotelFacilities/', views.HotelFacilitiesInsertSelect,name="HotelFacilitiesInsertSelect"),
    path('delHotelFacilities/<int:did>', views.delHotelFacilities,name="delHotelFacilities"),

    path('MealPackages/', views.MealPackagesInsertSelect,name="MealPackagesInsertSelect"),
    path('delMealPackages/<int:did>', views.delMealPackages,name="delMealPackages"),

    path('TourPackages/', views.TourPackagesInsertSelect,name="TourPackagesInsertSelect"),
    path('delTourPackages/<int:did>', views.delTourPackages,name="delTourPackages"),

    path('PickAndDropHead/',views.pickanddropinsertselect,name="pickanddropinsertselect"),
    path('delPickAndDropHead/<int:did>', views.delpickanddrop,name="delpickanddrop"),

    path('Specialized/', views.specializedInsertSelect,name="specializedInsertSelect"),
    path('delSpecialized/<int:did>', views.delspecialized,name="delspecialized"),

    path('Userbooking/',views.userbooking,name="userbooking"),

    path('acceptbooking/<int:aid>',views.acceptbooking,name="acceptbooking"),
    path('rejectbooking/<int:rid>',views.rejectbooking,name="rejectbooking"),
    path('sentconfirmation/<int:id>',views.sentconfirmation,name="sentconfirmation"),

    path('adddetails/<int:id>',views.adddetails,name="adddetails"),

    path('Complaint/',views.complaint,name="complaint"),
    path('MyComplaints/',views.mycomplaints,name="mycomplaints"),

    path('logout/',views.logout,name="logout"),

]