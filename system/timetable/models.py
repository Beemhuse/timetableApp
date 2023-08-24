from django.db import models

from system.config.models import Programme, Semester, Venue, Course, Slot, Section, Day
from system.models import BaseModel


class SubTable(BaseModel):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='time_table')
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='time_table')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='time_table')

    def __str__(self):
        return f'{self.section.name} -> {self.programme.name}:{self.section.name}'

    class Meta:
        unique_together = ('section', 'programme', 'semester')


class TimeTable(BaseModel):
    sub_table = models.ForeignKey(SubTable, on_delete=models.CASCADE, related_name='items')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_query_name='items')
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_query_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_query_name='items')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_query_name='items')

    def __str__(self):
        return f'{self.day}: {self.course.name}'

    class Meta:
        unique_together = ('day', 'venue', 'slot')
