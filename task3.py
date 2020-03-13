def solution(N):
    string = str(N)
    if "-" in string:
        number = string[1:]
        bigger_number = -int(getSmallerNumber(number))
    else:
        bigger_number = int(getBiggerNumber(string[:]))
    return bigger_number


def getBiggerNumber(number_string):
    for x in range(len(number_string)):
        if int(number_string[x]) < 5:
            return number_string[:x] + '5' + number_string[x:]
    return number_string + '5'
def getSmallerNumber(number_string):
    for x in range(len(number_string)):
        if int(number_string[x]) > 5:
            return number_string[:x] + '5' + number_string[x:]
    return '5' + number_string

print(solution(-999))
print(solution(0))
print(solution(670))
