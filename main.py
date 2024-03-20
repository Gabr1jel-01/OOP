import csv

class Item:
    pay_rate = 0.8 # The pay rate after after 20% discount
    all = []
    #init je konstruktor metoda koja se pokrece automatski kod kreiranja instance klase
    def __init__(self,name: str,price: float, quantity=0):   #kada stavim nulu pod atribut metode to mi dozvoljava da ne moram ispuniti taj atribut pri stvaranju instance klase
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self): # U ovu metodu ne trebam stavljati parametre osim self zato sto mi self omogucava da pristupim atributima u konstruktor init metodi
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate       
        
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    
    @staticmethod        
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e; 5.0, 2.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            pass


class Phone(Item):
    pass





        
phone1 = Phone("jscPhonev10", 500, 5)
phone1.broken_phones = 1

phone2 = Phone("jscPhonev20", 700, 5)
phone2.broken_phones = 1

