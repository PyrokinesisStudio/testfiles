import pickle
import time
import sys
import bge
import BasicMain

class ProfileMain(BasicMain.BasicMain):
	def __init__(self, logFileName, frame):
		BasicMain.BasicMain.__init__(self, frame)
		self.profile = []
		self.log = open(logFileName, "wb")

	def __del__(self):
		pickle.dump(self.profile, self.log)
		self.log.close()

	def init(self):
		return BasicMain.BasicMain.init(self)

	def endFrame(self, i):
		info = bge.logic.getProfileInfo()
		self.profile.append((bge.logic.getRealTime(), dict(info)))


if __name__ == "__main__":
	frame = int(sys.argv[-2])
	filename = sys.argv[-1]
	BasicMain.launch(ProfileMain(filename, frame))
