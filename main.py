import sys
import math

def main():
    args = len(sys.argv) - 1
    if args == 0 or sys.argv[1] == "--help":
        print(
    "mathtool — решение уравнений вида A*x^2 + B*x + C = 0 \nИспользование:\npython mathtool.py -> вывод справки\npython mathtool.py --help -> вывод справки\npython mathtool.py solve -> ввод коэффициентов с клавиатуры\npython mathtool.py solve -a 1 -b -3 -c 2 -> решение с заданными коэффициентами\nКоэффициенты A, B, C — целые числа, по модулю не превышающие 10000."
    )
        sys.exit(0)
    elif sys.argv[1] != "solve":
        print("Неизвестная команда")
        sys.exit(1)
    elif sys.argv[1] == "solve" and len(sys.argv) == 2:
        A = str(input("Введите A: "))
        B = str(input("Введите B: "))
        C = str(input("Введите C: "))
    elif len(sys.argv) == 8:
        if sys.argv[2] != "-a" and sys.argv[4] != "-b" and sys.argv[6] != "-c":
            print("Неизвестный параметр")
            sys.exit(1)
        A = int(sys.argv[3])
        B = int(sys.argv[5])
        C = int(sys.argv[7])
    else:
        print("Неверный набор параметров") 
        sys.exit(1)
    try:
        A1 = int(A)
        B1 = int(B)
        C1 = int(C)
    except ValueError:
           print("ОШИБКА: коэффициент не является целым числом")
           sys.exit(1) 
    if abs(int(A)) > 10000 or abs(int(B)) > 10000 or abs(int(C)) > 10000:
                print("ОШИБКА: значение вне допустимого диапазона")
                sys.exit(1)
    if A == 0:
        if B != 0:
            print ("Линейное уравнение")
            x = -C / B
            print (f"x = {x:.3f}")
        else:
            print("ОШИБКА: это не уравнение, неизвестное отсутствует")
            sys.exit(1)
    else:
        print ("Уравнение квадратное")
        D = (B**2) - (4*A*C)
        print(f"Дискриминант: {D:.3f}")
        if D > 0:
            x1 = (-b + D**(1/2))/(2*a)
            x2 = (-b - D**(1/2))/(2*a)
            print (f"x1 = {x1:.3f}")
            print (f"x2 = {x2:.3f}")
        elif D == 0:
                x = -b / (2*a)
                print (f"x = {x:.3f}")
        else:
                print("Действительных корней нет")      
    sys.exit(0)

main()