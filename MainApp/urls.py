
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('Members.urls')),
    path('', include('base.urls')),
    path('app/', include('App.urls')),
]
