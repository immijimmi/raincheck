from tkcomponents import Component
from tkcomponents.extensions import GridHelper


class DashboardComponent(Component.with_extensions(GridHelper)):
    def __init__(self, dashboard, container):
        self._dashboard = dashboard

        super().__init__(container)

    @property
    def state(self):
        return self._dashboard.state
