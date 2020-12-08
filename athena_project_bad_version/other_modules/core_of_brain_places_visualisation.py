from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np

application = QApplication([])
w = gl.GLViewWidget()
w.opts["distance"] = 40
w.show()
gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-10, 0, 0)
w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -10, 0)
w.addItem(gy)
gz = gl.GLGridItem()
gz.translate(0, 0, -10)
w.addItem(gz)
if __name__ == "__main__":
    import sys
    if(sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QGuiApplication.instance().exec_()