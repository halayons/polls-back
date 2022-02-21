from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

import json


# polls/apiviews.py
@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def polls_view(request):
    if request.method == 'GET':
        polls = Polls.objects.all()
        serializer = PollsSerializer(polls, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PollsSerializer(data=request.data)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollsSerializer(poll).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def polls_detail_view(request, poll_id):
    poll = get_object_or_404(Polls, pk=poll_id)
    if request.method == 'GET':
        serializer = PollsDetailPageSerializer(poll)
        return Response(serializer.data)


class QuestionViewSets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializar_class = QuestionSerializer


class PollViewSets(viewsets.ModelViewSet):
    queryset = Polls.objects.all()
    serializar_class = PollsSerializer
