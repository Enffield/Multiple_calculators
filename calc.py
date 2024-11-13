print('---Calc---\n')
while True:
    def a_view(value_1):
        kont_m_kv = []
        kont_pog_m = []
        kont_sum = []
        shirina = 0
        while True:
            try:
                shirina = float(input('\nШирина: ').replace(',', '.'))
            except ValueError:
                print('Ошибка')
                continue
            else:
                break

        t = f'|{'Номер':<5}|{'Кол - во':<8}|{'Длина':<8}|{'Пог.м':<15}|{'М2':15}|'
        print('_' * (len(t)))
        print(t)
        print('_' * (len(t)))
        for i in value_1:
            pog_m = i['Штук'] * i['Длина']
            m_kv = i['Штук'] * i['Длина'] * shirina
            print(f'|{i['Номер']:^5}|{i['Штук']:<8}|{i['Длина']:<8}|{pog_m:<15.3f}|{m_kv:<15.3f}|')
            kont_m_kv.append(m_kv)
            kont_pog_m.append(pog_m)
            kont_sum.append(i['Штук'])
        print('_' * (len(t)))
        print(f'|Итого|{sum(kont_sum):<8}|{'---':^8}|{sum(kont_pog_m):<15.3f}|{sum(kont_m_kv):<15.3f}|')
        print('_' * (len(t)))

        valuess = input('\nP.S.')
        print()

    if __name__ == '__main__':
        a = []
        shetchik = 0
        while True:
            sht_long = input('Кол -во длина: ').replace(',', '.')

            if sht_long == '0':
                print('Все данные введены')
                break

            value = sht_long.split()

            if len(value) != 2:
                print('Должно быть 2 значения: Кол -во длина')
                continue

            try:
                value = [float(i) for i in value]
            except ValueError:
                print('Значение должно состоять из цифр')
                continue

            shetchik += 1
            a.append({'Номер': shetchik, 'Штук': value[0], 'Длина': value[1]})

        a_view(a)

    continue