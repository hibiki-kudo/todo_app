DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks(
    id INTEGER PRIMARY KEY,
    done TEXT,
    task_name TEXT
);

INSERT INTO tasks
    (id,done,task_name)
VALUES
    (1,'[Done]','task1'),
    (2,'[Undone]','task2'),
    (3,'[Undone]','task3')
;