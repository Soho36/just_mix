from PiConst import Pi
import time
a = int(input("Введите высоту прямоугольника(cm): "))
b = int(input("Введите ширину прямоугольника(cm): "))
r = int(input("Введите радиус круга(cm): "))
time.sleep(1)
print("-------------------------------------")
print("Считаем...")
time.sleep(2)
print("-------------------------------------")


def rectangle_area():
    return a * b


print("Площадь прямоугольника: ", rectangle_area(), "cm2")


def round_area():
    return Pi * r ** 2


print("Площадь круга: ", round_area(), "cm2")
print("-------------------------------------")
print("Считаем...")
time.sleep(2)
print("-------------------------------------")
if rectangle_area() > round_area():
    print("Прямоугольник больше!".upper())
elif rectangle_area() < round_area():
    print("Круг больше!".upper())
else:
    print("Фигуры равны".upper())
