from django.urls import path
from app import views


urlpatterns =[
    path('',views.index,name="index"),
    path('booking',views.book_appo,name="book_appo"),
]