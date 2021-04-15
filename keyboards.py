import json
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

program1_btn = InlineKeyboardButton('Первая программа', callback_data='program1')
program2_btn = InlineKeyboardButton('Вторая программа', callback_data='program2')
program3_btn = InlineKeyboardButton('Третья программа', callback_data='program3')
program4_btn = InlineKeyboardButton('Четвертая программа', callback_data='program4')
program5_btn = InlineKeyboardButton('Первая программа', callback_data='program5')
program = InlineKeyboardMarkup(row_width=1)
program.row(program1_btn)
program.row(program2_btn)
program.row(program3_btn)
program.row(program4_btn)
program.row(program5_btn)


# i = 1


def weekday_number(weekday):
    if weekday == 'Понедельник':
        return 0
    elif weekday == 'Вторник':
        return 1
    elif weekday == 'Среда':
        return 2
    elif weekday == 'Четверг':
        return 3
    elif weekday == 'Пятница':
        return 4
    elif weekday == 'Суббота':
        return 5
    else:
        return -1


# group_number = '921703'
# weekday = '0'
# week_number = '1'


def convert_to_bsuir_week(week_number):
    if 3 <= int(week_number) <= 4:
        # difference between normal and bsuir week number(2 is a magic number)
        bsuir_week_number = int(week_number) - 2
        return bsuir_week_number
    elif 1 <= int(week_number) <= 2:
        return int(week_number) + 2
    elif int(week_number) < 1:
        print(f"You're trying to convert incorrect week number({week_number})!")
    else:
        return convert_to_bsuir_week(int(week_number) - 4)


def get_lessons(group_number, weekday, week_number):
    subjects = InlineKeyboardMarkup(row_width=1)
    with open(str(group_number) + '.json') as json_file:
        data = json.load(json_file)
        # weekNumber = data['currentWeekNumber']
        # print(weekNumber)
        for schedules in data['schedules']:
            # print(schedules['weekDay'])
            i = 1
            if weekday_number(schedules['weekDay']) == weekday:
                for lesson in schedules['schedule']:
                    if week_number in lesson['weekNumber']:
                        lesson_btn = InlineKeyboardButton(
                            str(i) + ". " + lesson['subject'] + " (" + lesson['lessonType'] + ")",
                            callback_data="lesson" + lesson['subject'] + " (" + lesson['lessonType'] + ")")
                        subjects.add(lesson_btn)
                        i += 1
    return subjects


# with open('921703.json') as json_file:
#     data = json.load(json_file)
#     for lesson in data['todaySchedules']:
#         lesson_btn = InlineKeyboardButton(str(i) + ". " + lesson['subject'] + " (" + lesson['lessonType'] + ")",
#                                           callback_data="lesson" + lesson['subject'] + " (" + lesson['lessonType'] + ")")
#         subjects.add(lesson_btn)
#         # print(str(i) + ". " + lesson['subject'] + " (" + lesson['lessonType'] + ")")
#         i += 1


recall_yes = InlineKeyboardButton('Да', callback_data='recall_yes')
recall_no = InlineKeyboardButton('Нет', callback_data='recall_no')
recall = InlineKeyboardMarkup(row_width=2)
recall.row(recall_yes, recall_no)
