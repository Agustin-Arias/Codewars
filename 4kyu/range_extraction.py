# Range Extraction
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    result = []
    index = 0
    while index < len(args):
        number = args[index]
        num = number
        counter = index
        while counter < len(args) and args[counter] == num:
            num += 1
            counter += 1
        if counter == index + 1:  # this means theres not a range present
            result.append(str(number))
        elif counter == index + 2:  # a range is present but it is not long enough
            result.append(str(number))
            result.append(str(number + 1))
        else:  # range >= 3
            result.append(str(number) + '-' + str(args[counter-1]))
        index += counter -index - 1
        index += 1
    return ','.join(result)
