#Pet Shop Application
#Acts like a mini inventory system
#Use what we have learned so far

"""
Imports
Class
--init
--addd
--remove
--display
--save
--load
Main
Test
"""
#Import
import json
import os.path

#Inventory class
class Inventory:
    pets = {}

    def __init__(self):
        self.load()

    def add(self,key,quantity):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v + quantity
        else:
            q = quantity
        self.pets[key] = q
        print(f'Add {quantity} {key} : total = {self.pets[key]}')
        

    def remove(self,key,quantity):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v - quantity
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'Removed {quantity} {key} : total = {self.pets[key]}')

    def display(self):
        for key, value in self.pets.items():
            print(f'{key} = {value}')

    def save(self):
        print('Saving inventory')
        with open('inventory.txt', 'w') as f:
            json.dump(self.pets,f)
        print('Saved!')

    def load(self):
        print('Loading inventory')
        if not os.path.exists('inventory.txt'):
            print('Skip, nothing to load')
            return
        with open('inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('Loaded!')

def main():
    inv = Inventory()

    while True:
        action = input('''Actions: 
- add
- remove
- list I have
- save
- exit
Choose what action you want: ''')
        if action =='exit':
            break
        if action =='add' or action == 'remove':
                key = input('Enter an animal: ')
                quantity = int(input('Enter the quantity: '))
                if action == 'add':
                    inv.add(key,quantity)
                if action == 'remove':
                    inv.remove(key,quantity)
        if action =='list I have':
            inv.display()
        if action =='save':
            inv.save()

    inv.save()


if __name__ == "__main__":
    main()