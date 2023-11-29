word1 = input()
word2 = input()
bulls = 0
cows = set()
for i in range(len(word1)):
    if word1[i] == word2[i]:
        bulls += 1
    else:
        if word1[i] in word2:
            cows.add(word1[i])
        if word2[i] in word1:
            cows.add(word2[i])
print(bulls, len(cows))


