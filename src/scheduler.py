from .task import Task

class Scheduler:
    def __init__(self, core_num: int):
        self._core_num = core_num
        pass

    def schedule(self, tasks: list[Task]) -> list[Task]:
        unscheduled_tasks: list[Task] = tasks
        wait_tasks: list[Task] = []
        scheduling_task_dict: dict[int, Task] = {c: None for c in range(self.core_num)} # core-task map: {0: Task, 1: None, 2: Task}
        scheduled_tasks: list[Task] = []
        time = 0

        # [v for v in scheduling_task_dict.values() if v is not None] -> [None, None, None] -> no task scheduling
        while(len(unscheduled_tasks) != 0 or len(wait_tasks) != 0 or len([v for v in scheduling_task_dict.values() if v is not None]) != 0):
            # if release, enque wait queue and remove unscheduled list
            for task in unscheduled_tasks:
                if time >= task.release_time:
                    wait_tasks.append(task)
                    unscheduled_tasks.remove(task)

            # sort for priority, defalut -> release_time
            wait_tasks.sort(key=lambda x: x.release_time)

            # if finish, push scheduled list and core-task map mark None
            for core, task in scheduling_task_dict.items():
                if task is not None and time >= task.finish_time:
                    scheduled_tasks.append(task)
                    scheduling_task_dict[core] = None

            # if any core empty, deque wait queue and map core-task map
            # this time, start time <- time, finish time <- time+wcet, core <- core
            for core in scheduling_task_dict.keys():
                if scheduling_task_dict[core] is None and len(wait_tasks) > 0:
                    new_scheduling_task = wait_tasks.pop(0)
                    new_scheduling_task.start_time = time
                    new_scheduling_task.finish_time = time + new_scheduling_task.wcet
                    new_scheduling_task.core = core
                    scheduling_task_dict[core] = new_scheduling_task

            # step forward
            time += 1

        return scheduled_tasks
    
    def display(self, tasks: list[Task]):
        sched_dict: dict[int, list[Task]] = {}

        for task in tasks:
            if task.core in sched_dict.keys():
                sched_dict[task.core].append(task)
            else:
                sched_dict[task.core] = [task]

        for c, ts in sorted(sched_dict.items(), key=lambda x: x[0]):
            ts_str = [f'{t.idx}: [{t.start_time}-{t.finish_time}]' for t in ts]
            print(f'{c}: {ts_str}')

    @property
    def core_num(self) -> int:
        return self._core_num