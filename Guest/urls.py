from django.urls import path,include
from Guest import views
#from Administrator import *

app_name="Guest"
urlpatterns = [

    path('',views.Home,name="Home"),
    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Login/',views.Login,name="Login"),




    path('NewHotel/',views.hotelRegistration,name="hotelRegistration"),

    path('SearchHotel/',views.searchhotel,name="searchhotel"),
    path('HotelDetailViewMore/<int:hid>',views.viewmore,name="viewmore"),

]