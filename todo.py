import db


class Todo:
    def task_list_display(self):
        for task_info in db.select_all_info():
            print(f"{task_info[0]}: {task_info[1]} {task_info[2]}")


if __name__ == "__main__":
    todo = Todo()
    todo.task_list_display()
