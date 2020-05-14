# The Hashtag Generator
# https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s):
    if s == "":
        return False
    string = "#" + "".join([word.lower().capitalize() for word in s.split(" ")])
    return false if len(string) > 140 else string

