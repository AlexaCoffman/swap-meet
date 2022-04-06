from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    

    def get_by_category(self, category):
        self.category = category
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)
                
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        vendor.inventory.append(my_item)
        vendor.inventory.remove(their_item)

        return True