n = int(input())
sentences = []
index = []
for i in range(n):
    sentences.append(input())
num = int(input())
for j in range(num):
    index.append(int(input()))
for i in index:
    print(sentences[i - 1])

