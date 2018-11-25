import sqlite3


def db_init_():
    conn = sqlite3.connect("task_list.sqlite")
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        sql = f.read()

    cursor.executescript(sql)
    conn.commit()
    conn.close()


def select_all_info():
    conn = sqlite3.connect("task_list.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM tasks"

    result = cursor.executescript(sql).fetchall()
    conn.commit()
    conn.close()

    return result


def insert_task(task_name):
    conn = sqlite3.connect("task_list.sqlite")
    cursor = conn.cursor()

    sql = "INSERT INTO tasks (done,task_name) VALUES (?, ?)"

    cursor.execute(sql, ('[Undone]', task_name))
    conn.commit()
    conn.close()


def update_done(task_name):
    conn = sqlite3.connect("task_list.sqlite")
    cursor = conn.cursor()

    sql = "UPDATE tasks SET done = '[Done]' WHERE task_name = ?"

    cursor.execute(sql, task_name)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    db_init_()
