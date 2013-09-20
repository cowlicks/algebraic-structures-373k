from sympy.combinatorics.named_groups import AlternatingGroup, \
        PermutationGroup, Permutation

# indexed from zero
H = PermutationGroup([Permutation(0), Permutation(0, 1, 2), Permutation(0, 2, 1)])
A4 = AlternatingGroup(4)

left_coset = []
right_coset = []

# for i in all permutations in A4
for i in A4.generate_schreier_sims():
    # Compute the cosets
    left = PermutationGroup([i*H[0], i*H[1], i*H[2]])
    right = PermutationGroup([H[0]*i, H[1]*i, H[2]*i])

    # check if we already have an equivalent coset
    if left not in left_coset:
        left_coset.append(left)
    if right not in right_coset:
        right_coset.append(right)
       
# print results
print('left cosets')
for i in left_coset:
    print(i)

print('right cosets')
for i in right_coset:
    print(i)
