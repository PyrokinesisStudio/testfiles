import Category
import pickle

class Profiler:
	def __init__(self, filename):
		self.filename = filename
		self.profilefile = open(self.filename, "rb")
		self.data = pickle.load(self.profilefile)

	def __del__(self):
		self.profilefile.close()

	def __repr__(self):
		return self.filename

	def read(self, category):
		try:
			Category.Category(category, self.data).read()
		except Category.InvalidCategoryName:
			print("Invalid category %s" % category)

	def compare(self, category, other):
		try:
			c1 = Category.Category(category, self.data)
			c2 = Category.Category(category, other.data)
			c1.compare(c2)
		except Category.InvalidCategoryName:
			print("Invalid category %s" % category)
