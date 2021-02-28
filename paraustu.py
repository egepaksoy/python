para = 10-2.5


def paraustu(nakit):
    if nakit <= 0:
        return 'daha büyük bir değer veriniz'

    paralar = [200, 100, 50, 20, 10, 5, 1, 0.50, 0.2, 0.1]
    nakitler = {200: 0, 100: 0, 50: 0, 20: 0,
                10: 0, 5: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0}
    x = 0

    while x < len(paralar):
        if nakit - paralar[x] == 0:
            nakitler[paralar[x]] += 1
            nakit -= paralar[x]
            break

        if nakit - paralar[x] > 0:
            nakitler[paralar[x]] += 1
            nakit -= paralar[x]

        else:
            x += 1

    new_nakitler = {}
    for nakit in nakitler:
        if nakitler[nakit] != 0:
            new_nakitler[nakit] = nakitler[nakit]
    return new_nakitler


print(paraustu(para))
