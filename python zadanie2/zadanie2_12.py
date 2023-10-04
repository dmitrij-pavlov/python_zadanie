message = input()
num_chars = len(message)
cost = num_chars * 0.4
cost_str = "{:.2f}".format(cost)
print(cost_str + ' рублей')
