from test_kyu5678.pseudo_test_lib import *
from kyu1234.kyu2 import *



clues = ( 3, 2, 2, 3, 2, 1,
          1, 2, 3, 3, 2, 2,
          5, 1, 2, 2, 4, 3,
          3, 2, 1, 2, 2, 4)

clues2 = ( 0, 0, 0, 2, 2, 0,
          0, 0, 0, 6, 3, 0,
          0, 4, 0, 0, 0, 0,
          4, 4, 0, 3, 0, 0)

clues3 = ( 0, 3, 0, 5, 3, 4,
          0, 0, 0, 0, 0, 1,
          0, 3, 0, 3, 2, 3,
          3, 2, 0, 3, 1, 0)

clues4 = [0]*24

# field = SkyscraperField(clues2)
# ITERATION_ROUNDS = 12
#
#
# field.pretty_print()
#
# field.print_lines()
# print('\n')
#
# field.solvePuzzle()

# for i in range(ITERATION_ROUNDS):
#     print("Iteration {}".format(i))
#     field.recalculatePossibilityField()
#     field.filterLinesByPossibilityField()
#     field.print_lines()
#     field.pretty_print()
#     print("\n\n")

sol2 = solve_puzzle(clues2)
print(sol2)

sol1 = solve_puzzle(clues)
print(sol1)



sol3 = solve_puzzle(clues3)
print(sol3)


