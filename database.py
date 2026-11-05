import sqlite3

DATABASE_NAME = "placeready.db"


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


def save_assessment(category, score, total):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO assessments (category, score, total)
        VALUES (?, ?, ?)
    """, (category, score, total))

    connection.commit()
    connection.close()


def get_assessments():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category, score, total, date
        FROM assessments
        ORDER BY id DESC
    """)

    records = cursor.fetchall()
    connection.close()
    return records


def clear_assessments():
    """Delete all assessment history without deleting practice tasks."""
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM assessments")

    connection.commit()
    connection.close()


def add_task(task_name):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (task_name) VALUES (?)",
        (task_name,)
    )

    connection.commit()
    connection.close()


def get_tasks():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, task_name, completed
        FROM tasks
        ORDER BY id
    """)

    records = cursor.fetchall()
    connection.close()
    return records


def update_task(task_id, completed):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET completed = ?
        WHERE id = ?
    """, (1 if completed else 0, task_id))

    connection.commit()
    connection.close()


def delete_task(task_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("PlaceReady database created successfully!")
