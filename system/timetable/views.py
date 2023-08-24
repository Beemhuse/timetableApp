from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from system.timetable.models import SubTable, TimeTable
from system.timetable.serializers import SubTableSerializer, ItemSerializer
from system.timetable.services import create_timetable


class SubTableView(ModelViewSet):
    serializer_class = SubTableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section', 'programme', 'semester']
    model = SubTable
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        return self.model.objects.all()

    def perform_create(self, serializer):
        table = create_timetable(serializer.validated_data)
        return table


class TableItemView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ItemSerializer
    model = TimeTable

    def get_queryset(self):
        return self.model.objects.all()
