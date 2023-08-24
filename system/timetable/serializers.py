from rest_framework import serializers

from system.config.models import Course, Section, Programme, Day, Slot, Semester, Venue
from system.config.serializers import VenueSerializer, SlotSerializer, CourseSerializer, DaySerializer, \
    SemesterSerializer, SectionSerializer, ProgrammeSerializer
from system.serializer import SerializedPrimaryKeyField
from system.timetable.models import TimeTable, SubTable


class ItemSerializer(serializers.ModelSerializer):
    venue = SerializedPrimaryKeyField(serializer_class=VenueSerializer, queryset=Venue.objects.all())
    slot = SerializedPrimaryKeyField(serializer_class=SlotSerializer, queryset=Slot.objects.all())
    course = SerializedPrimaryKeyField(serializer_class=CourseSerializer, queryset=Course.objects.all())
    day = SerializedPrimaryKeyField(serializer_class=DaySerializer, queryset=Day.objects.all())

    class Meta:
        fields = ['id', 'day', 'course', 'venue', 'slot']
        model = TimeTable
        read_only_fields = ['id']


class SubTableSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    section = SerializedPrimaryKeyField(serializer_class=SectionSerializer, queryset=Section.objects.all())
    semester = SerializedPrimaryKeyField(serializer_class=SemesterSerializer, queryset=Semester.objects.all())
    programme = SerializedPrimaryKeyField(serializer_class=ProgrammeSerializer, queryset=Programme.objects.all())

    class Meta:
        fields = ['id', 'section', 'semester', 'programme', 'items', 'created_at']
        model = SubTable
        read_only_fields = ['id']
