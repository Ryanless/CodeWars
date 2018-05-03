
#end function
def alphabet_war(fight):
    return  basic_alpha_war(fight)

#Evalutes who wins in a basic fight
def basic_alpha_war(fight_string):
    left_score = 0
    right_score = 0
    for char in fight_string:
        temp = evaluate_letter_strenght(char)
        left_score += temp[0]
        right_score += temp[1]
    print("left: %d right: %d" % (left_score, right_score))


    if left_score < right_score:
        return "Right side wins!"
    else:
        return "Left side wins!"

def priest_converting(fight_string):
    convert_letter(fight_string, 0)
    convert_letter(fight_string, len(fight_string) -1)
    for i in range(1, len(fight_string) - 1):
        if i == 't' or 'j':
            convert_letter(fight_string, i - 1)
            convert_letter(fight_string, i + 1)

    return fight_string


def check_convert_letter(fight_string, index):
    transform = (0, 0)
    if index == 0 & len(fight_string) > 1:
        pass
    elif index == len(fight_string) - 1:
        pass
    else:
        pass


def is_opponent_team(charA, charB):
    if charA in 'wpbst' & charB in 'mqdzj':
        return True
    elif charA in 'mqdzj' & charB in 'wpbst':
        return True
    else:
        return False


def convert_letter(char):
    return {'w': 'm',
            'p': 'q',
            'b': 'd',
            's': 'z',
            'm': 'w',
            'q': 'p',
            'd': 'b',
            's': 'z'}.get(char)


def evaluate_letter_strenght(char):
    return {'w': (4, 0),
            'p': (3, 0),
            'b': (2, 0),
            's': (1, 0),
            'm': (0, 4),
            'q': (0, 3),
            'd': (0, 2),
            'z': (0, 1)}.get(char, (0, 0))
