# GCD
import fractions

# This function generates all the generators and finds the smallest one
# function definition
def gens(start, n):
    # collect values to return
    return_list = []
    # form list to compare to
    t = [_ for _ in range(n)]
    t = list(filter(lambda x: fractions.gcd(x, n) == 1, t))
    # go v = start ... n
    for v in range(start, n):
        # form list
        lst = {(pow(v, x) % n) for x in range(len(t) + 1) if x != 0}
        # check
        if lst == set(t):
            return_list.append(v)
            print(return_list)
    # return
    return return_list

# print
print(gens(1000, 4969)[0])
# print(len(gens(1000, 4969)))
