import random

def create_data(amount):
    data = []

    for i in range(amount):
        number = random.randint(1, 100)
        data.append(number)

    return data