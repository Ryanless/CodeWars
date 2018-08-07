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

field = SkyscraperField(clues4)


#start
field.recalculatePossibilityField()
field.pretty_print()

#step 1
field.filterLines()
field.print_lines()
field.recalculatePossibilityField()
field.pretty_print()

#step 1
field.filterLines()
field.print_lines()
field.recalculatePossibilityField()
field.pretty_print()
#step 1
field.filterLines()
field.print_lines()
field.recalculatePossibilityField()
field.pretty_print()
#step 1
field.filterLines()
field.print_lines()
field.recalculatePossibilityField()
field.pretty_print()
#step 1
field.filterLines()
field.print_lines()
field.recalculatePossibilityField()
field.pretty_print()
#step 1
field.filterLines()
field.print_lines()
field.recalculatePossibilityField()
field.pretty_print()
#step 1
field.filterLines()
field.print_lines()
field.recalculatePossibilityField()
field.pretty_print()
