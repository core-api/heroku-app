from rest_framework import serializers


class AddNoteSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)


class EditNoteSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100, required=False)
    complete = serializers.BooleanField(required=False)
