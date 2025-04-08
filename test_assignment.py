import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test for Bicycle ride method
def test_bicycle_ride():
    from assignment import Bicycle
    bicycle = Bicycle()
    assert bicycle.ride() == "Human powered, not enclosed", "DMACC Student, the Bicycle ride method should return 'Human powered, not enclosed'."

# Test for Bicycle riders method
def test_bicycle_riders():
    from assignment import Bicycle
    bicycle = Bicycle()
    assert bicycle.riders() == "1 or 2 if tandem or a daredevil", "DMACC Student, the Bicycle riders method should return '1 or 2 if tandem or a daredevil'."

# Test for Motorcycle ride method
def test_motorcycle_ride():
    from assignment import Motorcycle
    motorcycle = Motorcycle()
    assert motorcycle.ride() == "Engine powered, not enclosed", "DMACC Student, the Motorcycle ride method should return 'Engine powered, not enclosed'."

# Test for Motorcycle riders method
def test_motorcycle_riders():
    from assignment import Motorcycle
    motorcycle = Motorcycle()
    assert motorcycle.riders() == "1 or 2", "DMACC Student, the Motorcycle riders method should return '1 or 2'."

# Test for Car ride method
def test_car_ride():
    from assignment import Car
    car = Car()
    assert car.ride() == "Engine powered, enclosed", "DMACC Student, the Car ride method should return 'Engine powered, enclosed'."

# Test for Car riders method
def test_car_riders():
    from assignment import Car
    car = Car()
    assert car.riders() == "1 plus comfortably", "DMACC Student, the Car riders method should return '1 plus comfortably'."

if __name__ == "__main__":
    pytest.main()