class PrintoutFormat(object):

	def __init__(self):
		pass

	def spacecount(self, space_type, count, text):
		spacebetween = space_type * (count - len(text))
		return spacebetween
