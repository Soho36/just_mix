import time
import random
def welcome_text():
    print("\nWelcome to the car building simulator!".upper(), "(the best ever existed)")
    print("\nPlease wait, loading", end=" ")
    time.sleep(1)
    n = 0
    while n <= 2:
        n += 1
        print(".", end=" ", flush=True)
        time.sleep(1)
    print(f"\n\nThe point is to fit 3 Chassis with the right parts in proper order")
welcome_text()

def print_available_parts():
    print("\n")
    print("Available chassis are (C1-C3):")
    time.sleep(1)
    for chassis in Chassis.chassis_instances:
        print(f"{chassis} chassis")
    print("-------------------")

    print("Available motors are (M1-M3):")
    time.sleep(1)
    for motor in Motor.motor_instances:
        print(f"{motor} motor")
    print("-------------------")

    print("Available transmissions are:(T1-T2)")
    time.sleep(1)
    for gearbox in Gearbox.gearbox_instances:
        print(f"{gearbox} transmission")
    print("-------------------")

    print("Available wheels are:(W1-W3)")
    time.sleep(1)
    for wheels in Wheels.wheels_instances:
        print(f"{wheels} wheels")
    print("-------------------")



counter_list = []
def print_current_state():
    global counter_list
    # print("before clear", counter_list)

    if len(counter_list) <= 7:
        counter_list.clear()     #this one must be inside the IF
        # print("after clear", counter_list)
        print("\nCurrent list of assembled parts (you need 9 lines to succeed):")
        for chassis in Chassis.chassis_instances:
            if chassis.motor_attached:
                counter_list.append(random.randint(0,10))
                print(f"{chassis} chassis --->: {chassis.motor_attachment_point} motor")

            if chassis.wheels_attached:
                counter_list.append(random.randint(20,30))
                print(f"{chassis} chassis ---> {chassis.wheels_attachment_point} wheels")

        for motor in Motor.motor_instances:
            if motor.transmission_attached:
                counter_list.append(random.randint(40,50))
                print(f"{motor} motor ---> {motor.gearbox_placement} transmission")

        print("Number of attached parts: ", len(counter_list))
        print("\nReloading...\n")
        time.sleep(1)
        # print("bottom line", counter_list)
    else:
        print("Bingo! You accomplished impossible! \n Game over!".upper())
        exit()
class Chassis:
    chassis_instances = []
    def __init__(self, chassis_type):
        Chassis.chassis_instances.append(self)
        self.chassis_type = chassis_type
        self.motor_attachment_point = None
        self.wheels_attachment_point = None
        self.motor_attached = False
        self.wheels_attached = False

    def __str__(self):
        return self.chassis_type

    def motor_attachment(self, motor_object):
        if motor_object.gearbox_placement is not None:
            if self.motor_attachment_point == None and self.motor_attached is False:
                self.motor_attachment_point = motor_object
                self.motor_attached = True
                print(f"\n{motor_object} motor was successfully attached to the {self.chassis_type} chassis")
                time.sleep(1)

            else:
                print(f"\nUnable to attach {motor_object.fuel_type} motor because there is other motor already attached")
                time.sleep(1)

        else:
            print(f"\nUnable to attach {motor_object.fuel_type} motor without a transmission")
            time.sleep(1)

    def wheels_attachment(self, wheels_object):
        if self.wheels_attached == False:
            self.wheels_attachment_point = wheels_object
            self.wheels_attached = True
            print(f"{wheels_object} wheels were successfully attached to the {self.chassis_type} chassis")
            time.sleep(1)

        else:
            print(f"\nUnable to attach {wheels_object.size} wheels because there are other wheels already attached")
            time.sleep(1)


class Motor:
    motor_instances = []
    def __init__(self, fuel_type):
        Motor.motor_instances.append(self)
        self.fuel_type = fuel_type
        self.gearbox_placement = None
        self.transmission_attached = False
    def __str__(self):
        return self.fuel_type


    def attach_gearbox(self, gearbox_object):
        if self.gearbox_placement == None and self.transmission_attached is False:
            self.gearbox_placement = gearbox_object
            self.transmission_attached = True
            print(f"\n{gearbox_object.gearbox_type} transmission was successfully attached to the {self.fuel_type} motor")
            time.sleep(1)
        else:
            print(f"\nUnable to attach {gearbox_object.gearbox_type} transmission "
                  f"because other transmission is already attached to the {self.fuel_type} motor")
            time.sleep(1)

class Gearbox:
    gearbox_instances = []
    def __init__(self, gearbox_type):
        Gearbox.gearbox_instances.append(self)
        self.gearbox_type = gearbox_type

    def __str__(self):
        return self.gearbox_type

class Wheels:
    wheels_instances = []
    def __init__(self, size):
        Wheels.wheels_instances.append(self)
        self.size = size
    def __str__(self):
        return self.size


