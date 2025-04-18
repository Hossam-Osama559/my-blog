from django.urls import path

from . import views




urlpatterns = [
 path("",views.index,name="index"),
 path("os/<str:number>",views.os,name="os")
]