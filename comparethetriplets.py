def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1
    li =[alice,bob]
    return li