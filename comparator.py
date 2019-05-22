import objects


def find_close(previous_marked_object, actual):
    status = -1
    for now_marked_object in actual:
        if (now_marked_object.class_id == previous_marked_object.class_id):
            previous_position = previous_marked_object.get_position()
            actual_position = now_marked_object.get_position()
            if(abs(actual_position - previous_position) / previous_position < 0.1):
                return 1
            elif (abs(actual_position - previous_position) / previous_position < 0.3):
                status = 0
    return status



def compare_objects_lists(previous, actual):
    if (len(previous) > len(actual)):
        return "Danger"
    moved = 0
    for marked_object in previous:
        finding_result = find_close(marked_object, actual)
        if (finding_result == 0):
            moved += 1
        elif (finding_result == -1):
            return "Danger"
        if (moved == 3):
            return "Warning"
        return "OK"