from django.db import models
from rest_framework import serializers


ALARM_SCRIPT_PATH = "/home/pi/Projects/home_automation_project_v2/backend/home_automation_project/scripts/run_led.sh"


class AlarmSchedule(models.Model):
    """
    Cron-based representation of a scheduled task
    minute (0 - 59)
    hour (0 - 23)
    day of week (0 - 6) (Sunday to Saturday;
    """
    minute = models.CharField(default="*", max_length=100)
    hour = models.CharField(default="*", max_length=100)
    day_of_week = models.CharField(default="*", max_length=100)
    command = models.CharField(default=ALARM_SCRIPT_PATH, max_length=100)
    active = models.BooleanField(default=False)


class AlarmScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    minute = serializers.CharField(default="*", max_length=100)
    hour = serializers.CharField(default="*", max_length=100)
    day_of_week = serializers.CharField(default="*", max_length=100)
    command = serializers.CharField(default=ALARM_SCRIPT_PATH, max_length=100)
    active = serializers.BooleanField(default=False)

    VALIDATION_ERROR_MSG = "Invalid input for scheduling an alarm task"

    """ validates user provided information during serialization """
    def validate_minute(self, val):
        minutes = {str(x) for x in range(0, 61)}
        minutes.add("*")
        if val not in minutes:
            raise serializers.ValidationError(self.VALIDATION_ERROR_MSG)
        return val

    def validate_hour(self, val):
        hours = {str(x) for x in range(0, 24)}
        hours.add("*")
        if val not in hours:
            raise serializers.ValidationError(self.VALIDATION_ERROR_MSG)
        return val

    def validate_day_of_week(self, val):
        days = {str(x) for x in range(0, 7)}
        if val != "*":
            for day in val.split(","):
                if day not in days:
                    raise serializers.ValidationError(self.VALIDATION_ERROR_MSG)
        return val

    """ used to craete and update directly using this serializer """
    def create(self, validated_data):
        return AlarmSchedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.minute = validated_data.get("minute", instance.minute)
        instance.hour = validated_data.get("hour", instance.hour)
        instance.day_of_week = validated_data.get("day_of_week",
                                                  instance.day_of_week)
        instance.command = validated_data.get("command", instance.command)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance
