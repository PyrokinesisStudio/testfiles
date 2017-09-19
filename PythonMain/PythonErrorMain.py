import sys
import traceback
import BasicMain

class PythonErrorMain(BasicMain.BasicMain):
	def __init__(self, logFileName):
		BasicMain.BasicMain.__init__(self)
		self.log = open(logFileName, "w")
		self.log.write(("*" * 30) + " " + sys.argv[-2] + " " + ("*" * 30) + "\n")

	def exceptHook(self, exctype, value, tb):
		print("Detect error")
		self.log.write("=" * 100 + "\n")
		traceback.print_exception(exctype, value, tb, file=self.log)

	def init(self):
		sys.excepthook = self.exceptHook
		return BasicMain.BasicMain.init(self)

if __name__ == "__main__":
	BasicMain.launch(PythonErrorMain(sys.argv[-1]))
