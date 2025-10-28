# Creator: Khady Gueye

""" THis program give you information about computers. """


class Computer:
    def __init__(self,manufacturer,model,processor,ram,display_size):
        #TODO_1: Define the constructor of the Base class 'Computer'
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size

    def print_info(self):
        #TODO_2: Define this method. It should print all the data attributes of a given 'Computer' object
        print(f"Manufacturer: {self.manufacturer}, Model: {self.model}, Processor: {self.processor}, RAM: {self.ram}, Display: {self.display_size}")

class Laptop(Computer):
    def __init__(self,manufacturer, model, processor, ram, display_size, weight, is_touch_screen):
        #TODO_3: Define the constructor of the derived class 1 (Laptop)
        super().__init__(manufacturer, model, processor, ram, display_size)
        self.weight = weight
        self.is_touch_screen = is_touch_screen


    def print_info(self):
        #TODO_4: this method should print all the data attributes of a 'Laptop' object
        super().print_info()
        print(f"Weight: {self.weight}, Touch-screen: {self.is_touch_screen}")

class Desktop(Computer):
    def __init__(self, manufacturer, model, processor, ram, display_size, desktop_type):
        # TODO_5: Define the constructor of the derived class 2 (Desktop)
        super().__init__(manufacturer, model, processor, ram, display_size)
        self.desktop_type = desktop_type
   
    def print_info(self):
        #TODO_6: this method should print all the data attributes of the 'Desktop' object
        super().print_info()
        print(f"Type: {self.desktop_type}")

# driver code. No modification is necessary after this line.
computer1 = Laptop('Apple', 'MacBook Air', 'Apple M1', '16GB', '13.3"', '2.7 lbs', False)
computer2 = Laptop('HP', 'Envy', 'core i5', '8GB', '15.6"', '4lbs', True)
computer3 = Desktop('Dell', 'Inspiron', 'core i7', '32GB', '27"', 'All-in-One')
computer1.print_info()
computer2.print_info()
computer3.print_info()
