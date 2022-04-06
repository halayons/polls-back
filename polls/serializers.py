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


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollsListPageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    poll_name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Polls.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PollsDetailPageSerializer(PollsListPageSerializer):
    polls = PollsSerializer(many=True, read_only=True)
