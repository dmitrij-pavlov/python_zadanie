interval1 = 1
interval2 = 10000

for _ in range(10):
    mid = (interval1 + interval2) // 2
    response = input(str(mid) + '\n')

    if response == '>':
        interval1 = mid + 1
    elif response == '<':
        interval2 = mid - 1
    elif response == '=':
        break
