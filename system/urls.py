from django.urls import path, include

urlpatterns = [
    path('config/', include('system.config.urls')),
    path('timetable/', include('system.timetable.urls')),
]
