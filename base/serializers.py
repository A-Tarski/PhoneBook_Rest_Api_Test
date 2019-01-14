from rest_framework import serializers
from base.models import Record

class RecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    number = serializers.CharField(required=True, allow_blank=False, max_length=30)

    def create(self, validated_data):
        return Record.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance

    class Meta:
        model = Record
        fields = ('id', 'name', 'number')
