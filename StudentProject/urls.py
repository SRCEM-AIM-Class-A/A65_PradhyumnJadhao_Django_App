from django.contrib import admin
from django.urls import path, include
from app1 import views as app1_views
from app2 import views as app2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1_views.home, name='home'),  # Home Page
    path('about/', app1_views.about, name='about'),  # About Page
    path('app2/', app2_views.app2_home, name='app2_home'),  # App2 Page
]
