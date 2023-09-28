from datetime import datetime

from db import DB


DATABASE_TABLE_SETUP = [
    """
    CREATE TABLE fonds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME
    );
    """,
    """
    CREATE TRIGGER update_fonds_timestamp
    AFTER UPDATE ON fonds
    FOR EACH ROW
    BEGIN
        UPDATE fonds SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
    END;
    """,
]

FONDS = [
    # {
    #     "id": 0,
    #     "name": "Groceries",
    #     "created_at": datetime.strptime("2023-09-24 09:10:11", "%Y-%m-%d %H:%M:%S"),
    #     "updated_at": datetime.strptime("2023-12-17 12:13:14", "%Y-%m-%d %H:%M:%S")
    # }
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
    
def post_fond(db: DB, fond):
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

