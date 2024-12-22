def get_customer_transactions(db):
    result = db['customers'].aggregate([
        {
            "$lookup": {
                "from": "bonus_cards",
                "localField": "bonus_cards",
                "foreignField": "card_id",
                "as": "cards_info"
            }
        },
        {
            "$unwind": "$cards_info"
        },
        {
            "$lookup": {
                "from": "transactions",
                "localField": "cards_info.transactions",
                "foreignField": "transaction_id",
                "as": "transactions_info"
            }
        }
    ])
    return list(result)

def get_total_points(db):
    result = db['customers'].aggregate([
        {
            "$lookup": {
                "from": "bonus_cards",
                "localField": "bonus_cards",
                "foreignField": "card_id",
                "as": "cards_info"
            }
        },
        {
            "$addFields": {
                "total_points": {"$sum": "$cards_info.points"}
            }
        },
        {
            "$project": {
                "name": 1,
                "total_points": 1
            }
        }
    ])
    return list(result)
