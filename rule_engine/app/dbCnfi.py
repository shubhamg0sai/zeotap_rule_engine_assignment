import sqlite3
from typing import List, Tuple, Any
from contextlib import contextmanager
import logging
import json
from pathlib import Path

# Configure logging
logger = logging.getLogger(__name__)

class DatabaseError(Exception):
    """Custom exception for database-related errors."""
    pass

class Database:
    """Database handler for Rule Engine."""

    def __init__(self, db_path: str = 'database_init.db'):
        """Initialize database handler and schema."""
        self.db_path = Path(db_path)
        self.initialize_database()

    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row  # Enable named columns
            yield conn
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {e}")
            raise DatabaseError(f"Failed to connect to database: {e}")
        finally:
            conn.close()

    def initialize_database(self) -> None:
        """Initialize database schema if it doesn't exist."""
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL,
            ast TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
        try:
            with self.get_connection() as conn:
                conn.execute(create_table_sql)
                logger.info("Database initialized successfully")
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise DatabaseError(f"Failed to initialize database: {e}")

    def load_rules(self) -> List[Tuple[str, Any]]:
        """Load all rules from database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT rule_string, ast FROM rules ORDER BY created_at DESC")
                rules = [(row['rule_string'], json.loads(row['ast'])) for row in cursor.fetchall()]
                logger.debug(f"Loaded {len(rules)} rules from database")
                return rules
        except sqlite3.Error as e:
            logger.error(f"Failed to load rules: {e}")
            raise DatabaseError(f"Failed to load rules: {e}")

    def save_rule(self, rule_string: str, ast: Any) -> int:
        """Save a new rule to the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO rules (rule_string, ast) VALUES (?, ?)", 
                               (rule_string, json.dumps(ast)))
                conn.commit()
                rule_id = cursor.lastrowid
                logger.info(f"Saved rule with ID: {rule_id}")
                return rule_id
        except sqlite3.Error as e:
            logger.error(f"Failed to save rule: {e}")
            raise DatabaseError(f"Failed to save rule: {e}")

    def get_rule_by_id(self, rule_id: int) -> Tuple[str, Any]:
        """Retrieve a specific rule by ID."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT rule_string, ast FROM rules WHERE id = ?", (rule_id,))
                row = cursor.fetchone()
                return (row['rule_string'], json.loads(row['ast'])) if row else None
        except sqlite3.Error as e:
            logger.error(f"Failed to get rule {rule_id}: {e}")
            raise DatabaseError(f"Failed to get rule {rule_id}: {e}")

# Create database instance
db = Database()

# For backward compatibility
initialize_database = db.initialize_database
load_rules = db.load_rules
save_rule = db.save_rule
