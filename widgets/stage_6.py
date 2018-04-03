from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from generation import Stage6
from base import Transaction


class Stage6Window(BaseWidget):

    def __init__(self, erd, transactions):
        super(Stage6Window, self).__init__()
        self.set_margin(20)

        self._label = ControlLabel('Nie masz tutaj nic do roboty, kliknij zapisz')
        self._save_button('Zapisz')

        self.erd = erd
        self.transactions = transactions

        self._populate()