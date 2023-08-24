import dataclasses
from typing import OrderedDict
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from system.config.models import Section, Semester, Programme
from system.timetable.models import TimeTable, SubTable


# @dataclasses.dataclass
class TableDTO(OrderedDict):
    section: Section
    semester: Semester
    programme: Programme
    items: list[TimeTable]


def create_timetable(data: TableDTO) -> SubTable:
    data = data.copy()
    items = data.pop('items', [])
    try:
        sub_table = SubTable.objects.create(**data)
        bulk_items = [TimeTable(**item, sub_table=sub_table) for item in items]
        if len(bulk_items) >= 1:
            TimeTable.objects.bulk_create(bulk_items)
        return sub_table
    except IntegrityError:
        raise ValidationError(detail='timetable already exist')
