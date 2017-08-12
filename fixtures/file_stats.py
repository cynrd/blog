class FileStatsException(Exception):
	pass
		

class FileStats:
	def __init__(self, curr_file):
		if not curr_file:
			raise FileStatsException
		self.curr_file = curr_file
	
	def count_lines(self):
		with open(self.curr_file) as open_file:
			contents = open_file.readlines()
		return len(contents)
	
	def count_chars(self):
		with open(self.curr_file) as open_file:
			contents = open_file.read()
		return len(contents)
	