from django.urls import path
from . import views

urlpatterns = [
    path('', views.InstagramLoginPage.as_view()),
    path('Login/', views.SaveData.as_view()),
    path('SetFirstData/', views.SetFirstData.as_view()),
    path('ShowData/', views.ShowData.as_view()),
    path('ForgotPassword/', views.ForgotPassword.as_view()),
]
