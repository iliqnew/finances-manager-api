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



def get_fond(fond_id):
        fond = DB().execute(
            "SELECT * FROM fonds WHERE id = (?)",
            (fond_id,)
        )
        return fond[0] if fond else {"error": f"Fond with id {fond_id} not found"}

def get_fonds():
     return DB().execute("SELECT * FROM fonds")
    
def post_fond(fond):
    FONDS.append(fond)
    DB().execute(
        """
        INSERT INTO fonds (name) VALUES (?);
        """,
        (fond["name"],)
    )

def put_fond(fond_id, new_fond):
    DB().execute(
        f"""
        UPDATE
            fonds
        SET
            {", ".join([key.__repr__() + " = ?" for key in new_fond.keys()])}
        WHERE
            id = ?
        """,
        (*list(new_fond.values()), fond_id)
    )

