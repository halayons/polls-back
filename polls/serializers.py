from pyexpat import model
from .models import *
from rest_framework import serializers


# class QuestionSerializer(serializers.Serializer):
#     question_text = serializers.CharField(max_length=200)
#     poll_name = serializers.CharField(max_length=100)
#     pub_date = serializers.DateTimeField()

#     # DRF serializer.save() calls self.create(self.validated_data)
#     def create(self, validated_data):
#         return Question.objects.create(**validated_data)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = '__all__'
