class Task:
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = deadline
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_task_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def get_task_by_priority(self, priority):
        priority_tasks = []
        for task in self.tasks:
            if task.priority == priority:
                priority_tasks.append(task)
        return priority_tasks

    def get_upcoming_tasks(self, days):
        upcoming_tasks = []
        for task in self.tasks:
            days_until_deadline = (task.deadline - datetime.datetime.now().date()).days
            if days_until_deadline <= days:
                upcoming_tasks.append(task)
        return upcoming_tasks

    #Le code définit deux classes : Task et TaskManager.
    #La classe Task représente une tâche avec un nom, une date limite et une priorité. La classe TaskManager gère une liste de tâches et permet d'ajouter, supprimer et rechercher des tâches en fonction de différents critères tels que le nom, la priorité et les tâches à venir dans un certain nombre de jours. Vous
    #pouvez utiliser cette base pour construire votre propre application de gestion de tâches en ajoutant des fonctionnalités supplémentaires et une interface utilisateur.
