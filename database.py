def initialize_database(client):
    db = client['supermarket_bonus_system']

    # Створення колекцій
    customers = db['customers']
    bonus_cards = db['bonus_cards']
    transactions = db['transactions']
    products = db['products']
    stores = db['stores']

    # Наповнення даними
    customers.insert_many([
        {
            "customer_id": 1,
            "name": "Іван Петренко",
            "phone": "+380501234567",
            "email": "ivan.petrenko@gmail.com",
            "bonus_cards": [1001, 1002]
        },
        {
            "customer_id": 2,
            "name": "Олена Коваль",
            "phone": "+380631234567",
            "email": "olena.koval@gmail.com",
            "bonus_cards": [1003]
        }
    ])

    bonus_cards.insert_many([
        {"card_id": 1001, "customer_id": 1, "points": 150, "transactions": [2001, 2002]},
        {"card_id": 1002, "customer_id": 1, "points": 75, "transactions": []},
        {"card_id": 1003, "customer_id": 2, "points": 200, "transactions": [2003]},
    ])

    transactions.insert_many([
        {"transaction_id": 2001, "card_id": 1001, "store_id": 3001, "products": [{"product_id": 4001, "quantity": 2}, {"product_id": 4002, "quantity": 1}], "total_amount": 500},
        {"transaction_id": 2002, "card_id": 1001, "store_id": 3002, "products": [{"product_id": 4003, "quantity": 3}], "total_amount": 300},
        {"transaction_id": 2003, "card_id": 1003, "store_id": 3001, "products": [{"product_id": 4002, "quantity": 1}, {"product_id": 4004, "quantity": 4}], "total_amount": 700},
    ])

    products.insert_many([
        {"product_id": 4001, "name": "Молоко", "price": 25},
        {"product_id": 4002, "name": "Хліб", "price": 30},
        {"product_id": 4003, "name": "Сир", "price": 100},
        {"product_id": 4004, "name": "Шоколад", "price": 50},
    ])

    stores.insert_many([
        {"store_id": 3001, "name": "Сільпо", "address": "Київ, вул. Хрещатик, 1"},
        {"store_id": 3002, "name": "АТБ", "address": "Київ, вул. Лесі Українки, 10"},
    ])
    print("Database initialized successfully!")
