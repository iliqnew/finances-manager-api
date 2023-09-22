from datetime import datetime


TRANSACTIONS = [
    {
        "id": 0,
        "source_fond_id": 0,
        "source_fond": "Groceries",
        "target_fond_id": None,
        "target_fond": None,
        "amount": 100,
        "comment": "test",

        "created_at": "2023-09-23 01:54:32",
        "updated_at": "2023-09-23 01:54:32"
    }
]


LAST_TRANSACTION_ID = 0


class TransactionNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_transaction(db, transaction_id):
        transaction = list(filter(lambda x: x["id"] == transaction_id, TRANSACTIONS))
        if not transaction:
            raise TransactionNotFoundError(f"transaction id {transaction_id} not found")
        return transaction[0]
    
def post_transaction(db, transaction):
    global LAST_TRANSACTION_ID
    creation_timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    transaction.update(
        {
            "id": (LAST_TRANSACTION_ID := LAST_TRANSACTION_ID + 1),
            "created_at": creation_timestamp,
            "updated_at": creation_timestamp,
        }
    )
    TRANSACTIONS.append(transaction)
    return transaction

def put_transaction(db, transaction_id, new_transaction):
    global LAST_TRANSACTION_ID
    old_transaction = get_transaction(db, transaction_id)
    transaction = old_transaction
    transaction.update(
        {
            **new_transaction,
            "updated_at": datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        }
    )
    TRANSACTIONS.remove(old_transaction)
    TRANSACTIONS.append(transaction)
    return transaction
