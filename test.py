class Hero:
    """
    Represents a hero character with money, health, and an inventory.
    """
    def __init__(self, name: str, starting_money: int, initial_item: str):
        """
        Initializes the Hero object.


        Args:
            name (str): The name of the hero.
            starting_money (int): The hero's initial amount of gold/money.
            initial_item (str): The first item in the hero's inventory.
        """
        self.name = name
        self.money = starting_money
        self.inventory = [initial_item]
        print(f"--- Hero Created ---\nName: {self.name}\nMoney: {self.money} gold\nInventory: {self.inventory}")


    def buy(self, item_name: str, cost: int):
        """
        Attempts to buy an item and add it to the inventory.


        Args:
            item_name (str): The name of the item to buy.
            cost (int): The cost of the item.
        """
        print(f"\n--- Attempting Purchase: {item_name} for {cost} gold ---")
       
        if self.money >= cost:
            self.money -= cost
            self.inventory.append(item_name)
            print(f"SUCCESS! {self.name} bought a {item_name}.")
        else:
            print(f"FAILURE! {self.name} does not have enough gold to buy the {item_name}.")
       
        self.display_status()


    def display_status(self):
        """Displays the hero's current status."""
        print(f"\n--- {self.name}'s Current Status ---")
        print(f"Remaining Gold: {self.money}")
        print(f"Inventory: {', '.join(self.inventory)}")


# --- Demonstration ---


# 1. Create the Hero object
hero_name = "Aethan, the Exile"
start_gold = 100
starting_item = "Worn Leather Armor"
aethan = Hero(hero_name, start_gold, starting_item)


# 2. Use the .buy() method to add a new item
new_item_name = "Healing Potion"
item_cost = 25
aethan.buy(new_item_name, item_cost)


# 3. Try to buy an expensive item to test the failure case
expensive_item_name = "Enchanted Sword"
expensive_cost = 200
aethan.buy(expensive_item_name, expensive_cost)



