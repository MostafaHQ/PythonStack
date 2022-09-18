# 1
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list


print(biggie_size([-1, 3, 5, -5]))

# 2


def count_positive(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list


print(count_positive([-1, 1, 1, 1]))

# 3


def sum_total(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


print(sum_total([1, 2, 3, 4]))

# 4


def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)


print(average([1, 2, 3, 4]))

# 5


def length(list):
    return len(list)


print(length([37, 2, 1, -9]))
print(length([]))

# 6


def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for i in list:
        if i < list[0]:
            min = i

    return min


print(minimum([37, 2, 1, -9]))
print(minimum([]))

# 7


def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for i in list:
        if i > list[0]:
            max = i

    return max


print(maximum([37, 2, 1, -9]))
print(maximum([]))

# 8


def ultimate_analysis(list):
    myDictionary = {'sumTotal': 0, 'avaeage': 0,
                    'maximum': list[0], 'minimum': list[0], 'length': 0}
    for i in list:
        if myDictionary['maximum'] < i:
            myDictionary['maximum'] = i

        if myDictionary['minimum'] > i:
            myDictionary['minimum'] = i

        myDictionary['sumTotal'] += i

        myDictionary['avaeage'] = myDictionary['sumTotal'] / len(list)

        myDictionary['length'] = len(list)

    return myDictionary


print(ultimate_analysis([37, 2, 1, -9]))


# 9
def reverse_list(list):
    for i in range(0, (len(list)-1)//2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list


print(reverse_list([37, 2, 1, -9]))
