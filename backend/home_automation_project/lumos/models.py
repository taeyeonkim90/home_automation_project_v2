from django.db import models
from rest_framework import serializers


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
    command = models.CharField(default="ls", max_length=100)


class AlarmScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    minute = serializers.CharField(max_length=100)
    hour = serializers.CharField(max_length=100)
    day_of_week = serializers.CharField(max_length=100)
    command = serializers.CharField(max_length=100)

    def validate_minute(self, val):
        minutes = [str(x) for x in range(0, 61)]
        minutes.append("*")
        if val not in minutes:
            raise serializers.ValidationError("Invalid input for scheduling an \
                                              alarm task")
        return val

    def validate_hour(self, val):
        hours = [str(x) for x in range(0, 25)]
        hours.append("*")
        if val not in hours:
            raise serializers.ValidationError("Invalid input for scheduling an \
                                              alarm task")
        return val
    
    def validate_day_of_week(self, val):
        days = [str(x) for x in range(0, 7)]
        days.append("*")
        if val not in days:
            raise serializers.ValidationError("Invalid input for scheduling an \
                                              alarm task")
        return val
    
    def create(self, validated_data):
        return AlarmSchedule.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.minute = validated_data.get("minute", instance.minute)
        instance.hour = validated_data.get("hour", instance.hour)
        instance.day_of_week = validated_data.get("day_of_week", 
                                                  instance.day_of_week)
        instance.command = validated_data.get("command", instance.command)
        instance.save()
        return instance