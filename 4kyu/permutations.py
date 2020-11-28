# Permutations
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/python
def permutations(s):
    if len(s) == 0:
        return [s]
    else:
        list_of_perms = set()
        i = 0
        while i < len(s):
            char = s[i]
            list_of_perms = list_of_perms.union({char + perm for perm in permutations(s[0:i] + s[i+1:])})
            i+=1
        return list(list_of_perms)

string = "aabb"
print(permutations(string))
