import sqlite3
from dataclasses import dataclass

class Database:
    def __init__(self, nome):
        self.conn = sqlite3.connect("data/" + nome + '.db')
        self.cur = self.conn.cursor()
        comando = """
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT NOT NULL
            );
        """
        self.cur.execute(comando)
    
    def add(self, note):
        comando = f"""
            INSERT INTO note (title, content) VALUES
                (
                    '{note.title}',
                    '{note.content}'
                );
        """
        self.conn.execute(comando)
        self.conn.commit()
        
    def get_all(self):
        comando = f"""
            SELECT id, title, content FROM note;
        """
        cursor = self.conn.execute(comando)
        # self.conn.commit()
        notes = [Note(id = linha[0], title = linha[1], content=linha[2]) for linha in cursor]
        return notes

    def update(self, entry):
        comando = f"""
            UPDATE note SET
                title = '{entry.title}', content = '{entry.content}'
                WHERE id = {entry.id}
        """
        self.conn.execute(comando)
        self.conn.commit()
    
    def delete(self, note_id):
        comando = f"""
            DELETE FROM note WHERE
                id = {note_id}
        """
        self.conn.execute(comando)
        self.conn.commit()
    
@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''