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


def get_student(name):
    try:
        students = Schoolkid.objects.all()
        return students.get(full_name__contains=name)
    except MultipleObjectsReturned:
        print(f"Скрипт нашел сразу несколько таких учеников {name}. Исправления не возможны")
        return False
    except ObjectDoesNotExist:
        print(f"Ученика с таким именем {name} не существует")
        return False


def change_mark(name):
    student = get_student(name)
    if (student):
        Mark.objects.filter(schoolkid=student, points__in=[2, 3]).update(points=5)
        print("Плохие оценки исправлены")


def remove_chastisements(name):
    student = get_student(name)
    if (student):
        Chastisement.objects.filter(schoolkid=student).delete()
        print(f"Все замечания для ученика {name} удалены")


def create_commendation(name, lesson):
    """ crack.create_commendation('Фролов Иван', 'Музыка') """
    student = get_student(name)
    if (student):
        student_lesson = Lesson.objects.filter(year_of_study=student.year_of_study, group_letter=student.group_letter, subject__title__contains=lesson).order_by('-date').first()
        if(student_lesson):
            Commendation.objects.create(text=random.choice(GOOD_RECORDS), created=student_lesson.date,
                                        subject=student_lesson.subject, teacher=student_lesson.teacher, schoolkid=student)
            print(f"Успешно добавил запись для {name}, хороший отзыв проставлен в предмете {lesson}")
        else:
            print(f"Нет такого урока {lesson}!")