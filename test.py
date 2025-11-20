class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)





Jillian = Hero("Jillian", 150, ["Potion"])
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)

goku=Hero("Goku", 627, ["Needle"])
goku.buy
    