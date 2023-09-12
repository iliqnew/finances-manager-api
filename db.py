
class DB:
    def get_fond(self, fond_id):
        return {
            "id": int(fond_id),
            "name": "Groceries",
            "balance": 120.34,
            "created_at": "2023-09-24 09:10:11",
            "updated_at": "2023-12-17 12:13:14",
            "payment_method": "Credit/debit card"
        }
