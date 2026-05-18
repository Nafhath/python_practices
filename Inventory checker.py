product1 = {
    "name": "Laptop",
    "price": 999.99,
    "quantity": 10,
    "category": "Electronics"
}
product2 = {
    "name": "Smartphone",
    "price": 499.99,
    "quantity": 20,
    "category": "Electronics"
}
product3 = {
    "name": "Headphones",
    "price": 199.99,
    "quantity": 15,
    "category": "Electronics"
}
products = [product1, product2, product3]
 
def check_inventory(products):
    highest_amount = 0
    highest_amount_product = ""
    lowest_amount = 0
    lowest_amount_product = ""
    category = {"Electronics": 0}
    for product in products:
        print(f"Product: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Category: {product['category']}\n")
        print(f"Total Value: ${product['price'] * product['quantity']:.2f}\n")
        
        if product["price"] > highest_amount:
            highest_amount = product["price"]
            highest_amount_product = product["name"]
        if lowest_amount == 0 or product["price"] < lowest_amount:
            lowest_amount = product["price"]
            lowest_amount_product = product["name"]
        if product["quantity"] < 5:
            print("This product is low in stock!\n")
        if product["category"] not in category:
            category[product["category"]] = product["price"] * product["quantity"] 
        else:
            category[product["category"]] += product["price"] * product["quantity"]
    
    print(f"Highest Priced Product: {highest_amount_product} - ${highest_amount:.2f}")
    print(f"Lowest Priced Product: {lowest_amount_product} - ${lowest_amount:.2f}")
    highest_category = max(category, key=category.get)
    print(f"Category with Highest Total Value: {highest_category} - ${category[highest_category]:.2f}")
    for category_name, total_value in category.items():
        print(f"Total value of {category_name} category: ${total_value:.2f}")
    
check_inventory(products)