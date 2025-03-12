import csv
import os


class PriceList:
    """
    A singleton class to manage product prices loaded from a CSV file.

    Attributes:
        current_dir (str): The directory where the current file is located.
        pricelist (dict): A dictionary to store product IDs, names, and their prices.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Ensures that only one instance of the PriceList class is created.

        Returns:
            PriceList: The singleton instance of the PriceList class.
        """
        if not cls._instance:
            cls._instance = super(PriceList, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, filename="price_list.csv"):
        """
        Initializes the PriceList instance and loads pricelist from the specified CSV file.

        Args:
            filename (str): The name of the CSV file to load pricelist from. Defaults to "pricelist.csv".
        """
        self.current_dir = os.path.dirname(__file__)
        self.pricelist = {}
        self.load_pricelist(filename)

    def load_pricelist(self, filename):
        """
        Loads pricelist and their prices from a CSV file.

        Args:
            filename (str): The name of the CSV file to load pricelist from.
        """
        with open(os.path.join(self.current_dir, filename), mode="r") as file:
            reader = csv.reader(file)
            for rows in reader:
                if len(rows) < 3:
                    continue  # Skip rows that don't have enough columns
                product_id = rows[0]
                self.pricelist[product_id] = {"name": rows[1], "price": float(rows[2])}

    def save_pricelist(self, filename):
        """
        Saves the current pricelist and their prices to a CSV file.

        Args:
            filename (str): The name of the CSV file to save pricelist to.
        """
        with open(os.path.join(self.current_dir, filename), mode="w") as file:
            writer = csv.writer(file)
            for product_id, details in self.pricelist.items():
                writer.writerow([product_id, details["name"], details["price"]])

    def get_price(self, product_id):
        """
        Returns the price of the specified product.

        Args:
            product_id (str): The ID of the product to get the price for.

        Returns:
            float: The price of the product, or None if the product is not found.
        """
        return self.pricelist.get(product_id, {}).get("price", None)

    def set_price(self, product_id, price):
        """
        Sets the price of the specified product.

        Args:
            product_id (str): The ID of the product to set the price for.
            price (float): The price to set for the product.
        """
        if product_id in self.pricelist:
            self.pricelist[product_id]["price"] = price

    def get_pricelist(self):
        """
        Returns the dictionary of all pricelist and their prices.

        Returns:
            dict: A dictionary of product IDs, names, and their prices.
        """
        return self.pricelist

    def print_pricelist(self):
        """
        Prints the list of all products with their IDs, names, and prices.
        """
        for product_id, details in self.pricelist.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}")

# Example usage:
if __name__ == "__main__":
    price_list = PriceList()
    price_list.print_pricelist()
