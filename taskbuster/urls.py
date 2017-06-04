
from django.conf.urls import url
from django.contrib import admin
from .views import home, home_files

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^$', home, name='home'),
]
