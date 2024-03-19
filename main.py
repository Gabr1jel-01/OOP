class Item:
    #init je konstruktor metoda koja se pokrece automatski kod kreiranja instance klase
    def __init__(self,name,price,quantity=0):   #kada stavim nulu pod atribut metode to mi dozvoljava da ne moram ispuniti taj atribut pri stvaranju instance klase
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def calculate_total_price(self):
        return self.price * self.quantity
        
        
        
        
        
        
item1 = Item("Phone", 100, 4)


item1.has_numpad = False

print(item1.has_numpad) #ovom linijom sam dodao jos jedan atribut u metodu __init__. To sto nije dodana gore pri kreiranju ne znaci da ne mogu nekada poslije dodati
