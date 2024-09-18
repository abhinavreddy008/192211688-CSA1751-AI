from itertools import permutations
def solve_cryptarithmetic():
    letters = 'SENDMORY'
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']
        if send + more == money:
            print(f"Solution found: {mapping}")
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
solve_cryptarithmetic()
