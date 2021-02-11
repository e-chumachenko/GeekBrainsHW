# count()

from itertools import count

for i in count(3):
    if i > 10:
        break
    else:
        print(i)


# cycle()

from itertools import cycle

w_list = ['раз', 'два', 'три']
i = 1
for pas in cycle(w_list):
    if i > 9:
        break
    print(pas)
    i += 1
