#
# class User:
#     pass
# peter = User()
# peter.name = "Petja Robinsov"
# peter.age = 36
#
# julia = User()
# julia.name = "Julia Donaldos"
# julia.age = 89
# julia.height = 189
#
# print(peter.name, peter.age)
# print(julia.name, julia.height)
#
# class Car:
#     number_of_wheels = 4
#     motor = True
#     frame = True
#     passengers = 5
# vw_passat = Car()
# print(vw_passat.motor, vw_passat.frame, vw_passat.passengers)
# vw_golf = Car()
# print(vw_golf.motor, vw_golf.number_of_wheels)
#
#
# class Car:
#     def __init__(self, number_of_wheels, motor, frame, passengers):
#         self.rr = motor
#         self.number_of_wheels = number_of_wheels
#         self.frame = frame
#         self.passengers = passengers
#
# vw_passat = Car(number_of_wheels=4, motor=True, frame=True, passengers=5)
# print(vw_passat.number_of_wheels, vw_passat.passengers, vw_passat.rr)

# class Product:
#     def __init__(self, name, category, quantity, vol):
#         self.name = name
#         self.category = category
#         self.quantity = quantity
#         self.vol = vol
#
#     def is_available(self):
#         return True if self.quantity > 4 else False
#
# double_bock = Product(name="Double bock", category="beer", quantity=5, vol="8%")
# print(double_bock.quantity, double_bock.vol)
# print(double_bock.is_available())

class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.event_type = event_type
        self.session_id = session_id

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)
    print(event_obj.event_type)