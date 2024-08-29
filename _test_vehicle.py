from vehicle import Car, Vehicle


def test_vehicle_class():
    vehicle1 = Vehicle('100', 'red')
    vehicle2 = Vehicle('1000', 'blue')
    assert vehicle1.color == 'red'
    assert vehicle1.regno == '100'
    assert vehicle2.regno== '1000'
    assert vehicle2.color== 'blue'

def test_car_class():
    Vehicle1 = Car("1000", 'grey')
    assert Vehicle1.color == 'grey'
    assert Vehicle1.getType() == "Car"

def test_check_inheritance():
    vehicle1 =Car('100', 'grey')
    assert isinstance(vehicle1, Vehicle)
