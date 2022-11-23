def take(first):
    """
    The received number represents the number of elements you have to take from the list (starting from the first one).
    :param first: int
    """
    global integers_list
    integers_list = integers_list[:first]


def delete(second):
    """
    The received number represents the number of elements you have to delete from
    the numbers you took (starting from the first one).
    :param second: int
    """
    global integers_list
    integers_list = integers_list[second:]


def collection(third):
    """
    The received number is the number we search in our collection after the manipulations.
    :param third: int
    """
    global integers_list
    integers_list = [x for x in integers_list if x == third]


def output():
    """
    If searched number presents in integers_list returns: “YES!”, otherwise print “NO!”.
    :return:
    """
    global integers_list
    if integers_list:
        return 'YES!'
    return 'NO!'


integers_list = [int(x) for x in input().split()]
first_num, second_num, third_num = input().split()

take(int(first_num))
delete(int(second_num))
collection(int(third_num))
print(output())
