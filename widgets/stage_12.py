from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlLabel import ControlLabel

from generation import Stage12

class Stage12Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage12Window, self).__init__()
        self.set_margin(20)

        self.erd = erd
        self.project = project

        self._label = ControlLabel('Etap 12')
        self._save_button = ControlButton('Zapisz etap 12')

        self._save_button.value = self.__save_action

    def __save_action(self):
        self.project.stages.append(Stage12(self.erd))