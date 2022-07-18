import func
import math

dot_limit = func.enter_float_number("Введите количество знаков после запятой в формате 0.xxxxxx: ")

dot_limit = func.digit_after_dot_counter(dot_limit)
print(f"Число Пи с округлением до {dot_limit} знаков после запятой - {round(math.pi, dot_limit)}")