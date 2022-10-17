def add_lesson(add_command):
    global initial_lessons
    lesson = add_command[1]
    if lesson not in initial_lessons:
        initial_lessons.append(lesson)


def insert_lesson(inset_command):
    global initial_lessons
    lesson = inset_command[1]
    idx = int(inset_command[2])
    if lesson not in initial_lessons:
        initial_lessons.insert(idx, lesson)


def remove_lesson(remove_command):
    global initial_lessons
    lesson = remove_command[1]
    if lesson in initial_lessons:
        initial_lessons.remove(lesson)
        if lesson + '-Exercise' in initial_lessons:
            initial_lessons.remove(lesson + '-Exercise')


def swap_lessons(swap_command):
    """
    Swap the position of the two lessons if they exist, should do the same with the Exercises,
    if there are any following the lessons.
    :param swap_command: take its values from current_command
    :return: initial_lesson as a global
    """
    global initial_lessons
    # take values of first and second lessons from swap_command
    lesson_one = swap_command[1]
    lesson_two = swap_command[2]
    # if both lessons are in initial_lessons;
    # take indexes of both lessons and swap them by their indexes
    if lesson_one in initial_lessons and lesson_two in initial_lessons:
        idx_first = initial_lessons.index(lesson_one)
        idx_second = initial_lessons.index(lesson_two)
        initial_lessons[idx_first], initial_lessons[idx_second] = \
            initial_lessons[idx_second], initial_lessons[idx_first]
        # if the first lesson has an exercise
        # take index of first lesson with exercise; pop his value from initial_lessons list;
        # insert the value after new position of first lesson
        if lesson_one + '-Exercise' in initial_lessons:
            exercise_idx = initial_lessons.index(lesson_one + '-Exercise')
            exercise_swap = initial_lessons.pop(exercise_idx)
            initial_lessons.insert(idx_second + 1, exercise_swap)
        # if the second lesson has an exercise
        # take index of second lesson with exercise; pop his value from initial_lessons list;
        # insert the value after new position of second lesson
        if lesson_two + '-Exercise' in initial_lessons:
            exercise_idx = initial_lessons.index(lesson_two + '-Exercise')
            exercise_swap = initial_lessons.pop(exercise_idx)
            initial_lessons.insert(idx_first + 1, exercise_swap)


def add_exercise(exercise_command):
    """
    Add Exercise in the schedule right after the lesson index, if the lesson exists and there is no exercise already,
    in the following format "{lesson}-Exercise". If the lesson doesn't exist, add the lesson at the end of the
    course schedule, followed by the Exercise.
    :param exercise_command: take its values from current_command
    :return: initial_lesson as a global
    """
    global initial_lessons
    lesson = exercise_command[1]
    # if the lesson exist but no exercise
    # take the index of lesson and insert exercise on next index
    if lesson in initial_lessons and lesson + '-Exercise' not in initial_lessons:
        lesson_idx = initial_lessons.index(lesson)
        initial_lessons.insert(lesson_idx + 1, lesson + '-Exercise')
    # if the lesson does not exist
    # add lesson in the end of initial_lessons
    # add exercise after new lesson
    elif lesson not in initial_lessons:
        initial_lessons.append(lesson)
        initial_lessons.append(lesson + '-Exercise')


initial_lessons = input().split(', ')

while True:
    command = input()
    if command == 'course start':
        break

    current_command = command.split(':')
    event = current_command[0]

    if event == 'Add':
        add_lesson(current_command)
    elif event == 'Insert':
        insert_lesson(current_command)
    elif event == 'Remove':
        remove_lesson(current_command)
    elif event == 'Swap':
        swap_lessons(current_command)
    elif event == 'Exercise':
        add_exercise(current_command)

for number, lesson_title in enumerate(initial_lessons):
    print(f'{number + 1}.{lesson_title}')
