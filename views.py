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
    data = []
    for fond in fonds:
        fond = {
            ** fond,
            "historical_data": []
        }
        for year in range(earliest_year, datetime.now().year + 1):
            yearly_data = {
                "year": year,
                "months": []
            }
            for month in range(1, 13):
                raw_monthly_data = list(filter(
                    lambda x:
                        datetime(year, month, 1, 0, 0, 0) <= x["created_at"] < datetime(year, month+1, 1, 0, 0, 0),
                    transactions
                ))
                yearly_data["months"].append({
                    "month": calendar.month_name[month],
                    "charges": (fond_charges := 
                        sum(
                            map(
                                lambda x: x["amount"],
                                filter(
                                    lambda x:
                                        x["target_fond_id"] == fond["id"],
                                    raw_monthly_data
                                )
                            )
                        )
                    ),
                    "expenses": (fond_expenses :=
                        sum(
                            map(
                                lambda x: x["amount"],
                                filter(
                                    lambda x:
                                        x["source_fond_id"] == fond["id"],
                                    raw_monthly_data
                                )
                            )
                        )
                    ),
                    "total": fond_charges - fond_expenses
                })

            fond["historical_data"].append(yearly_data)
        data.append(fond)
    return data

