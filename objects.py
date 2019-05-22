import time

import comparator
from detector import mark_objects

N = 100

previous_objects = None


class MarkedObject:
    def __init__(self, class_id, x1, y1, x2, y2):
        self.class_id = int(class_id)
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.y1 = float(y1)
        self.y2 = float(y2)

    def get_position(self):
        return self.x1 + self.x2 + self.y1 + self.y2


def detect_objects():
    global previous_objects
    while (True):
        marked_objects = mark_objects()
        time.sleep(N)
        if (not previous_objects):
            previous_objects = marked_objects
        else:
            print(comparator.compare_objects_lists(previous_objects, marked_objects))


detect_objects()
