from django.urls import path
from rest_framework.routers import DefaultRouter
from system.timetable.views import SubTableView, TableItemView

router = DefaultRouter()
router.register('', SubTableView, 'timetable')

urlpatterns = router.urls
urlpatterns.extend([
    path('item/<int:id>', TableItemView.as_view())
])
