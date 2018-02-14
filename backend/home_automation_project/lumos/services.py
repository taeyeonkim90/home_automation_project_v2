from .models import AlarmSchedule, AlarmScheduleSerializer


class CronJobService:
    """ A service provider for cron job management """

    pass


class CRUDResult:
    def __init__(self, success, data=None, message=""):
        self.success = success
        self.data = data
        self.message = message


class AlarmService:
    """ Provides CRUD managements for AlarmSchedule models """

    def _get_object(self, pk):
        try:
            return AlarmSchedule.objects.get(pk=pk)
        except AlarmSchedule.DoesNotExist:
            raise

    def create(self, data):
        serializer = AlarmScheduleSerializer(data=data)
        if serializer.is_valid():
            alarm = serializer.save()
            serializer = AlarmScheduleSerializer(alarm)
            return CRUDResult(True, serializer.data)
        return CRUDResult(False, message="Provided data had invalid format")

    def read_all(self):
        alarms = AlarmSchedule.objects.all()
        serializer = AlarmScheduleSerializer(alarms, many=True)
        return CRUDResult(True, serializer.data)

    def read(self, pk):
        try:
            alarm = self._get_object(pk)
            serializer = AlarmScheduleSerializer(alarm)
            return CRUDResult(True, serializer.data)
        except AlarmSchedule.DoesNotExist:
            return CRUDResult(False, message="No entries with the provided \
                                              primary key was found from \
                                              the database")

    def update(self, data, pk):
        try:
            alarm = self._get_object(pk)
            serializer = AlarmScheduleSerializer(alarm, data=data)
            if serializer.is_valid():
                alarm = serializer.save()
                serializer = AlarmScheduleSerializer(alarm)
                return CRUDResult(True, serializer.data)
            return CRUDResult(False,
                              message="Provided data had invalid format")
        except AlarmSchedule.DoesNotExist:
            return CRUDResult(False, message="No entries with the provided \
                                              primary key was found from \
                                              the database")

    def delete(self, pk):
        try:
            alarm = self._get_object(pk)
            alarm.delete()
            return CRUDResult(True)
        except AlarmSchedule.DoesNotExist:
            return CRUDResult(False, message="No entries with the provided \
                                              primary key was found from \
                                              the database")
