from crontab import CronTab

from .models import AlarmSchedule, AlarmScheduleSerializer


class CronJobService:
    """ A service provider for cron job management """
    def __init__(self):
        self.cron = CronTab(user=True)

    def update_all(self):
        self.cron.remove_all()
        self._create_jobs()
        self.cron.write()

    def clear_all(self):
        self.cron.remove_all()
        self.cron.write()

    def print_all(self):
        for job in self.cron:
            print(job)

    def _create_jobs(self):
        alarms = AlarmSchedule.objects.all()
        for alarm in alarms:
            if not alarm.active:
                continue
            time = self._serialize_alarm_time(alarm)
            job = self.cron.new(command=alarm.command, comment=str(alarm.id))
            job.setall(time)

    def _serialize_alarm_time(self, model):
        template = "{} {} * * {}"
        serialized = template.format(model.minute,
                                     model.hour,
                                     model.day_of_week)
        return serialized


class CRUDResult:
    def __init__(self, success, data=None, message=""):
        self.success = success
        self.data = data
        self.message = message


class AlarmService:
    """
    Provides CRUD operations for AlarmSchedule
    Consumes JSON, and outputs serialized data
    """

    def _get_object(self, pk):
        try:
            return AlarmSchedule.objects.get(pk=pk)
        except AlarmSchedule.DoesNotExist:
            raise

    def create(self, data):
        """ (json) -> Serialized model """
        serializer = AlarmScheduleSerializer(data=data)
        if serializer.is_valid():
            alarm = serializer.save()
            serializer = AlarmScheduleSerializer(alarm)
            return CRUDResult(True, serializer.data)
        return CRUDResult(False, message="Provided data had invalid format")

    def read_all(self):
        """ () -> List(Serialized model) """
        alarms = AlarmSchedule.objects.all()
        serializer = AlarmScheduleSerializer(alarms, many=True)
        return CRUDResult(True, serializer.data)

    def read(self, pk):
        """ (int) -> Serialized model """
        try:
            alarm = self._get_object(pk)
            serializer = AlarmScheduleSerializer(alarm)
            return CRUDResult(True, serializer.data)
        except AlarmSchedule.DoesNotExist:
            return CRUDResult(False, message="No entries with the provided \
                                              primary key was found from \
                                              the database")

    def update(self, data, pk):
        """ """
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
        """ """
        try:
            alarm = self._get_object(pk)
            alarm.delete()
            return CRUDResult(True)
        except AlarmSchedule.DoesNotExist:
            return CRUDResult(False, message="No entries with the provided \
                                              primary key was found from \
                                              the database")
