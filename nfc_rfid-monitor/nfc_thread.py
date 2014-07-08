from PyQt4 import QtCore

# a thread with a single signal

class NFCThread(QtCore.QThread):

	# emitted when we got an ID
	gotID = QtCore.pyqtSignal(str)

	def __init__(self, nfc_iface, parent=None):
		QtCore.QThread.__init__(self, parent)
		self.nfc = nfc_iface


	def run(self):
		while True:
			currentID = self.nfc.getCurrentID()
			if currentID:
				self.gotID.emit(currentID)

			QtCore.QThread.msleep(150)

		self.exec_()


if __name__ == '__main__':
	import sys
	app = QtCore.QCoreApplication(sys.argv)

	def gotNewID(new_id):
		print 'got an id: %s' % new_id

	nfc_thread = NFCThread(None)
	nfc_thread.gotID[str].connect(gotNewID)
	nfc_thread.start()

	sys.exit(app.exec_())