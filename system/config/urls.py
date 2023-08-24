from rest_framework.routers import DefaultRouter

from system.config.views import SectionView, ProgrammeView, SlotView, DayView, SemesterView, CourseView, VenueView

router = DefaultRouter()
router.register('section', SectionView, 'section')
router.register('programme', ProgrammeView, 'programme')
router.register('slot', SlotView, 'slot')
router.register('day', DayView, 'day')
router.register('semester', SemesterView, 'semester')
router.register('course', CourseView, 'course')
router.register('venue', VenueView, 'venue')

urlpatterns = router.urls
