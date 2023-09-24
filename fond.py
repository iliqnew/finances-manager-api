from datetime import datetime


FONDS = [
    {
        "id": 0,
        "name": "Groceries",
        "created_at": datetime.strptime("2023-09-24 09:10:11", "%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.strptime("2023-12-17 12:13:14", "%Y-%m-%d %H:%M:%S")
    }
]


LAST_FOND_ID = 0


class FondNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_fond(db, fond_id):
        fond = list(filter(lambda x: x["id"] == fond_id, FONDS))
        if not fond:
            raise FondNotFoundError(f"Fond id {fond_id} not found")
        return fond[0]

def get_fonds(db):
     return FONDS
    
def post_fond(db, fond):
    global LAST_FOND_ID
    creation_timestamp = datetime.now()
    fond.update(
        {
            "id": (LAST_FOND_ID := LAST_FOND_ID + 1),
            "created_at": creation_timestamp,
            "updated_at": creation_timestamp,
        }
    )
    FONDS.append(fond)
    return fond

def put_fond(db, fond_id, new_fond):
    global LAST_FOND_ID
    old_fond = get_fond(db, fond_id)
    fond = old_fond
    fond.update(
        {
            **new_fond,
            "updated_at": datetime.now()
        }
    )
    FONDS.remove(old_fond)
    FONDS.append(fond)
    return fond

