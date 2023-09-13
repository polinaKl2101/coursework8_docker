from rest_framework import serializers

from habit.validators import validate_time, validate_periodicity, validate_habit
from users.models import User
from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    execution_time = serializers.IntegerField(validators=[validate_time])
    periodicity = serializers.IntegerField(validators=[validate_periodicity])
    linked_habit = serializers.PrimaryKeyRelatedField(queryset=Habit.objects.all(), required=False,
                                                      validators=[validate_habit])

    class Meta:
        model = Habit
        fields = '__all__'
