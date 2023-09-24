from datetime import datetime
import calendar

from fond import (
    get_fonds
)
from transaction import (
    get_transactions
)

def get_expenses(db):
    fonds = get_fonds(db)
    transactions = get_transactions(db)
    earliest_year = min(list(transaction["created_at"] for transaction in transactions), default=datetime.now()).year
    return [
        {
            **fond,
            "historical_data": [
                {
                    "year": year,
                    "months": [
                        [
                            calendar.month_name[month],
                            sum(
                                map(
                                    lambda x: x["amount"],
                                    filter(
                                        lambda x:
                                            datetime(year, month, 1, 0, 0, 0) <= x["created_at"] < datetime(year, month+1, 1, 0, 0, 0)
                                            and x["target_fond_id"] == fond["id"],
                                        transactions
                                    )
                                )
                            )
                            - sum(
                                map(
                                    lambda x: x["amount"],
                                    filter(
                                        lambda x:
                                            datetime(year, month, 1, 0, 0, 0) <= x["created_at"] < datetime(year, month+1, 1, 0, 0, 0)
                                            and x["source_fond_id"] == fond["id"],
                                        transactions
                                    )
                                )
                            )
                        ]
                        for month in range(1, 13)
                    ]
                }
                for year in range(earliest_year, datetime.now().year + 1)
            ]
        }
        for fond in fonds
    ]

