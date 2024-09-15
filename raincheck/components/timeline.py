from .dashboard_component import DashboardComponent


class Timeline(DashboardComponent):
    def _render(self) -> None:
        tasks = self.state.registered_get("tasks")
        task_groups = self.state.registered_get("tasks")

        ordered_task_groups = [
            (task_group_id, task_group_data) for task_group_id, task_group_data in task_groups
        ]
        ordered_task_groups.sort(
            key=lambda group_details: (
                group_details[1]["duration_s"],
                group_details[0]
            )
        )

        ordered_tasks = [
            (task_id, task_data) for task_id, task_data in tasks
        ]
        ordered_task_groups.sort(
            key=lambda task_details: (
                task_details[1]["initial_deadline"],
                task_details[0]
            )
        )
        ##### Filter out completed non-repeating tasks and deleted tasks
