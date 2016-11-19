import datetime

from core.models.tasks import Task


class TaskManager:

    def __init__(self, engine):
        self._engine = engine

    def add_task(self, task: Task):
        session = self._engine.persistence.session()
        session.add(task)
        session.commit()
        print('[TASK-DB]: add ', task)

    def create_task(self, subject, **kwargs):
        task = Task(subject=subject, **kwargs)

        session = self._engine.persistence.session()
        session.add(task)
        session.commit()
        print('[TASK-DB]: created ', task)

    def get_task_by_subject(self, subject):
        session = self._engine.persistence.session()
        task = session.query(Task).filter_by(subject=subject).first()
        return task

    def get_tasks(self):
        session = self._engine.persistence.session()
        tasks = session.query(Task).all()
        return tasks

    def do_task_by_subject(self, subject):
        session = self._engine.persistence.session()
        task = self.get_task_by_subject(subject)
        task.exec_date = datetime.datetime.utcnow()
        session.commit()

    def get_done_tasks(self):
        session = self._engine.persistence.session()
        tasks = session.query(Task).filter(Task.exec_date.isnot(None)).all()
        return tasks

    def get_undone_tasks(self):
        session = self._engine.persistence.session()
        tasks = session.query(Task).filter(Task.exec_date is None).all()
        return tasks
