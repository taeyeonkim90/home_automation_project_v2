from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import AlarmSchedule, AlarmScheduleSerializer


class AlarmList(APIView):
    """
    List all alarms, or create a new alarm.
    """
    def get(self, request, format=None):
        alarms = AlarmSchedule.objects.all()
        serializer = AlarmScheduleSerializer(alarms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlarmScheduleSerializer(data=request.data)
        if serializer.is_valid():
            alarm = serializer.save()
            serializer = AlarmScheduleSerializer(alarm)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlarmDetail(APIView):
    """
    Retrieve, update or delete a alarm instance.
    """
    def get_object(self, pk):
        try:
            return AlarmSchedule.objects.get(pk=pk)
        except AlarmSchedule.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        alarm = self.get_object(pk)
        serializer = AlarmScheduleSerializer(alarm)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        alarm = self.get_object(pk)
        serializer = AlarmScheduleSerializer(alarm, data=request.data)
        if serializer.is_valid():
            alarm = serializer.save()
            serializer = AlarmScheduleSerializer(alarm)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        alarm = self.get_object(pk)
        alarm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)