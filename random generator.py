import random, string

n = int(input("Length: "))
chars = string.ascii_letters + string.digits + string.punctuation
print("Password:", "".join(random.choice(chars) for _ in range(n)))
