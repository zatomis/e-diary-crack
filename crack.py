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


def change_mark(name):
    try:
        kids = Schoolkid.objects.all()
        kid = kids.get(full_name__contains=name)
        kid_marks = Mark.objects.filter(schoolkid=kid)
        kid_marks = Mark.objects.filter(schoolkid=kid, points__in=[2, 3])
        kid_marks.select_related('id').update(points=5)
        print("Плохие оценки исправлены")
    except MultipleObjectsReturned:
        print(f"Скрипт нашел сразу несколько таких учеников {name}. Исправления не возможны")
    except ObjectDoesNotExist as DoesNotExist:
        print(f"Ученика с таким именем {name} не существует")



def remove_chastisements(name):
    try:
        kids = Schoolkid.objects.all()
        kid = kids.get(full_name__contains=name)
        Chastisement.objects.filter(schoolkid=kid).delete()
        print(f"Все замечания для ученика {name} удалены")
    except MultipleObjectsReturned:
        print(f"Скрипт нашел сразу несколько таких учеников {name}. Исправления не возможны")
    except ObjectDoesNotExist as DoesNotExist:
        print(f"Ученика с таким именем {name} не существует")


def create_commendation(name, lesson):
    """ 'Фролов Иван', 'Музыка' """
    try:
        kids = Schoolkid.objects.all()
        kid = kids.get(full_name__contains=name)
        lesson_kid = Lesson.objects.filter(year_of_study=kid.year_of_study, group_letter=kid.year_of_study, subject__title__contains=lesson)
        lesson_kid.order_by('-date').first()
        teachers = Teacher.objects.all()
        teacher = teachers.get(full_name__contains=lesson_kid.teacher)
        lessons = Subject.objects.all()
        lesson_kid = lessons.get(title=lesson, year_of_study=kid.year_of_study)
        Commendation.objects.create(text=random.choice(GOOD_RECORDS), created=lesson_kid.date,
                                    subject=lesson_kid, teacher=teacher_id, schoolkid=kid)
        print(f"Успешно добавил запись для {name}, хороший отзыв проставлен в предмете {lesson}")
    except MultipleObjectsReturned:
        print(f"Скрипт нашел сразу несколько таких учеников {name}. Исправления не возможны")
    except ObjectDoesNotExist as DoesNotExist:
        print(f"Ученика с таким именем {name} не существует")

