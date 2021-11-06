from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   


    path("", views.home , name='home'),
    path("room/<str:pk>/", views.room , name='room'),
    

    path("create-room/", views.createRoom, name='create-room'),
    path("update-room/<str:pk>", views.updateRoom, name='update-room'),
    path("delete-room/<str:pk>", views.deleteRoom, name='delete-room'),

    
    path("delete-massage/<str:pk>", views.deleteMassage, name='delete-massage'),

    path('profile/<str:pk>', views.userProfile , name= 'profile'),

    path('topics/', views.topicpage , name='topics'),
    path('activities/', views.activitypage , name='activities'),
    

]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)