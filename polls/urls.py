from django.urls import path
from rest_framework import routers

from . import views
from . import apiviews
router = routers.SimpleRouter()

app_name = 'polls'
urlpatterns = [
    path('questions/', apiviews.questions_view, name='questions_view'),
    path('pname/', apiviews.polls_view, name='polls_view'),
    path('choice/', apiviews.choice_view, name='choice_view'),
    path('pname/<int:poll_id>/', apiviews.polls_detail_view,
         name='poll_detail_view'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
