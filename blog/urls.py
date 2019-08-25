from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$',views.blog_home,name="blog-home"),
    url(r'^look/',views.blog_look,name="blog-look"),

]

