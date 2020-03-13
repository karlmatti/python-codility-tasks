def solution(A):
    numbers = set(A)
    for i in range(1, 100000):
        if i not in numbers:
            return i

