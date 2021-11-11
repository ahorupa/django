from django.urls import path
from.views import*

urlpatterns = [
    path('sign_up/', UserRegisterView.as_view(), name="sign_up")


]
