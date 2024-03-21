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
]