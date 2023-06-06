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

def change_mark():
    kids = Schoolkid.objects.all()
    kid_ivan = kids.get(full_name__contains='Фролов Иван')
    ivan_marks = Mark.objects.filter(schoolkid=kid_ivan)
    print(ivan_marks)
    ivan_marks = Mark.objects.filter(schoolkid=kid_ivan, points__in=[2, 3])
    ivan_marks.filter().values_list("id")
    for bad_marks in ivan_marks.filter().values_list("id"):
        Mark.objects.filter(id=bad_marks[0]).update(points=5)
    print("Плохие оценки исправлены")


def remove_chastisements():
    kids = Schoolkid.objects.all()
    kid = kids.get(full_name__contains='Фролов Иван')
    Chastisement.objects.filter(schoolkid=kid).delete()
    print("Все замечания удалены")


def create_commendation(name, lesson): #'Фролов Иван', 'Музыка'
    good_records = [
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
    try:
        kids = Schoolkid.objects.all()
        kid = kids.get(full_name__contains=name)
        lesson_kid = Lesson.objects.filter(year_of_study='6', group_letter = 'А', subject__title__contains=lesson).order_by('-date').first()
        teachers = Teacher.objects.all()
        teacher = teachers.get(full_name__contains=lesson_kid.teacher)
        predmeti = Subject.objects.all()
        predmet = predmeti.get(title=lesson, year_of_study=6)
        Commendation.objects.create(text=random.choice(good_records), created=lesson_kid.date, subject=predmet, teacher=teacher, schoolkid=kid)
        print(f"Успешно добавил запись для {name}, хороший отзыв проставлен в предмете {lesson}")
    except MultipleObjectsReturned :
        print(f"Скрипт нашел сразу несколько таких учеников {name}. Исправления не возможны")
    except ObjectDoesNotExist:
        print(f"Ученика с таким именем {name} не существует")
