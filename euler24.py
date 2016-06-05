def next_permutation(remaining, computed, perm, target):
    if len(remaining) == 0:
        return (perm + 1, computed)

    r_list = sorted(list(remaining))

    for i, x in enumerate(r_list):
        perm, answer = next_permutation(remaining - set([x]), computed + [x], perm, target)

        if perm == target:
            return perm, answer

    return perm, answer

a = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

perm, answer = next_permutation(a, [], 0, 1000000)

print "".join([str(x) for x in answer])

