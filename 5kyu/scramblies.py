# Scramblies
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
def scramble(s1, s2):
    dic = {}
    for letter in s2:
        dic.setdefault(letter, 0)
        dic[letter] += 1

    for letter, num in dic.items():
        if num > s1.count(letter):
            return False
    return True
