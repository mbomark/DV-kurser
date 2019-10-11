from random import randint


targets = []



def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n", "Biathlon", "\n", "a hit or miss game", "\n", "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def open():
    return 0

def closed():
    return 1

def is_open(target):
    if target == open():
        return True
    elif target == closed():
        return False

def is_closed(target):
    if target == closed():
        return True
    elif target == open():
        return False
    
def new_targets():

    if len(targets) <5:
        for i in range(5):
            targets.append(open())

    #print(targets)

def close_target(target, targets):          #funkar med "targets" ej med new_targets
   
    if is_open( targets[target] ) == True:
        targets[target] = closed()
        print(targets)

def hits(targets):
    n = 0
    for target in targets:
        if is_closed(target) == True:
            n = n + 1

    print(n)

def target_to_string(target):
    if is_open(target) == True:
        return "* "
    elif is_closed(target) == True:
        return "O "

def targets_to_strings(targets):
    for i in range(len(targets)):
        if is_open(targets[i]) == True:     #ändrar i listan på position (i)
            targets[i] = '* '
        elif is_closed(targets[i]) == True:
            targets[i] = 'O '

def view_targets(targets):
    number = []
    for i in range(len(targets)):
        number.append(i)
    print(number)
    print(targets)

def random_hit():
    i = randint(0,1)
    if i == 0:
        return False
    elif i == 1:
        return True

def shoot(targets, target):
    
    
                    




ts = new_targets()
tt = targets_to_strings(targets)











splash()


