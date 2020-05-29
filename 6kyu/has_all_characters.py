def regex_contains_all(st):
    conditional = '('+ '|'.join(set(st)) + ')'
    pattern = f'.*{conditional}' * len(set(st)) + '.*'
    return pattern

st = 'abc'
print(''.join(f'(?=.*{x})' for x in set(st)))
