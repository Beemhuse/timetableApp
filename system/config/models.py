from django.db import models

from system.models import BaseModel


class Section(BaseModel):
    name = models.CharField(max_length=255)


class Programme(BaseModel):
    name = models.CharField(max_length=255)


class Day(BaseModel):
    name = models.CharField(max_length=255)


class Slot(BaseModel):
    name = models.CharField(max_length=255)


class Semester(BaseModel):
    name = models.CharField(max_length=255)


class Course(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=8)


class Venue(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=8)
