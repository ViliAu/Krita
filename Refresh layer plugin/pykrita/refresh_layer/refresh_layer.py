# BBD's Krita Script Starter Feb 2018

from krita import Extension
from krita import FileLayer
from krita import QMessageBox
from krita import QWidget

EXTENSION_ID = "pykrita_refresh_layer"
MENU_ENTRY = "Refresh layer"

def errorMessage():
        QMessageBox.information(QWidget(), "Refresh layer error", "No active file layer selected. Select a file layer\nfrom the layer selection.")

class RefreshLayer(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(EXTENSION_ID, MENU_ENTRY, "tools/scripts")
        action.triggered.connect(self.action_triggered)

    def action_triggered(self):
        try:
            if isinstance(Krita.instance().activeDocument().activeNode(), FileLayer): 
                Krita.instance().activeDocument().activeNode().resetCache()
            else:
                errorMessage()
        except:
            errorMessage()
