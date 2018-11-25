import db


def task_list_display():
    for task_info in db.select_all_info():
        print(f"{task_info[0]}: {task_info[1]} {task_info[2]}")


def task_select_display(select_value):
    for task_info in db.select_info(select_value):
        print(f"{task_info[0]}: {task_info[1]} {task_info[2]}")


def add_new_task(new_task):
    db.insert_task(new_task)


def done_task(task):
    db.update_done(task)


if __name__ == "__main__":
    task_list_display()