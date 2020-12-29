from django.urls import path
from .views import toppage,search,date,getok
urlpatterns=[
    path("",toppage,name="top"),
    path("search/<str:name>",search),
    path("date/<int:date>",date),
    path("getok",getok,name="getok")
    ]