#motor init
gasoline_motor = Motor("M1. Gasoline")
diesel_motor = Motor("M2. Diesel")
natural_gas_motor = Motor("M3. Natural gas")

#transmission init
automatic_transmission = Gearbox("T1. Automatic")
manual_transmission = Gearbox("T2. Manual")


#chassis init
universal_chassis = Chassis("C1. Universal")
sedan_chassis = Chassis("C2. Sedan")
coupe_chassis = Chassis("C3. Coupe")

#wheels init
wheels_14_size = Wheels("W1. 14 size")
wheels_18_size = Wheels("W2. 18 size")
wheels_21_size = Wheels("W3. 21 size")

#available chassis print
print_available_parts()

#user inputs
def user_inputs():

    allowed_inputs = ["c1", "c2", "c3", "m1", "m2", "m3", "t1", "t2", "w1", "w2", "w3"]
    upper_list = list(map(str.upper, allowed_inputs))

    while True:
        user_input_1 = input('Please choose the first item C1-W3 (For available parts type "parts", for exit type "exit"): ')
        user_input_upper = user_input_1.upper()
        if user_input_upper == "exit".upper():
            time.sleep(1)
            print("\nYou were close!")
            time.sleep(2)
            print("Bye bye!".upper())
            exit()
        elif user_input_upper == "parts".upper():
            print_available_parts()
            user_inputs()
    # typo
        elif user_input_upper not in upper_list:
            print("Wrong input")
            user_inputs()

        user_input_2 = input("Please choose the item to attach:")
        user_input_2_upper = user_input_2.upper()

        if user_input_2_upper not in upper_list:
            print(f"'{user_input_2}' is not the right item")

    # transmission to motor
        if user_input_upper == "T1".upper() and user_input_2_upper == "M1".upper():
            gasoline_motor.attach_gearbox(automatic_transmission)
            print_current_state()
        elif user_input_upper == "T2".upper() and user_input_2_upper == "M2".upper():
            diesel_motor.attach_gearbox(manual_transmission)
            print_current_state()
        elif user_input_upper == "T3".upper() and user_input_2_upper == "M3".upper():
            natural_gas_motor.attach_gearbox(automatic_transmission)
            print_current_state()
        elif user_input_upper == "T2".upper() and user_input_2_upper == "M1".upper():
            gasoline_motor.attach_gearbox(manual_transmission)
            print_current_state()
        elif user_input_upper == "T1".upper() and user_input_2_upper == "M2".upper():
            diesel_motor.attach_gearbox(automatic_transmission)
            print_current_state()
        elif user_input_upper == "T2".upper() and user_input_2_upper == "M3".upper():
            natural_gas_motor.attach_gearbox(manual_transmission)
            print_current_state()

    # motor to chassis
        elif user_input_upper == "M1".upper() and user_input_2_upper == "C1".upper():
            universal_chassis.motor_attachment(gasoline_motor)
            print_current_state()
        elif user_input_upper == "M1".upper() and user_input_2_upper == "C2".upper():
            sedan_chassis.motor_attachment(gasoline_motor)
            print_current_state()
        elif user_input_upper == "M1".upper() and user_input_2_upper == "C3".upper():
            coupe_chassis.motor_attachment(gasoline_motor)
            print_current_state()
        elif user_input_upper == "M2".upper() and user_input_2_upper == "C1".upper():
            universal_chassis.motor_attachment(diesel_motor)
            print_current_state()
        elif user_input_upper == "M2".upper() and user_input_2_upper == "C2".upper():
            sedan_chassis.motor_attachment(diesel_motor)
            print_current_state()
        elif user_input_upper == "M2".upper() and user_input_2_upper == "C3".upper():
            coupe_chassis.motor_attachment(diesel_motor)
            print_current_state()
        elif user_input_upper == "M3".upper() and user_input_2_upper == "C1".upper():
            universal_chassis.motor_attachment(natural_gas_motor)
            print_current_state()
        elif user_input_upper == "M3".upper() and user_input_2_upper == "C2".upper():
            sedan_chassis.motor_attachment(natural_gas_motor)
            print_current_state()
        elif user_input_upper == "M3".upper() and user_input_2_upper == "C3".upper():
            coupe_chassis.motor_attachment(natural_gas_motor)
            print_current_state()

    # wheels to chassis
        elif user_input_upper == "W1".upper() and user_input_2_upper == "C1".upper():
            universal_chassis.wheels_attachment(wheels_14_size)
            print_current_state()
        elif user_input_upper == "W2".upper() and user_input_2_upper == "C1".upper():
            universal_chassis.wheels_attachment(wheels_18_size)
            print_current_state()
        elif user_input_upper == "W3".upper() and user_input_2_upper == "C1".upper():
            universal_chassis.wheels_attachment(wheels_21_size)
            print_current_state()
        elif user_input_upper == "W1".upper() and user_input_2_upper == "C2".upper():
            sedan_chassis.wheels_attachment(wheels_14_size)
            print_current_state()
        elif user_input_upper == "W2".upper() and user_input_2_upper == "C2".upper():
            sedan_chassis.wheels_attachment(wheels_18_size)
            print_current_state()
        elif user_input_upper == "W3".upper() and user_input_2_upper == "C2".upper():
            sedan_chassis.wheels_attachment(wheels_21_size)
            print_current_state()
        elif user_input_upper == "W1".upper() and user_input_2_upper == "C3".upper():
            coupe_chassis.wheels_attachment(wheels_14_size)
            print_current_state()
        elif user_input_upper == "W2".upper() and user_input_2_upper == "C3".upper():
            coupe_chassis.wheels_attachment(wheels_18_size)
            print_current_state()
        elif user_input_upper == "W3".upper() and user_input_2_upper == "C3".upper():
            coupe_chassis.wheels_attachment(wheels_21_size)
            print_current_state()

    # wrong order chassis-wheels
        elif ((user_input_upper == "C1".upper() or
              user_input_upper == "C3".upper())
              and
              (user_input_2_upper == "W1".upper() or
              user_input_2_upper == "W3".upper())):
            print("You cannot attach Chassis to Wheels!")
            print_current_state()


        elif ((user_input_upper == "C1".upper() or
              user_input_upper == "C2".upper())
              and
              (user_input_2_upper == "M1".upper() or
              user_input_2_upper == "M2".upper())):
            print("Oops! Chassis can't be attached directly to a motor (but motor does)!")
            print_current_state()

    # wrong order wheels-motor
        elif ((user_input_upper == "W1".upper() or
              user_input_upper == "W2".upper())
              and
              (user_input_2_upper == "M1".upper() or
              user_input_2_upper == "M2".upper())):
            print("You trying to create a motorized unicycle? You can't attach wheels directly to a motor!")
            print_current_state()

        elif ((user_input_upper == "M2".upper() or
              user_input_upper == "M3".upper())
              and
              (user_input_2_upper == "W2".upper() or
              user_input_2_upper == "W3".upper())):
            print("Are you sure? Motor to a wheel?!")
            print_current_state()

    # wrong order motor-transmission
        elif ((user_input_upper == "M1".upper() or
              user_input_upper == "M3".upper())
              and
              (user_input_2_upper == "T1".upper() or
              user_input_2_upper == "T3".upper())):
            print("Sorry, can't attach motor to a transmission!")
            print_current_state()

    # wrong order transmission-wheels
        elif ((user_input_upper == "T1".upper() or
              user_input_upper == "T3".upper())
              and
              (user_input_2_upper == "W1".upper() or
              user_input_2_upper == "W3".upper())):
            print("Transmission to wheels?")
            print_current_state()
    # wrong order wheels-transmission
        elif ((user_input_upper == "W1".upper() or
              user_input_upper == "W3".upper())
              and
              (user_input_2_upper == "T1".upper() or
              user_input_2_upper == "T3".upper())):
            print("Oh man...")
            print_current_state()
    # wrong order transmission-transmission
        elif ((user_input_upper == "T1".upper() or
              user_input_upper == "T3".upper())
              and
              (user_input_2_upper == "T1".upper() or
              user_input_2_upper == "T3".upper())):
            print("You will be first to invent a double transmission!")
            print_current_state()

    # wrong order motor-motor
        elif ((user_input_upper == "M1".upper() or
              user_input_upper == "M3".upper())
              and
              (user_input_2_upper == "M1".upper() or
              user_input_2_upper == "M3".upper())):
            print("Great choice!")
            print_current_state()

    # wrong order chassis - chassis
        elif ((user_input_upper == "C1".upper() or
              user_input_upper == "C3".upper())
              and
              (user_input_2_upper == "C1".upper() or
              user_input_2_upper == "C3".upper())):
            print("Not today!")
            print_current_state()
        else:
            print("Nope!") #wrong input


user_inputs()

#gearbox to motor
# gearbox_attachment_attempt = gasoline_motor.attach_gearbox(automatic_transmission)
# gearbox_attachment_attempt1 = gasoline_motor.attach_gearbox(automatic_transmission)
# gearbox_attachment_attempt2 = diesel_motor.attach_gearbox(automatic_transmission)
# gearbox_attachment_attempt3 = diesel_motor.attach_gearbox(automatic_transmission)

#motor to chassis
# motor_attachment_attempt = universal_chassis.motor_attachment(gasoline_motor)
# motor_attachment_attempt4 = universal_chassis.motor_attachment(gasoline_motor)
# motor_attachment_attempt2 = universal_chassis.motor_attachment(natural_gas_motor)
# motor_attachment_attempt3 = universal_chassis.motor_attachment(natural_gas_motor)
# motor_attachment_attempt5 = universal_chassis.motor_attachment(diesel_motor)


