
import time
start_time = time.time()


def rotate(l, n):
    return l[n:] + l[:n]

def pick_player(navneliste, rhyme_len, n):
    indeks = (rhyme_len - 1)% n
    spiller_i = navneliste[indeks]
    navneliste.remove(navneliste[indeks])
    rest = navneliste
    if len(navneliste) > 1:
        rest = rotate(navneliste, indeks % len(navneliste))
    return spiller_i, rest


#print(rotate(['Kalle','Lisa','Rakel'],3-1))
#print(rotate(['Kalle','Rakel'],2-1))

def opgave_e(input):
    lines = input.split('\n')
    word_count = len(lines[0].split())
    n = int(lines[1])
    navne = lines[2:]

    hold_1 = []
    hold_2 = []
    turn = 0

    for i in reversed(range(n)):
        spiller_i, navne = pick_player(navne, word_count, i + 1)
        if turn == 0:
            hold_1.append(spiller_i)
            turn = 1
        else:
            hold_2.append(spiller_i)
            turn = 0
    return hold_1, hold_2


print(opgave_e('eeny meeny miny\n4\nKalle\nLisa\nAlvar\nRakel'))
print(opgave_e('every other \n3\nA\nB\nC'))

print("--- %s seconds ---" % (time.time() - start_time))

#print(pick_player(['Kalle','Lisa','Alvar','Rakel'],5,4))




