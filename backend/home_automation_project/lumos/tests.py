from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


from .models import AlarmSchedule, AlarmScheduleSerializer


class JSONGenerator:
    @classmethod
    def get_alarm(cls, minute="*", hour="*", day_of_week="*", command="*"):
        template = '{{"id":null,"minute":"{}","hour":"{}",' + \
                      '"day_of_week":"{}","command":"{}"}}'
        formatted = template.format(minute, hour, day_of_week, command)
        return formatted.encode()

    @classmethod
    def json_to_data(cls, json):
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        return data


class AlarmTestCase(TestCase):
    def test_alarm_serializer(self):
        """Test Django REST serializer. Model -> JSON"""
        model = AlarmSchedule(minute="*", hour="*", day_of_week="*")
        serializer = AlarmScheduleSerializer(model)
        json = JSONRenderer().render(serializer.data)
        expected_json = JSONGenerator.get_alarm(command="ls")
        self.assertEqual(json, expected_json)

    def test_alarm_deserializer(self):
        """Test Django REST serializer. JSON -> Model"""
        # positive case
        json = JSONGenerator.get_alarm("1", "2", "3", "ls")
        data = JSONGenerator.json_to_data(json)

        serializer = AlarmScheduleSerializer(data=data)
        self.assertTrue(serializer.is_valid(),
                        "Serializer validation has failed")

        model = AlarmSchedule(**serializer.data)
        self.assertEqual(model.minute, "1")
        self.assertEqual(model.hour, "2")
        self.assertEqual(model.day_of_week, "3")

        # negative case
        json = JSONGenerator.get_alarm("-1", "25", "8", "ls")
        data = JSONGenerator.json_to_data(json)

        serializer = AlarmScheduleSerializer(data=data)
        self.assertFalse(serializer.is_valid(),
                         "Serializer validation has failed")


class AlarmSericeTestCase(TestCase):
    def test_create(self):
        pass

    def test_read(self):
        pass

    def test_read_all(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass
