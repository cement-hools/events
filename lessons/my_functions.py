from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
    """Права доступа для групп."""

    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)


def lessons_in_json(lessons):
    lesson_arr = []
    for lesson in lessons:
        lesson_sub_arr = dict()
        lesson_sub_arr['id'] = lesson.id
        lesson_sub_arr['title'] = lesson.title
        lesson_sub_arr['start'] = str(lesson.start_date)
        lesson_sub_arr['end'] = str(lesson.end_date)
        lesson_arr.append(lesson_sub_arr)
    return lesson_arr
