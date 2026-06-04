import random
import time

def generate_matric_number():
    year= time.strftime("%y")
    rand_digits=random.randint(200000,900000)
    return f"SAM{year}{rand_digits}"



