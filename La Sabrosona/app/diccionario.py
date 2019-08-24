if __name__ == "__main__":
    equipos_lpf = {
        'arabe unido': 15,
        'CAI': 2,
        'Tauro': 13,
        'San Francisco': 10,
        'Plaza amador': 7,
        'Universitario': 2,
        'Sporting SM': 1
    }

    print(equipos_lpf)

    print(equipos_lpf['CAI'])

    equipos_lpf['Alianza FC'] = 1
    print(equipos_lpf)
    equipos_lpf['Alianza FC'] = 0
    print(equipos_lpf)

    del equipos_lpf['Alianza FC']
    print(equipos_lpf)

    print(equipos_lpf.get('arabe unido'))
    print(equipos_lpf.get('Atlentico Veraguense'))

    e = equipos_lpf.items()
    print(e)

    e1 = equipos_lpf.keys()
    print(e1)

    e2 = equipos_lpf.values()
    print(e2)

    equipos_lpf.pop('CAI')
    print(equipos_lpf)

    equipos_lpf.clear()
    print(equipos_lpf)