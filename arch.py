import math


def solve_r(c, h):
    return h/2 + (c**2)/(8*h)


def solve_alpha(c, r):
    return 2 * math.asin(c/(2*r))


def solve_h_ot_t(r, x, alpha):
    t = -1 + 2 * x / c  # пересчет в t
    return r * (math.sqrt(1 - t**2 * math.sin(alpha)**2) - math.cos(alpha))


def value(data):
    max_data = max(data, key=lambda i: i['Длина'])
    full_data = data.append(max_data)
    return full_data

if __name__ == "__main__":
    print('---Арочник---\n')
    while True:
        try:

            # Исходные данные
            c = float(input('Длина хорды(м):             ').replace(',', '.'))  # Длина хорды, м
            h = float(input('Высота хорды(м):            ').replace(',', '.'))  # Высота хорды, м
            shag = float(input('Полезная профнастила:       ').replace(',', '.'))

            if h > c / 2:
                print('\nВысота хорды не может быть больше половины длины хорды.\n'
                      'Проверьте данные.\n')
                continue

            R = solve_r(c, h)  # Радиус дуги
            alpha = solve_alpha(c, R)  # Угол раствора

            print('_' * 43)
            print(f'|{"Радиус:":10}|{"Угол:":15}|{"Длина дуги:":15}|')
            print('_' * 43)
            print(f'|{R:<10.4f}|{math.degrees(alpha):<15.4f}|{R*alpha:<15.4f}|')
            print('_' * 43, '\n')

            schetchik = 0
            x = 0
            a = []
            d = []
            while x < c - shag:
                x += shag
                y = solve_h_ot_t(R, x, alpha/2)
                a.append({'Шаг': x, 'Длина': y})
            print(value(a))

        except ValueError:
            print('\nОшибка -> для расчета должны вводиться только - цифры'
                  '\nРазделитель - точка(".") или запятая(",")\n')
            continue

        a = input('\nНажмите "Ввод" для еще одного просчета')
        print()
