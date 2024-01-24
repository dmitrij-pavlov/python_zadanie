import random

def generate_password(m):
    password = ''
    for i in range(m):
        char = random.choice('23456789abcdefghjklmnopqrstuvwxyz')
        password += char
        if i % 2 == 0:
            password += random.choice('A-Z')
        else:
            password += random.choice('a-z')
    return password

def main(n, m):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m))
    return passwords


print("��������� ������ �� 7 ��������:" , generate_password(7))
print("10 ��������� ������� ������ 15 ��������:")
print(*main(10, 15), sep="\n")