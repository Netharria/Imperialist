def convert_wgt(start_wgt, start_unit, destination_unit):
    if 'kg' == start_unit:
        grams_conversion = kg_g(start_wgt)
    elif 'lb' == start_unit:
        grams_conversion = lb_g(start_wgt)
    elif 'oz' == start_unit:
        grams_conversion = oz_g(start_wgt)
    elif 'g' == start_unit:
        grams_conversion = start_wgt
    else:
        return False
    if 'g' == destination_unit:
        return grams_conversion
    elif 'kg' == destination_unit:
        return g_kg(grams_conversion)
    elif 'lb' == destination_unit:
        return g_lb(grams_conversion)
    elif 'oz' == destination_unit:
        return g_oz(grams_conversion)
    else:
        return False


def convert_unit(unit):
    if unit == 'g':
        return 'Grams'
    elif 'kg' == unit:
        return 'Kilograms'
    elif 'lb' == unit:
        return 'Pounds'
    elif 'oz' == unit:
        return 'Ounces'


def kg_g(start_wgt):
    return start_wgt * 1000


def lb_g(start_wgt):
    return start_wgt * 453.5924


def oz_g(start_wgt):
    return start_wgt * 28.349556839727


def g_kg(start_wgt):
    return start_wgt / 1000


def g_lb(start_wgt):
    return start_wgt * 0.002204622476038


def g_oz(start_wgt):
    return start_wgt * 0.03527392
