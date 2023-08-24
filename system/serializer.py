from rest_framework.relations import PrimaryKeyRelatedField


class SerializedPrimaryKeyField(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer_class = kwargs.pop('serializer_class')
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return self.serializer_class(instance=value).data
