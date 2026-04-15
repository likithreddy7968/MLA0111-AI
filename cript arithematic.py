import itertools

def solve_cryptarithm():
    # Example: SEND + MORE = MONEY
    letters = 'SENDMORY'
    digits = '0123456789'

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if mapping['S'] == '0' or mapping['M'] == '0':
            continue

        send = int("".join(mapping[c] for c in "SEND"))
        more = int("".join(mapping[c] for c in "MORE"))
        money = int("".join(mapping[c] for c in "MONEY"))

        if send + more == money:
            print("Solution found:")
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print(mapping)
            return

    print("No solution found.")

solve_cryptarithm()
