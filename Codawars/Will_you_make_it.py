def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg * fuel_left
    if a < distance_to_pump:
        return False
    else:
        return True


zero_fuel(90, 25, 2)


def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


zeroFuel(141, 50, 2)
