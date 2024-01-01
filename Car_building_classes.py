class Chassis:
    def __init__(self, chassis_type):
        self.chassis_type = chassis_type
        self.motor_placement = None
        self.motor_attached = False

    def __str__(self):
        return self.chassis_type

    def motor_attachment(self, motor_object):
        if motor_object.gearbox_placement is not None:
            if self.motor_placement == None and self.motor_attached is False:
                self.motor_placement = motor_object
                self.motor_attached = True
                print(f"{motor_object} motor was successfully attached to the chassis")
            else:
                print(f"Unable to attach {motor_object.fuel_type} motor because other motor is already attached")
        else:
            print(f"Unable to attach {motor_object.fuel_type} motor because transmission is not attached")
class Motor:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.gearbox_placement = None
        self.transmission_attached = False
    def __str__(self):
        return self.fuel_type


    def attach_gearbox(self, gearbox_object):
        if self.gearbox_placement == None and self.transmission_attached is False:
            self.gearbox_placement = gearbox_object
            self.transmission_attached = True
            print(f"{gearbox_object.gearbox_type} transmission is successfully attached to the {self.fuel_type} motor")
        else:
            print(f"Unable to attach {gearbox_object.gearbox_type} transmission "
                  f"because other transmission is already attached to the {self.fuel_type} motor")

class Gearbox:
    def __init__(self, gearbox_type):
        self.gearbox_type = gearbox_type


#motor init
gasoline_motor = Motor("Gasoline")
diesel_motor = Motor("Diesel")
natural_gas_motor = Motor("Natural gas")

#transmission init
automatic_transmission = Gearbox("Automatic")
manual_transmission = Gearbox("Manual")

#chassis init
universal_chassis = Chassis("Universal")
sedan_chassis = Chassis("Sedan")
coupe_chassis = Chassis("Coupe")

#gearbox attachment
# gearbox_attachment_attempt = gasoline_motor.attach_gearbox(automatic_transmission)
# gearbox_attachment_attempt1 = gasoline_motor.attach_gearbox(automatic_transmission)
gearbox_attachment_attempt2 = diesel_motor.attach_gearbox(automatic_transmission)
# gearbox_attachment_attempt3 = diesel_motor.attach_gearbox(automatic_transmission)

#motor attachment
# motor_attachment_attempt = universal_chassis.motor_attachment(gasoline_motor)
# motor_attachment_attempt4 = universal_chassis.motor_attachment(gasoline_motor)
# motor_attachment_attempt2 = universal_chassis.motor_attachment(natural_gas_motor)
# motor_attachment_attempt3 = universal_chassis.motor_attachment(natural_gas_motor)
motor_attachment_attempt5 = universal_chassis.motor_attachment(diesel_motor)
