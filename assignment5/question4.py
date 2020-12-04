
def TotalDifferentDonations(D, L, donations):
    if D == 0:
        return 1

    elif donations[D][L] is not None:
        return donations[D][L]

    different = 0
    j = min(D, L)

    while j != 0:
        different += TotalDifferentDonations(D - j, j, donations)
        j -= 1

    donations[D][L] = different
    print(donations)
    return donations[D][L]

# Testing
D = 1000
L = 15
donations = [ [None] * (L + 1) ] * (D + 1)

print(TotalDifferentDonations(D, L, donations))