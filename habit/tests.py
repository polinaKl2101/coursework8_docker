from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test_user@mail.ru',
            password='12345U'
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place='Парк',
            time="08:30:00",
            action='Пробежка с собакой',
            periodicity=4,
            execution_time=60,
            pleasant_habit=True
        )

    def test_create_habit(self):

        self.client.force_authenticate(user=self.user)

        data = {
            'user': self.user.id,
            'place': 'Улица',
            'time': '14:00:00',
            'action': 'Прогулка',
            'periodicity': 4,
            'execution_time': 40,
            'pleasant_habit': True,
        }

        response = self.client.post(
            reverse('habit:create_habit'),
            data, format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)

    def test_list_habit(self):

        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('habit:list_habit'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):

        self.client.force_authenticate(user=self.user)

        test_data_fixed = {'place': 'Дом'}

        response = self.client.patch(
            reverse('habit:update_habit', args=[self.habit.id]),
            data=test_data_fixed
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['place'],
            'Дом'
        )

    def test_delete_habit(self):

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('habit:delete_habit',
                    args=[self.habit.id])
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT)
