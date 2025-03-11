import random

def random_primer():
    chislo_1 = random.randint(-100, 100)
    chislo_2 = random.randint(-100, 100)
    myseq = ['+', '-', '/', '*']
    znak = random.choice(myseq)
    return f"{chislo_1} {znak} {chislo_2}"

def calk(primer):
    split_primer = primer.split(' ')
    nomer_1 = float(split_primer[0])
    znako = split_primer[1]
    nomer_2 = float(split_primer[2])
    if znako == '+':
        return nomer_1 + nomer_2
    elif znako == '-':
        return nomer_1 - nomer_2
    elif znako == '*':
        return nomer_1 * nomer_2
    else:
        return round(nomer_1 / nomer_2, 2)

def chek(correct, user_input):
    if round(user_input, 2) == round(correct, 2):
        return True
    else:
        return False


