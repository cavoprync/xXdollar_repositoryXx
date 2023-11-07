import random

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

random_string = generate_random_string(10)  # Change the length as needed
print("Random string:", random_string)
r: ", juhuslik_number)
juhuslik_number = random.randint(23, 420)
print("Juhuslik number: ", juhuslik_number)