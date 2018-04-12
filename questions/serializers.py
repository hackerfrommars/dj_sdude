from rest_framework import serializers


class AnswerSerializer(serializers.Serializer):
    to_question = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    content = serializers.CharField()
