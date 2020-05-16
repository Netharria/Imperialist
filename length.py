def convert_length(start_len, start_unit, destination_unit):
    if 'km' == start_unit.lower():
        meter_conversion = km_m(start_len)
    elif 'cm' == start_unit.lower():
        meter_conversion = cm_m(start_len)
    elif 'mm' == start_unit.lower():
        meter_conversion = mm_m(start_len)
    elif 'mi' == start_unit.lower():
        meter_conversion = mi_m(start_len)
    elif 'yd' == start_unit.lower():
        meter_conversion = yd_m(start_len)
    elif 'ft' == start_unit.lower():
        meter_conversion = ft_m(start_len)
    elif 'in' == start_unit.lower():
        meter_conversion = in_m(start_len)
    elif 'm' == start_unit.lower():
        meter_conversion = start_len
    else:
        return False
    if destination_unit == 'm':
        return meter_conversion
    elif 'km' == destination_unit.lower():
        return m_km(meter_conversion)
    elif 'cm' == destination_unit.lower():
        return m_cm(meter_conversion)
    elif 'mm' == destination_unit.lower():
        return m_mm(meter_conversion)
    elif 'mi' == destination_unit.lower():
        return m_mi(meter_conversion)
    elif 'yd' == destination_unit.lower():
        return m_yd(meter_conversion)
    elif 'ft' == destination_unit.lower():
        return m_ft(meter_conversion)
    elif 'in' == destination_unit.lower():
        return m_in(meter_conversion)
    else:
        return False


def convert_unit(unit):
    if 'km' == unit.lower():
        return 'Kilometers'
    elif 'cm' == unit.lower():
        return 'Centimeters'
    elif 'mm' == unit.lower():
        return 'Millimeters'
    elif 'mi' == unit.lower():
        return 'Miles'
    elif 'yd' == unit.lower():
        return 'Yards'
    elif 'ft' == unit.lower():
        return 'Feet'
    elif 'in' == unit.lower():
        return 'Inches'
    else:
        return False


def km_m(start_len):
    return start_len * 1000


def cm_m(start_len):
    return start_len / 100


def mm_m(start_len):
    return start_len / 1000


def mi_m(start_len):
    return start_len * 1609.344


def yd_m(start_len):
    return start_len * 0.9144


def ft_m(start_len):
    return start_len * 0.3048


def in_m(start_len):
    return start_len * .0254


def m_km(start_len):
    return start_len / 1000


def m_cm(start_len):
    return start_len * 100


def m_mm(start_len):
    return start_len * 1000


def m_mi(start_len):
    return start_len * 0.00062137119223733


def m_yd(start_len):
    return start_len * 1.0936132983377


def m_ft(start_len):
    return start_len * 3.2808398950131


def m_in(start_len):
    return start_len * 39.370078740157
