from tkinter import Toplevel, Button
from tkinter.messagebox import askquestion

from structural.facade import Render


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Rendering")
        self.geometry("200x700")

        self.button = Button(self, text="Start rendering",
                             command=self.start_rendering())
        self.button.pack(expand=True)

    def start_rendering(self):
        renderTrack = Render()
        askquestion('...', message='Start Rendering?')
        renderTrack.startRendering()
