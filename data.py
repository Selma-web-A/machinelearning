import random
from unicodedata import name

def create_data(amount):
    listOfData = []

    for i in range(amount):
        number = random.randint(1, 50)
        listOfData.append(number)

    return listOfData

def datalista ():
    data = [10, 10, 20, 30, 30, 30, 40]
    return data


def fruktlista (name):
    frukt = ["Äpple, Apelsin, Kiwi"]
    
    for i in(name):
        number = random.randint(1, 10)
        frukt.append(number)

    return frukt