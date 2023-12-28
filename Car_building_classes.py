import time
class Wheel:
    def __init__(self, size, color, tire_type, air_pressure=35, rim_type="steel"):
        self.size = size
        self.color = color
        self.tyre_type = tire_type
        self.air_pressure = air_pressure
        self.rim_type = rim_type
    #
    # equality check
    def __eq__(self, other):
        if isinstance(other, Wheel):
            return (
                    self.tyre_type == other.tyre_type and
                    self.size == other.size and
                    self.color == other.color and
                    self.air_pressure == other.air_pressure and
                    self.rim_type == other.rim_type)
        else:
            return False

    def roll(self):
        return f"The wheel with {self.tyre_type} is rolling!"
    def needs_air(self):
        if self.air_pressure < 30:
            return "The wheel needs more are!"
        else:
            return "The air pressure is good."
    def describe_rim(self):
        if self.rim_type == "steel":
            return f"The rim is made of steel"
        elif self.rim_type == "light alloy":
            return f"The rim is made of light alloy"
        else:
            return "Unknown type"


class Chassis:
    def __init__(self, size, color, weight, material="steel"):
        self.size = size
        self.material = material
        self.color = color
        self.weight = weight
        self.wheels = []
        self.motor = []

    def attach_wheel(self, x):
        if len(self.wheels) < 4:
            self.wheels.append(x)
            print(f"{x.size} wheel attached successfully!")
            time.sleep(1)
        elif x in self.wheels:
            print("This wheel is already attached! Try other one!")
        else:
            print("Cannot attach more than 4 wheels.")

    def wheels_check(self):
        if len(self.wheels) >= 4:
            print("The car has all wheels attached...")
            time.sleep(1)
            return True
        else:
            print("Cannot move without enough wheels. Please attach any!")
            return False
    def attach_motor(self, x):
        if len(self.motor) == 0:
            self.motor.append(x)
            print(f"{x.fuel_type} {x.capacity} Motor is attached successfully!")
            time.sleep(1)
        else:
            print("NB!!! Motor is already attached")
    def motor_check(self):
        attached_motor = self.motor[0]
        if hasattr(attached_motor, "fuel_type"):
            print("The chassis has motor attached...")
            time.sleep(1)
            return True
        else:
            print("The chassis has no motor")
            return False
    def drive(self):
        if self.wheels_check() and self.motor_check():
            print("We now can start driving!".upper())
        else:
            print("The construction in not complete, please install the motor or wheels!")

class Motor:
    def __init__(self, fuel_type, capacity, power, torque, fuel_consumption,rpm, number_of_pistons=4):
        self.rpm = rpm
        self.fuel_type = fuel_type
        self.power = power
        self.torque = torque
        self.number_of_pistons = number_of_pistons
        self.fuel_consumption = fuel_consumption
        self.capacity = capacity
        self.transmission = []

    def fuel_type_check(self):
        if self.fuel_type == "Gasoline":
            return f"Fuel type is {self.fuel_type}"
        elif self.fuel_type == "Diesel":
            return f"Fuel type is {self.fuel_type}"
        else:
            return "Incorrect fuel type"

    def attach_transmission(self, x):
        if len(self.transmission) == 0:
            self.transmission.append(x)
            print(f"Transmission {x.trans_type} is successfully attached!")
        else:
            print(f"Transmission was not attached")
    def transmission_check(self):
        attached_transmisstion = self.transmission[0]
        if hasattr(attached_transmisstion, "trans_type"):
            print(f"The motor has transmission attached...")
            time.sleep(1)
            return True
        else:
            print("The motor has no transmission")
            return False




class Transmission:
    def __init__(self, first_gear, second_gear, third_gear, fourth_gear, fifth_gear, clutch, trans_type):
        self.first_gear = first_gear
        self.second_gear = second_gear
        self.third_gear = third_gear
        self.fourth_gear = fourth_gear
        self.fifth_gear = fifth_gear
        self.clutch = clutch
        self.trans_type = trans_type

    def transmission_type(self):
        if self.trans_type == "Manual":
            print(f"The transmission type is {self.trans_type}")
        elif self.trans_type == "Automatic":
            print(f"The transmission type is {self.trans_type}")
        else:
            print(f"The transmission type is N/A")

# Instantiate a transmission
trans1 = Transmission(1, 2, 3, 4, 5, "on", trans_type = "Manual")
trans2 = Transmission(1, 2, 3, 4, 5, "on", trans_type = "Automatic")


# Instantiate a Chassis
my_chassis = Chassis(78, "grey", 348)

# Instantiate a Motor
motor1 = Motor("Gasoline", 5, 87, 154, 11, 500)
motor2 = Motor("Diesel", 2.4, 112, 87, 6, 500)
motor3 = Motor("Natural gas", 2.0, 111, 87, 7, 500)

# Attach the motor to the chassis
motor_attachment_attempt = my_chassis.attach_motor(motor3)
# Motor installation check
# motor_check = my_chassis.motor_check()

# Instantiate a Wheel
my_wheel = Wheel(18, "black", "summer", 35)
my_wheel2 = Wheel(18, "black", "summer", 35)
my_wheel3 = Wheel(18, "black", "summer", 35)
my_wheel4 = Wheel(18, "black", "summer", 35)


# Wheel attachment attempts
if my_wheel == my_wheel2 == my_wheel3 == my_wheel4:
    wheel_attachment_result = my_chassis.attach_wheel(my_wheel)
    wheel_attachment_result1 = my_chassis.attach_wheel(my_wheel2)
    wheel_attachment_result2 = my_chassis.attach_wheel(my_wheel3)
    wheel_attachment_result3 = my_chassis.attach_wheel(my_wheel4)
else:
    print("Wheels have different parameters")

#transmission attachment attempt
transmission_attachment_attempt1 = motor1.attach_transmission(trans2)

#transmission check
transmission_check1 = motor1.transmission_check()

#drive attempt
drive_attempt = my_chassis.drive()



