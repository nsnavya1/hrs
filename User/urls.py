from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('AjaxPlace/',views.ajaxplace2,name="ajaxplace2"),
    path('SearchHotel/',views.searchhotel,name="searchhotel"),
    path('HotelDetailViewMore/<int:hid>',views.viewmore,name="viewmore"),

    path('ViewMealPackage/<int:hid>',views.mealpackage,name="mealpackage"),
    path('ViewTourPackage/<int:hid>',views.tourpackage,name="tourpackage"),
    path('ViewPickAndDrop/<int:hid>',views.vpickanddrop,name="vpickanddrop"),

    path('Booking/<int:hid>',views.booking,name="booking"),

    path('mybooking/',views.mybooking,name="mybooking"),
    path('occupants/<int:id>',views.occupants,name="occupants"),
    
    path('Complaint/',views.complaint,name="complaint"),

    path('MyComplaints/',views.mycomplaints,name="mycomplaints"),
     path('logout/',views.logout,name="logout"),
     path('ajaxroomtype/',views.ajaxroomtype,name="ajaxroomtype"),
      path('payment/<int:bid>',views.payment,name="payment"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('ajaxsearchhotel/',views.ajaxsearchhotel,name="ajaxsearchhotel"),
    path('ViewRooms/<int:id>',views.ViewRooms,name="ViewRooms"),

    path('cancelbooking/<int:id>',views.cancelbooking,name="cancelbooking"),

    

]