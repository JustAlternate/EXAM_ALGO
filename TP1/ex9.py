
Monday = 0
Thusday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6

max_j = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

date = [Monday, 1, 1, 1900]

while date[3] != 2000 and date[2] != 12 and date[1] != 31:
    date[0] = (date[0] + 1) % 7
    date[1] = (date[1]+1) % max_j[date[2]]
