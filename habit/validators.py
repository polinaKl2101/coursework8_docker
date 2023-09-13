from rest_framework import serializers


def validate_habit(data):
    if data.get('linked_habit') and data.get('reward'):
        raise serializers.ValidationError('Одновременный выбор связанной привычки и вознаграждения невозможен')
    elif data.get('pleasant_habit') and (data.get('reward') is not None):
        raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
    elif data.get('pleasant_habit') and (data.get('linked_habit') is not None):
        raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

    return data


def validate_periodicity(data):
    if data < 7:
        raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


def validate_pleasant_habit(data):

    if data.get('pleasant_habit') is False:
        raise serializers.ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


def validate_time(data):
    if data > 120:
        raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд.')
