from rest_framework import serializers

from system.config.models import Course, Section, Programme, Day, Slot, Semester, Venue


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Section
        read_only_fields = ['id']


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Programme
        read_only_fields = ['id']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Day
        read_only_fields = ['id']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Slot
        read_only_fields = ['id']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Semester
        read_only_fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'code']
        model = Course
        read_only_fields = ['id']


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'code']
        model = Venue
        read_only_fields = ['id']
