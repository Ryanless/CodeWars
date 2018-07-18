
from kyu5678.kyu5 import *
from test_kyu5678.pseudo_test_lib import *




# pseudo_test_func(domain_name, "http://github.com/carbonfive/raygun")
# pseudo_test_func(domain_name, "http://www.zombie-bites.com")
# pseudo_test_func(domain_name, "https://www.cnet.com")
# pseudo_test_func(domain_name, "www.xakep.ru")


# pseudo_test_func(scramble_words, 'professionals')
# pseudo_test_func(scramble_words, 'i')
# pseudo_test_func(scramble_words, '')
# pseudo_test_func(scramble_words, 'me')
# pseudo_test_func(scramble_words, 'you')
# pseudo_test_func(scramble_words, 'card-carrying')
# pseudo_test_func(scramble_words, "shan't")
# pseudo_test_func(scramble_words, '-dcba')
# pseudo_test_func(scramble_words, 'I can!')


# carpark1 = [[1, 0, 0, 0, 2],
#            [0, 0, 0, 0, 0]]
#
# carpark2 = [[2, 0, 0, 1, 0],
#            [0, 0, 0, 1, 0],
#            [0, 0, 0, 0, 0]]
#
# carpark3 = [[0, 2, 0, 0, 1],
#            [0, 0, 0, 0, 1],
#            [0, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]]
#
# carpark4 = [[1, 0, 0, 0, 2],
#            [0, 0, 0, 0, 1],
#            [1, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0]]
#
# carpark5 = [[0, 0, 0, 0, 2]]
#
# pseudo_test_func(escape, carpark1)
# pseudo_test_func(escape, carpark2)
# pseudo_test_func(escape, carpark3)
# pseudo_test_func(escape, carpark4)
# pseudo_test_func(escape, carpark5)


# pseudo_test_func(order_weight, "103 123 4444 99 2000")
# pseudo_test_func(order_weight, "2000 10003 1234000 44444444 9999 11 11 22 123")
# pseudo_test_func(order_weight, "12")
# pseudo_test_func(order_weight, "")
# pseudo_test_func(order_weight, )

# pseudo_test_func(dirReduc, ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
# pseudo_test_func(dirReduc, ["NORTH", "WEST", "SOUTH", "EAST"])


# pseudo_test_func(parse_simple_molecule, 'H2O')

# a = seven(times(five()))
# print(a)

# pseudo_test_func(smallest, 324)
# pseudo_test_func(smallest, 32300)
# pseudo_test_func(smallest, 3204)
# pseudo_test_func(smallest, 1000)

farm = "fox,bug,chicken,grass,sheep"
prarie = 'giraffe,leaves,leaves,leaves,bear,bug,leaves,leaves,panda'
long_necks = 'big-fish,lion,leaves,grass,busker,giraffe,giraffe,grass,leaves,giraffe'
pseudo_test_func(who_eats_who, long_necks)
pseudo_test_func(who_eats_who, prarie)
pseudo_test_func(who_eats_who, farm)