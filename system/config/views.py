from rest_framework.viewsets import ModelViewSet

from system.config.models import Venue, Course, Semester, Slot, Day, Programme, Section
from system.config.serializers import VenueSerializer, CourseSerializer, SemesterSerializer, SlotSerializer, \
    DaySerializer, ProgrammeSerializer, SectionSerializer


class SectionView(ModelViewSet):
    serializer_class = SectionSerializer
    model = Section

    def get_queryset(self):
        return self.model.objects.all()


class ProgrammeView(ModelViewSet):
    serializer_class = ProgrammeSerializer
    model = Programme

    def get_queryset(self):
        return self.model.objects.all()


class DayView(ModelViewSet):
    serializer_class = DaySerializer
    model = Day

    def get_queryset(self):
        return self.model.objects.all()


class SlotView(ModelViewSet):
    serializer_class = SlotSerializer
    model = Slot

    def get_queryset(self):
        return self.model.objects.all()


class SemesterView(ModelViewSet):
    serializer_class = SemesterSerializer
    model = Semester

    def get_queryset(self):
        return self.model.objects.all()


class CourseView(ModelViewSet):
    serializer_class = CourseSerializer
    model = Course

    def get_queryset(self):
        return self.model.objects.all()


class VenueView(ModelViewSet):
    serializer_class = VenueSerializer
    model = Venue

    def get_queryset(self):
        return self.model.objects.all()
