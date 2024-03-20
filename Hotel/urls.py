from django.urls import path
from Hotel import views
app_name="Hotel"
urlpatterns = [
    path('homepage/',views.homepages,name="homepages"),
    path('My_profile/',views.my_pros,name="my_pros"),
    path('editprofile/',views.editprofiles,name="editprofiles"),
    path('changepassword/',views.changepasswords,name="changepasswords"),

    
    path('RoomDetails/', views.roomInsertSelect,name="roomInsertSelect"),
    #path('delRoom/<int:did>', views.delRoom,name="delRoom"),
    #path('roomupdate/<int:eid>',views.roomupdate,name="roomupdate"),
]