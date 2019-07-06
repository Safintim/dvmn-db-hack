from .models import Schoolkid, Mark, Сhastisement, Commendation, Lesson
import random


def fix_marks(schoolkid_name):
    bad_marks_child = Mark.objects.all().filter(
        schoolkid__full_name=schoolkid_name,
        points__in=[2, 3])
    if bad_marks_child:
        for mark in bad_marks_child:
            mark.points = random.randint(4, 5)
            mark.save()
    return bad_marks_child


def remove_сhastisements(schoolkid_name):
    return Сhastisement.objects.all().filter(schoolkid__full_name=schoolkid_name).delete()


def make_commendation(schoolkid_name, subject):
    try:
        commendations = [
            'Молодец!',
            'Отлично!',
            'Гораздо лучше, чем я ожидал!',
            'Ты меня приятно удивил!',
            'Именно этого я давно ждал от тебя!',
            'С каждым разом у тебя получается всё лучше!',
            'Я вижу, как ты стараешься!',
            'Это как раз то, что нужно!',
            'Уже существенно лучше!',
            'Очень хороший ответ!',
            'Я поражен!',
            'Здорово!'
        ]
        child = Schoolkid.objects.all().get(full_name=schoolkid_name)
        exist_commendation = [c.created for c in Commendation.objects.all().filter(
                                                                    schoolkid=child,
                                                                    subject__title=subject)]
        lessons_child = Lesson.objects.all().filter(
            year_of_study=child.year_of_study,
            group_letter=child.group_letter,
            subject__title=subject
        ).exclude(date__in=exist_commendation)
        if lessons_child:
            lesson = lessons_child[0]
            return Commendation.objects.create(
                        text=random.choice(commendations),
                        created=lesson.date,
                        schoolkid=child,
                        subject=lesson.subject,
                        teacher=lesson.teacher
                    )
    except Schoolkid.DoesNotExist:
        ...
