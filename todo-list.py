"""
Day 19 - 2026-10-25
Tool: Simple To-Do List
What it does: Keeps a small list of tasks, marks them done, counts
what is left, and shows pending tasks first - the basic logic behind
every to-do app.
Who it helps: Students planning study tasks, office workers tracking
daily work, or anyone organising household jobs for the day.
"""


def add_task(tasks, title, priority="normal"):
    """Add one task (a dict) to the list and return the list."""
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")
    tasks.append({"title": title.strip(), "priority": priority,
                  "done": False})
    return tasks


def mark_done(tasks, title):
    """Mark the first task with this title as done. Returns True if found."""
    for task in tasks:
        if task["title"] == title and not task["done"]:
            task["done"] = True
            return True
    return False


def pending_tasks(tasks):
    return [t for t in tasks if not t["done"]]


def counts(tasks):
    done = sum(1 for t in tasks if t["done"])
    return {"total": len(tasks), "done": done,
            "pending": len(tasks) - done}


if __name__ == "__main__":
    my_tasks = []
    add_task(my_tasks, "Buy groceries", "high")
    add_task(my_tasks, "Finish assignment", "high")
    add_task(my_tasks, "Call the bank")
    add_task(my_tasks, "Evening walk")

    mark_done(my_tasks, "Buy groceries")

    print("Counts:", counts(my_tasks))
    print("Still to do:")
    for task in pending_tasks(my_tasks):
        print(" -", task["title"], f"({task['priority']})")
