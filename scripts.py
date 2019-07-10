from datacenter.models import Schoolkid, Mark, Сhastisement, Commendation, Lesson
import random


def is_exist_schoolkid(schoolkid_name):
    schoolkids = Schoolkid.objects.filter(full_name=schoolkid_name)
    if not schoolkids or len(schoolkids) > 2:
        print(f'По вашему запросу <{schoolkid_name}> найдено {len(schoolkids)} записей')
        return False
    return schoolkids[0]


def fix_marks(schoolkid_name):
    schoolkid = is_exist_schoolkid(schoolkid_name)
    if schoolkid:
        bad_marks_child = Mark.objects.filter(
            schoolkid=schoolkid,
            points__in=[2, 3])
        if bad_marks_child:
            for mark in bad_marks_child:
                mark.points = random.randint(4, 5)
                mark.save()
        return bad_marks_child


def remove_сhastisements(schoolkid_name):
    schoolkid = is_exist_schoolkid(schoolkid_name)
    if schoolkid:
        return Сhastisement.objects.filter(schoolkid=schoolkid).delete()


def make_commendation(schoolkid_name, subject):
    schoolkid = is_exist_schoolkid(schoolkid_name)
    if schoolkid:
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
        exist_commendation = [c.created for c in Commendation.objects.filter(
                                                                        schoolkid=schoolkid,
                                                                        subject__title=subject)]
        child_lessons = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject
        ).exclude(date__in=exist_commendation)
        if child_lessons:
            lesson = child_lessons[0]
            return Commendation.objects.create(
                        text=random.choice(commendations),
                        created=lesson.date,
                        schoolkid=schoolkid,
                        subject=lesson.subject,
                        teacher=lesson.teacher
                    )
