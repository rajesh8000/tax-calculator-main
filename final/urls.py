from django.urls import path
from .views import BlogListView, BlogDetailView

from . import views

#making routes and urls
urlpatterns = [
    path('',views.home, name='index'), 
    path('news/', BlogListView.as_view(), name='news'),
    path('news/<int:pk>/', BlogDetailView.as_view(), name='inside-news'),
    path('faqs/',views.faqs , name='faqs'),
    path('aboutus/',views.aboutus , name='aboutus') , 
    path('signin/',views.signin , name='signin') ,
    path('signup/',views.signup , name='signup') ,
    path('logout/',views.logoutuser , name='logout') ,
    path('profile/',views.profileuser , name='profile') ,
    path('history/',views.viewHistory , name='profileHistory') ,
    path('Vat/',views.Vat , name='Vat') ,
]
