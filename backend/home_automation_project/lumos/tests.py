from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


from .models import AlarmSchedule, AlarmScheduleSerializer


class AlarmTestCase(TestCase):
    def test_alarm_serializer(self):
        """Test Django REST serializer. Model -> JSON"""
        model = AlarmSchedule(minute="*", hour="*", day_of_week="*")
        serializer = AlarmScheduleSerializer(model)
        json = JSONRenderer().render(serializer.data)
        expected_json = b'{"minute":"*","hour":"*","day_of_week":"*",\
                          "command":"ls"}'
        self.assertEqual(json, expected_json)
    
    def test_alarm_deserializer(self):
        """Test Django REST serializer. JSON -> Model"""
        # positive case
        json = b'{"minute":"1","hour":"2","day_of_week":"3","command":"ls"}'
        stream = BytesIO(json)
        data = JSONParser().parse(stream)

        serializer = AlarmScheduleSerializer(data=data)
        self.assertTrue(serializer.is_valid(), 
                        "Serializer validation has failed")

        model = AlarmSchedule(**serializer.data)
        self.assertEqual(model.minute, "1")
        self.assertEqual(model.hour, "2")
        self.assertEqual(model.day_of_week, "3")

        # negative case
        json = b'{"minute":"-1","hour":"25","day_of_week":"8","command":"ls"}'
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        
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
