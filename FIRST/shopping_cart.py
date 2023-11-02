class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price):
        self.items.append({'name': item_name, 'price': price})

    def apply_discount(self, item_name, discount_percentage):
        for item in self.items:
            if item['name'] == item_name:
                item['price'] = item['price'] - (item['price'] * discount_percentage / 100)
                break

    def get_total_cost(self):
        total = 0.0
        for item in self.items:
            total += item['price']
        return total

    def get_items(self):
        return self.items

    def remove_item(self, item_name):
        item_found = False
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                item_found = True
                break

        if not item_found:
            raise ValueError("The article to be deleted does not exist in the shopping cart.")

    def clear_cart(self):
        self.items = []

    def item_exists(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                return True
        return False
