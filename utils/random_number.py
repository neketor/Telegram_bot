import random
def random_number(first, sec):
    return random.randint(first, sec) if sec > first else print(BaseException("Второе число превышает первое."))
