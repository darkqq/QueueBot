lessons = {}
queue = {}


def add_person(name, position, lesson):
    queue[str(position)] = str(name)
    for les in lessons:
        if les == lesson:
            lessons[les] = queue
        else:
            lessons[lesson] = queue


def get_queue():
    return lessons

