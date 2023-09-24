from datetime import datetime


TRANSACTIONS = [
    {
        "id": 0,
        "source_fond_id": 0,
        "source_fond": "Groceries",
        "source_fond_payment_method_id": 0,
        "target_fond_id": None,
        "target_fond": None,
        "source_fond_payment_method_id": 0,
        "amount": 100,
        "comment": "test",

        "created_at": datetime.strptime("2023-09-23 01:54:32", "%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.strptime("2023-09-23 01:54:32", "%Y-%m-%d %H:%M:%S")
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

def get_transactions(db):
    return TRANSACTIONS

def post_transaction(db, transaction):
    global LAST_TRANSACTION_ID
    creation_timestamp = datetime.now()
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
            "updated_at": datetime.now()
        }
    )
    TRANSACTIONS.remove(old_transaction)
    TRANSACTIONS.append(transaction)
    return transaction
