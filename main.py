from config import get_client
from database import initialize_database
from queries import get_customer_transactions, get_total_points

if __name__ == "__main__":

    client = get_client()
    db = client['supermarket_bonus_system']


    initialize_database(client)


    print("Транзакції клієнтів:")
    transactions = get_customer_transactions(db)
    for t in transactions:
        print(t)

    print("\nЗагальна кількість бонусів у клієнтів:")
    points = get_total_points(db)
    for p in points:
        print(p)
