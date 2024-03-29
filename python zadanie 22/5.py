import string
import random

def generate_password(m):
    valid_chars = string.ascii_letters + string.digits
    valid_chars = ''.join(set(valid_chars) - {'l', 'I', '1', 'o', 'O'})
    password = []
    for i in range(m):
        password.append(random.choice(valid_chars))
    return ''.join(password)

def main(n, m):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(m)
        passwords.add(password)
    return list(passwords)


print("��������� ������ �� 7 ��������:", generate_password(7))
print("10 ��������� ������� ������ 15 ��������:")
print(*main(10, 15), sep="\n")