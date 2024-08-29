import pytest
from parkinglot import ParkingLot
from vehicle import Vehicle


# def test_create_parking():
#     parking_lot = ParkingLot()
#     capacity = 10
#     parking_lot.create_parking_lot(10)
#     assert capacity == parking_lot.capacity

class TestParking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.parking_lot = ParkingLot()

    def test_create_parking_lot(self):
        assert self.parking_lot.create_parking_lot(6) == 6
        assert self.parking_lot.capacity == 6

    def test_park(self):
        self.parking_lot.create_parking_lot(3)
        assert self.parking_lot.park("KA-01-HH-1234", "White") == 1
        assert self.parking_lot.park("KA-01-HH-9999", "White") == 2
        assert self.parking_lot.park("KA-01-BB-0001", "Black") == 3
        assert self.parking_lot.park("KA-01-HH-7777", "Red") == -1  # Parking lot is full

    def test_leave_slot(self):
        self.parking_lot.create_parking_lot(3)
        self.parking_lot.park("KA-01-HH-1234", "White")
        self.parking_lot.park("KA-01-HH-9999", "White")
        self.parking_lot.park("KA-01-BB-0001", "Black")
        
        assert self.parking_lot.leave_slot(2) == True  # Slot 2 is now free
        assert self.parking_lot.leave_slot(2) == False  # Slot 2 is already empty
        # assert self.parking_lot.leave_slot(5) == False  # Invalid slot number

    def test_check_status(self, capsys):
        self.parking_lot.create_parking_lot(3)
        self.parking_lot.park("KA-01-HH-1234", "White")
        self.parking_lot.park("KA-01-HH-9999", "White")
        
        self.parking_lot.check_status()
        captured = capsys.readouterr()
        assert "Slot No \tRegistration No \tColor" in captured.out
        assert "1\tKA-01-HH-1234\tWhite" in captured.out
        assert "2\tKA-01-HH-9999\tWhite" in captured.out

    def test_get_regno_from_color(self):
        self.parking_lot.create_parking_lot(3)
        self.parking_lot.park("KA-01-HH-1234", "White")
        self.parking_lot.park("KA-01-HH-9999", "White")
        self.parking_lot.park("KA-01-BB-0001", "Black")
        
        assert self.parking_lot.get_regno_from_color("White") == ["KA-01-HH-1234", "KA-01-HH-9999"]
        assert self.parking_lot.get_regno_from_color("Black") == ["KA-01-BB-0001"]
        assert self.parking_lot.get_regno_from_color("Red") == []

    def test_get_slotno_from_regno(self):
        self.parking_lot.create_parking_lot(3)
        self.parking_lot.park("KA-01-HH-1234", "White")
        self.parking_lot.park("KA-01-HH-9999", "White")
        self.parking_lot.park("KA-01-BB-0001", "Black")
        
        assert self.parking_lot.get_slotno_from_regno("KA-01-HH-1234") == 1
        assert self.parking_lot.get_slotno_from_regno("KA-01-HH-9999") == 2
        assert self.parking_lot.get_slotno_from_regno("KA-01-BB-0001") == 3
        assert self.parking_lot.get_slotno_from_regno("KA-01-HH-0000") == -1

    def test_get_slotno_from_color(self):
        self.parking_lot.create_parking_lot(3)
        self.parking_lot.park("KA-01-HH-1234", "White")
        self.parking_lot.park("KA-01-HH-9999", "White")
        self.parking_lot.park("KA-01-BB-0001", "Black")
        
        assert self.parking_lot.get_slotno_from_color("White") == ["1", "2"]
        assert self.parking_lot.get_slotno_from_color("Black") == ["3"]
        assert self.parking_lot.get_slotno_from_color("Red") == []

if __name__ == '__main__':
    pytest.main()
