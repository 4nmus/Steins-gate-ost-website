from django.contrib import admin
from django.urls import path
import front.views as vws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vws.HomeView.as_view(), name='home-page')
]
