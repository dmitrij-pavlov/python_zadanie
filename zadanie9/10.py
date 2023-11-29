n = int(input())
white_list = []
requests = []
for i in range(n):
    white_list.append(input())
n_req = int(input())
for i in range(n_req):
    requests.append(input())
for i in requests:
    if i in white_list:
        print(i)