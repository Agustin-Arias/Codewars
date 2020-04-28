# The Hashtag Generator
# https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s):
    if s == '':
        return False
    string = '#'
    for word in s.split():
        string += word.capitalize()
    if len(string) > 140:
        return False
    else:
        return string
