from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


from .models import AlarmSchedule, AlarmScheduleSerializer
from .services import AlarmService


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
    def setUp(self):
        self.alarm_service = AlarmService()

    def test_create(self):
        """ Tests AlarmService.create() """
        # positive case
        target_string = "positive case"
        json = JSONGenerator.get_alarm(command=target_string)
        data = JSONGenerator.json_to_data(json)
        result = self.alarm_service.create(data)
        self.assertTrue(result.success)

        target_model = AlarmSchedule.objects.get(command=target_string)
        self.assertEqual(target_string, target_model.command)

        # negative case
        target_string = "negative case"
        json = JSONGenerator.get_alarm(hour="25", command=target_string)
        data = JSONGenerator.json_to_data(json)
        result = self.alarm_service.create(data)
        self.assertFalse(result.success)

        try:
            target_model = AlarmSchedule.objects.get(command=target_string)
            self.fail()
        except AlarmSchedule.DoesNotExist:
            pass

    def test_read(self):
        """ Tests AlarmService.read() """
        # positive case
        model = AlarmSchedule()
        model.save()
        target_id = model.id

        result = self.alarm_service.read(target_id)
        self.assertTrue(result.success)
        self.assertEqual(result.data["id"], target_id)

        # negative case
        result = self.alarm_service.read(3000)
        self.assertFalse(result.success)

    def test_read_all(self):
        # empty case
        result = self.alarm_service.read_all()
        self.assertEqual(len(result.data), 0)

        # create two instances
        model_1 = AlarmSchedule()
        model_2 = AlarmSchedule()
        model_1.save()
        model_2.save()

        result = self.alarm_service.read_all()
        self.assertTrue(result.success)
        self.assertEqual(len(result.data), 2)

    def test_update(self):
        original_command = "foo"
        model = AlarmSchedule(command=original_command)
        model.save()
        self.assertEqual(original_command, model.command)

        # positive case
        target_id = model.id
        new_command = "bar"
        json = JSONGenerator.get_alarm(command=new_command)
        data = JSONGenerator.json_to_data(json)
        result = self.alarm_service.update(data, target_id)

        self.assertTrue(result.success)
        self.assertNotEqual(original_command, result.data["command"])

        # negative case
        result = self.alarm_service.update(data, 9999)
        self.assertFalse(result.success)

    def test_delete(self):
        model = AlarmSchedule()
        model.save()
        target_id = model.id
        target_model = AlarmSchedule.objects.get(id=target_id)
        self.assertEqual(target_model.id, target_id)

        # positive case
        result = self.alarm_service.delete(target_id)
        self.assertTrue(result.success)

        # negative case
        result = self.alarm_service.delete(target_id)
        self.assertFalse(result.success)
