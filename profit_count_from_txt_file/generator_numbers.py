import re

def generator_numbers(text: str):
    pattern =  r"\d+\.\d+"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

