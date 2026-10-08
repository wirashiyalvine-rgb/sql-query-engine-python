import sqlite3
import logging
from typing import List, Tuple, Optional

# Configure structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DatabaseEngine:
    def __init__(self, db_name: str = ":memory:"):
        """Initialize database connection."""
        self.db_name = db_name
        self.connection: Optional[sqlite3.Connection] = None
        self.connect()

    def connect(self) -> None:
        """Establish database connection."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            logging.info(f"Connected successfully to database: {self.db_name}")
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            raise

    def initialize_schema(self) -> None:
        """Create sample tables with constraints."""
        query = """
        CREATE TABLE IF NOT EXISTS developers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            language TEXT NOT NULL,
            experience_years INTEGER CHECK(experience_years >= 0)
        );
        """
        self.execute_query(query)
        logging.info("Schema initialized successfully.")

    def execute_query(self, query: str, params: Tuple = ()) -> None:
        """Execute non-fetching SQL queries securely using parameters."""
        if not self.connection:
            raise RuntimeError("No active database connection.")
        try:
            with self.connection:
                self.connection.execute(query, params)
        except sqlite3.Error as e:
            logging.error(f"Query execution failed: {e}")
            raise

    def fetch_all(self, query: str, params: Tuple = ()) -> List[Tuple]:
        """Fetch results from a parameterized SELECT query."""
        if not self.connection:
            raise RuntimeError("No active database connection.")
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Data fetch failed: {e}")
            return []

    def close(self) -> None:
        """Close connection cleanly."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")


if __name__ == "__main__":
    db = DatabaseEngine()
    db.initialize_schema()

    # Insert test data using parameterized queries
    devs = [
        ("Alvine", "Python", 4),
        ("Jackson", "C++", 3),
        ("Sarah", "SQL", 5)
    ]
    
    for dev in devs:
        db.execute_query("INSERT INTO developers (name, language, experience_years) VALUES (?, ?, ?);", dev)

    # Query records
    results = db.fetch_all("SELECT * FROM developers WHERE experience_years >= ?;", (3,))
    print("\n--- Developer Records ---")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Tech: {row[2]} | Experience: {row[3]} yrs")

    db.close()
