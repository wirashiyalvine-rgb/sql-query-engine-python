# Python SQL Query Engine & Database Utility

A modular, production-ready Python utility demonstrating relational database management, parameterized SQL query execution, and structured error handling using SQLite/PostgreSQL principles.

## Features
- Safe parameterized query execution to prevent SQL injection vulnerabilities.
- Automated relational schema initialization and transactional rollback on failure.
- Robust exception handling (`try/except/finally`) ensuring proper connection closing.

## Tech Stack
- Language: Python 3.10+
- Database: SQLite3 / PostgreSQL compatible
- Libraries: `sqlite3`, `logging`, `typing`

## How to Run
```bash
# Clone the repository
git clone [https://github.com/your-username/sql-query-engine-python.git](https://github.com/your-username/sql-query-engine-python.git)

# Navigate into directory
cd sql-query-engine-python

# Execute script
python main.py
