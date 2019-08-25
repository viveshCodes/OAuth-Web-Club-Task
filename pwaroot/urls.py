from django.conf.urls import url , include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^blog/' ,include("blog.urls")),
    #url(r'^account/', include("account.urls")),
    url('', include('pwa.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^home',views.home, name='home'),
    url(r'^$',views.index,name="index"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
