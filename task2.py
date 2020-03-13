def solution(S):
    counter = 0
    if "aaa" in S:
        return -1
    prev_double_a = False
    for position in range(1, len(S)-1):
        if "aa" == S[position-1]+S[position]:
            prev_double_a = True
        elif "a" in S[position-1]+S[position]:
            if prev_double_a == True:
                pass
            elif S[position]+S[position+1]:
                counter += 1
            prev_double_a = False
    if S[len(S)-1] != "a":
        counter += 2
    return counter

print(solution("aabab")) # 8
print(solution("dog")) # -1
print(solution("aa")) # 0
print(solution("baaa")) # 3
print("abcd"[-2:])