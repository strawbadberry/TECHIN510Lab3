import sqlite3

def create_connection():
    conn = sqlite3.connect('todo.db')
    return conn

def create_table():
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute(""" CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT,
                        state TEXT
                      ); """)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def add_task(task):
    conn = create_connection()
    sql = ''' INSERT INTO tasks(name, description, state)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = create_connection()
    sql = 'SELECT * FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    tasks = cur.fetchall()
    conn.close()
    return tasks

def update_task_state(id, new_state):
    conn = create_connection()
    sql = ''' UPDATE tasks
              SET state = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (new_state, id))
    conn.commit()
    conn.close()

def delete_task(id):
    conn = create_connection()
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    conn.close()

# Initialize the database and table
create_table()
