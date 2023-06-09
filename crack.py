from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Teacher
from datacenter.models import Subject
from datacenter.models import Commendation
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
import random

GOOD_RECORDS = [
    'Красавчег',
    'Молодец',
    'Один из лучших ответов',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Tалантливо!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!']


def get_kid(name):
    try:
        kids = Schoolkid.objects.all()
        return kids.get(full_name__contains=name)
    except MultipleObjectsReturned:
        print(f"Скрипт нашел сразу несколько таких учеников {name}. Исправления не возможны")
        return False
    except ObjectDoesNotExist as DoesNotExist:
        print(f"Ученика с таким именем {name} не существует")
        return False


def change_mark(name):
    kid = get_kid(name)
    if (kid):
        kid_marks = Mark.objects.filter(schoolkid=kid, points__in=[2, 3])
        kid_marks.select_related('id').update(points=5)
        print("Плохие оценки исправлены")


def remove_chastisements(name):
    kid = get_kid(name)
    if (kid):
        Chastisement.objects.filter(schoolkid=kid).delete()
        print(f"Все замечания для ученика {name} удалены")


def create_commendation(name, lesson):
    """ crack.create_commendation('Фролов Иван', 'Музыка') """
    kid = get_kid(name)
    if (kid):
        lesson_kid = Lesson.objects.filter(year_of_study=kid.year_of_study, group_letter=kid.group_letter, subject__title__contains=lesson).order_by('-date').first()
        Commendation.objects.create(text=random.choice(GOOD_RECORDS), created=lesson_kid.date,
                                    subject=lesson_kid.subject, teacher=lesson_kid.teacher, schoolkid=kid)
        print(f"Успешно добавил запись для {name}, хороший отзыв проставлен в предмете {lesson}")