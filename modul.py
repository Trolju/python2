import math
def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "nie mozna dzielic przez 0"
def potegowanie(a,b):
    return a ** b
def zaokroglanie(a, b):
    return round(a, b)