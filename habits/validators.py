from rest_framework.serializers import ValidationError
from datetime import timedelta


def validator_for_habit(value):
    """ Проверка на правильность заполнения полей привычки """

    time = timedelta(minutes=2)

    if value['habit_is_good']:
        if value['connected_habit'] or value['prize']:
            raise ValidationError('У приятной привычки не может быть связанной привычки или вознаграждения')

    if value['connected_habit'] and value['prize']:
        raise ValidationError('Можно выбрать или приятную привычку или вознаграждение')

    if value['duration'] > time:
        raise ValidationError('Привычку можно выполнять не более 2 минут')

    if value['connected_habit']:
        if not value['connected_habit'].habit_is_good:
            raise ValidationError('В связанные привычки могут попадать только приятные привычки')
