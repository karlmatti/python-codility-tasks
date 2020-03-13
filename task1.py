def solution(S, K):
    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    current_day = week_days.index(S)
    index = K%7 + current_day
    if index > 6:
        index -= 7

    return week_days[index]

print(solution("Sat", 23))
