from PyQt4 import QtGui
from nfc_interface import NFCInterface
from nfc_thread import NFCThread
import sys

# a simple gui shows the card id

class MonitorWindow(QtGui.QWidget):
	
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		
		self.idLabel = QtGui.QLabel('Card ID:')
		self.idText = QtGui.QLineEdit()
		self.idText.setReadOnly(True)

		self.idHbox = QtGui.QHBoxLayout()
		self.idHbox.addWidget(self.idLabel)
		self.idHbox.addWidget(self.idText)

		self.setLayout(self.idHbox)
		self.nfc = NFCInterface()
		self.nfcThread = NFCThread(self.nfc)
		self.nfcThread.gotID[str].connect(self.gotNewID)

		self.connectNFC()
		self.nfcThread.start()

	def connectNFC(self):
		port, ok = QtGui.QInputDialog.getText(self, 'Port', 'Enter port of arduino board:')
		if not ok:
			sys.exit(0)
		else:
			self.nfc.port = str(port) #.upper()
		
		self.nfc.connectToArduino()

		if not self.nfc.isConnected() or not port:
			QtGui.QMessageBox.critical(self, 'Error', 'Please connect arduino and enter the correct port')
			sys.exit(1)
	

	def gotNewID(self, new_id):
		self.idText.setText(new_id)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	win = MonitorWindow()
	win.show()
	sys.exit(app.exec_())