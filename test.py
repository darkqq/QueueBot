# -------------------get json into file------------------------------
# schedule = schedule.api.get_schedule("920601")
# print(schedule)
# with open('920601.json', 'w') as outfile:
#     json.dump(schedule, outfile, ensure_ascii=False)
# -------------------get json into file------------------------------
import lesson_queue
import json

for i in range(10):
    lesson_queue.add_person('Vander', i, 'ППвИС')

lesson_queue.add_person('Penis', 10, 'ППвИс')

queue = lesson_queue.get_queue()
print(queue)
with open('queue.json', 'w') as outfile:
    json.dump(queue, outfile, ensure_ascii=False)
