from celery import shared_task
from config import settings
from habit.models import Habit
import requests

telegram_bot_api_token = settings.TELEGRAM_BOT_API_TOKEN
chat_id = settings.CHAT_ID


@shared_task
def send_telegram_message(habit_id):

    habit = Habit.objects.get(id=habit_id)

    message = {f"Полезная привычка {habit.user.telegram_username} \n"
               f"Я буду {habit.action} в {habit.place} Время: {habit.time}"}

    url = f"https://api.telegram.org/bot{telegram_bot_api_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    response = requests.get(url, params=params)
    return response
