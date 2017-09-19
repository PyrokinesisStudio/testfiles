import Profile
import cmd
import sys

def getArgs(line):
	return line.split(" ")

class Commands(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.profiles = {}

	def onecmd(self, str):
		#try:
			cmd.Cmd.onecmd(self, str)
		#except ValueError:
			#print("Failed execute command %s" % str)

	def do_load(self, line):
		filename, register = getArgs(line)
		try:
			profile = Profile.Profiler(filename)
		except FileNotFoundError:
			print("Failed open file %s" % filename)
		else:
			print("Load profile file %s into register %s" % (filename, register))
			self.profiles[register] = profile

	def do_unload(self, line):
		register = getArgs(line)
		if register in self.profiles:
			print("Remove profile at register %s" % register)
			self.profiles.pop(register)
		else:
			print("Could not found register %s" % register)

	def do_read(self, line):
		category, register = getArgs(line)
		if register in self.profiles:
			profile = self.profiles[register]
			profile.read(category)

	def do_compare(self, line):
		category, r1, r2 = getArgs(line)
		if r1 in self.profiles and r2 in self.profiles:
			p1 = self.profiles[r1]
			p2 = self.profiles[r2]
			p1.compare(category, p2)

	def do_list(self, line):
		for r in self.profiles.keys():
			print("\t%s : \t%s" % (r, self.profiles[r]))

if __name__ == "__main__":
	try:
		c = Commands()

		for i in range(1, len(sys.argv), 2):
			c.do_load(sys.argv[i] + " " + sys.argv[i + 1])

		c.cmdloop()
	except KeyboardInterrupt:
		print("Quit")
