import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(100)
t.pensize(1)
h=0.5
for i in range(400):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.fillcolor(c)
    h+=0.008
    t.begin_fill()
    t.fd(i)
    t.lt(100)
    t.circle(30)
    for j in range(2):
        t.fd(i*j)
        t.rt(109)
    t.end_fill()

# class ComplexNumber():
#     def __init__(self,real,imaginary) -> None:
#         self.real = real
#         self.imaginary = imaginary
#     def __it__(self,complex_number_2):
#         if self.real < complex_number_2.real:
#             return True
#         elif self.real == complex_number_2.real:
#             if self.imaginary<complex_number_2.imaginary:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     def __str__(self) -> str:
#         return str(self.real)+ ' + ' +str(self.imaginary)+'i'
# complex_number1 = ComplexNumber(1,2)
# complex_number2 = ComplexNumber(3,4)
# if (complex_number1 < complex_number2):
#     print(f'complex number:({complex_number1}) is less then the complex number:({complex_number2})')
# else:
#     print(f'complex number:({complex_number1}) is not less then the complex number:({complex_number2})')

