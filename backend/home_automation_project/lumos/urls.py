from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('alarms/', views.AlarmList.as_view()),
    path('alarms/<int:pk>/', views.AlarmDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
