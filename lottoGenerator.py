import random

print("Wybierz grę Lotto dla której chcesz wylosowac zestaw liczb.")
gra = input()
lotto = []
euro = [[], []]
ekstra = [[], []]
multi = []
mini = []
if gra == 'lotto':
    lotto.append(random.sample(range(1, 49), 6))
    lotto.sort()
    print(lotto)
elif gra == 'euro':
    euro[0].append(random.sample(range(1, 50), 6))
    euro[1].append(random.sample(range(1, 10), 2))
    print(euro)
elif gra == 'ekstra':
    ekstra[0].append(random.sample(range(1, 35), 5))
    ekstra[0].sort()
    ekstra[1].append(random.sample(range(1, 4), 1))
    ekstra[1].sort()
    print(ekstra)
elif gra == 'multi':
    print("Ile liczb chcesz typować?")
    ile = int(input())
    multi.append(random.sample(range(1, 80), ile))
    print(multi)
elif gra == 'mini':
    mini.append(random.sample(range(1, 42), 5))
    print(mini)
else:
    print("Nieprawidłowa nazwa gry.")