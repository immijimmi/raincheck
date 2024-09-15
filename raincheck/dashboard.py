from tkcomponents import Component
from tkcomponents.extensions import GridHelper
from managedstate import State, NO_DEFAULT
from managedstate.extensions import Registrar, Listeners
from managedstate.extensions.registrar import PartialQueries


class Dashboard(Component.with_extensions(GridHelper)):
    def __init__(self, container):
        super().__init__(container)

        # State Initialisation
        self.state = State.with_extensions(Registrar, Listeners)()
        self.register_paths(self.state)

    def _render(self) -> None:
        pass  #####self.children["timeline"] = None

        #####workspace.render().grid(row=0, column=1, sticky="nswe")

    @staticmethod
    def register_paths(state: State.with_extensions(Registrar)) -> None:
        state.register_path("load_file", [], [])  # Used to add metadata for listeners

        state.register_path("locked_by", ["locked_by"], [None])

        state.register_path("task_groups", ["task_groups"], [{}])
        state.register_path("task_group", ["task_groups", PartialQueries.KEY], [{}])
        state.register_path(
            "task_group_name",
            ["task_groups", PartialQueries.KEY, "name"],
            [{}, NO_DEFAULT, ""]
        )
        state.register_path(
            "task_group_duration",
            ["task_groups", PartialQueries.KEY, "duration_s"],
            [{}, NO_DEFAULT, 0]
        )

        state.register_path("tasks", ["tasks"], [{}])
        state.register_path("task", ["tasks", PartialQueries.KEY], [{}])
        state.register_path("task_initial_deadline", ["tasks", PartialQueries.KEY, "initial_deadline"], [{}])
        state.register_path("task_current_deadline", ["tasks", PartialQueries.KEY, "current_deadline"], [{}])
        state.register_path("task_completions", ["tasks", PartialQueries.KEY, "completions"], [{}, NO_DEFAULT, []])
        state.register_path("task_dismissals", ["tasks", PartialQueries.KEY, "dismissals"], [{}, NO_DEFAULT, []])
        state.register_path("task_is_static", ["tasks", PartialQueries.KEY, "is_static"], [{}, NO_DEFAULT, True])
        state.register_path("task_deleted_at", ["tasks", PartialQueries.KEY, "deleted_at"], [{}, NO_DEFAULT, None])
