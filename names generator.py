import string, random

def simple_names():
    letter1=random.choice(string.ascii_uppercase)
    letter2=random.choice(string.ascii_lowercase)
    letter3=random.choice(string.ascii_lowercase)
    letter4=random.choice(string.ascii_lowercase)
    letter5=random.choice(string.ascii_lowercase)
    letter6=random.choice(string.ascii_lowercase)
    letter7=random.choice(string.ascii_lowercase)
    name= letter1+letter2+letter3+letter4+letter5+letter6+letter7
    return(name)
print(simple_names())
