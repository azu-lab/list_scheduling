from task import Task

class Scheduler:
    def __init__(self):
        pass

    def schedule(self, tasks: list[Task]) -> list[Task]:
        return tasks
    
    def display(self, tasks: list[Task]):
        sched_dict: dict[int, list[Task]] = {}

        for task in tasks:
            if task.core in sched_dict.keys():
                sched_dict[task.core].append(task)
            else:
                sched_dict[task.core] = [task]

        for c, ts in sched_dict.items():
            ts_str = [f'[{t.start_time}-{t.finish_time}]' for t in ts]
            print(f'{c}: {ts_str}')