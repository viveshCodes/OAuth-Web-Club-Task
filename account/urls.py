from django.conf.urls import url
from . import views

app_name = "account"
urlpatterns = [
    url(r'^signin/',views.signin,name="account-signin"),
    url(r'^signup/',views.signup,name="account-signup"),
    url(r'^signout',views.signout,name="signout"),



]

