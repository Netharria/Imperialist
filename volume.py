def convert_vol(start_vol, start_unit, destination_unit):
    if "l" == start_unit.lower():
        liter_conversion = start_vol
    elif "tsp" == start_unit.lower():
        liter_conversion = tsp_liter(start_vol)
    elif "tbsp" == start_unit.lower():
        liter_conversion = tbsp_liter(start_vol)
    elif "oz" == start_unit.lower():
        liter_conversion = oz_liter(start_vol)
    elif "c" == start_unit.lower():
        liter_conversion = cups_liter(start_vol)
    elif "pt" == start_unit.lower():
        liter_conversion = pint_liter(start_vol)
    elif "qt" == start_unit.lower():
        liter_conversion = quart_liter(start_vol)
    elif "gal" == start_unit.lower():
        liter_conversion = gallon_liter(start_vol)
    elif "ml" == start_unit.lower():
        liter_conversion = ml_liter(start_vol)
    else:
        return False
    if "l" == destination_unit.lower():
        return liter_conversion
    elif "tsp" == destination_unit.lower():
        return liter_tsp(liter_conversion)
    elif "tbsp" == destination_unit.lower():
        return liter_tbsp(liter_conversion)
    elif "oz" == destination_unit.lower():
        return liter_oz(liter_conversion)
    elif "c" == destination_unit.lower():
        return liter_cups(liter_conversion)
    elif "pt" == destination_unit.lower():
        return liter_pint(liter_conversion)
    elif "qt" == destination_unit.lower():
        return liter_quart(liter_conversion)
    elif "gal" == destination_unit.lower():
        return liter_gallon(liter_conversion)
    elif "ml" == destination_unit.lower():
        return liter_ml(liter_conversion)
    else:
        return False


def convert_units(unit):
    if "l" == unit.lower():
        return "Liters"
    elif "tsp" == unit.lower():
        return "Teaspoons"
    elif "tbsp" == unit.lower():
        return "Tablespoons"
    elif "oz" == unit.lower():
        return "Ounces"
    elif "c" == unit.lower():
        return "Cups"
    elif "pt" == unit.lower():
        return "Pints"
    elif "qt" == unit.lower():
        return "Quarts"
    elif "gal" == unit.lower():
        return "Gallons"
    elif "ml" == unit.lower():
        return "Milliliters"
    else:
        return False


def tsp_liter(start_vol):
    return start_vol * 0.0049289216


def tbsp_liter(start_vol):
    return start_vol * 0.014786765


def oz_liter(start_vol):
    return start_vol * 0.029573530


def cups_liter(start_vol):
    return start_vol * 0.23658824


def pint_liter(start_vol):
    return start_vol * 0.47317647


def quart_liter(start_vol):
    return start_vol * 0.94635295


def gallon_liter(start_vol):
    return start_vol * 3.7854118


def ml_liter(start_vol):
    return start_vol * 0.001


def liter_ml(start_vol):
    return start_vol * 1000


def liter_tsp(start_vol):
    return start_vol * 202.88414


def liter_tbsp(start_vol):
    return start_vol * 67.628045


def liter_oz(start_vol):
    return start_vol * 33.814023


def liter_cups(start_vol):
    return start_vol * 4.2267528


def liter_pint(start_vol):
    return start_vol * 2.1133764


def liter_quart(start_vol):
    return start_vol * 1.0566882


def liter_gallon(start_vol):
    return start_vol * 0.26417205
