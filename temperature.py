def convert_temp(start_temp, start_unit, destination_unit):
    if 'f' == start_unit.lower():
        celsius_temp = fahrenheit_celsius(start_temp)
    elif 'k' == start_unit.lower():
        celsius_temp = kelvin_celsius(start_temp)
    elif 'c' == start_unit.lower():
        celsius_temp = start_temp
    else:
        return False
    if 'f' == destination_unit.lower():
        return celsius_fahrenheit(celsius_temp)
    elif 'k' == destination_unit.lower():
        return celsius_kelvin(celsius_temp)
    elif 'c' == destination_unit.lower():
        return celsius_temp
    else:
        return False


def convert_units(unit):
    if 'f' == unit.lower():
        return "Fahrenheit"
    elif 'k' == unit.lower():
        return "Kelvin"
    elif 'c' == unit.lower():
        return "Celsius"
    else:
        return False


def celsius_fahrenheit(start_temp):
    return (start_temp * 9 / 5) + 32


def fahrenheit_celsius(start_temp):
    return (start_temp - 32) * 5 / 9


def kelvin_celsius(start_temp):
    return start_temp - 273.15


def celsius_kelvin(start_temp):
    return start_temp + 273.15
