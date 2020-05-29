import re
def alphanumeric(password): return password != '' and not bool(re.match('.*[^A-Za-z0-9].*', password))
