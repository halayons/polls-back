import datetime
from statistics import mode
from django.db import models
from django.utils import timezone

# Create your models here.


class Polls(models.Model):
    poll_name = models.CharField(max_length=100)

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    answer = models.IntegerField()
    option_one = models.CharField(max_length=100, blank=True)
    option_two = models.CharField(max_length=100, blank=True)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
