from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import AlarmService, CronJobService


class AlarmView(APIView):
    """
    Base class to configure dependencies in the constructor
    """
    def __init__(self):
        super()
        self.alarm_service = AlarmService()
        self.cron_service = CronJobService()


class AlarmList(AlarmView):
    """
    List all alarms, or create a new alarm.
    """
    def get(self, request, format=None):
        result = self.alarm_service.read_all()
        if result.success:
            return Response(result.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        result = self.alarm_service.create(request.data)
        if result.success:
            return Response(result.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AlarmDetail(AlarmView):
    """
    Retrieve, update or delete a alarm instance.
    """
    def get(self, request, pk, format=None):
        result = self.alarm_service.read(pk)
        if result.success:
            return Response(result.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        result = self.alarm_service.update(request.data, pk)
        if result.success:
            return Response(result.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        result = self.alarm_service.delete(pk)
        if result.success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
