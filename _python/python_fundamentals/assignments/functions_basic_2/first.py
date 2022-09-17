1


def countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList


print(countDown(5))

2


def print_return(list):
    print(list[0])
    return list[1]


print(print_return([1, 2]))

3


def first_plus_length(list):
    return list[0] + len(list)


print(first_plus_length([1, 2, 3, 4, 5]))

4


def greater_than_second(list):
    # if len(list) < 2:
    #     return False
    newList = []
    for i in list:
        if i > list[1]:
            return newList.append(list[i])


print(greater_than_second([5, 2, 3, 2, 1, 4]))


# 5
def length_and_value(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList


print(length_and_value(3, 8))
