from tkinter import Tk


from .components import Dashboard


class App:
    def __init__(self):
        self._window = Tk()
        self._window.resizable(False, False)
        self._window.minsize(width=200, height=0)  # Min width so that the window remains grabbable using the cursor
        self._window.title(Constants.WINDOW_TITLE)

        # Make the window expand to fit displayed content
        self._window.columnconfigure(0, weight=1)
        self._window.rowconfigure(0, weight=1)

        s = Dashboard(self._window)
        s.render().grid(sticky="nswe")

        self._window.mainloop()
