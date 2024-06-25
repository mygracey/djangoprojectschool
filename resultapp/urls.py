from django.urls import path
from . import views


urlpatterns = [
    path('',views.indexPage,name='index'),
    path('result/',views.resultPage,name='result'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout')
    
]
