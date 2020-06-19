import datetime

class DateTime(dict):

	def __init__(self):
		self.now = datetime.datetime.today()
		self.setdefault('date', {})
		self['date'].setdefault('weekday', None)
		self['date'].setdefault('month', None)
		self['date'].setdefault('day', None)
		self['date'].setdefault('year', None)
		self.compiledate()

	def compiledate(self):
		# Set weekday
		self.getdaystring(self.now.weekday())
		# Set month
		self.getmonthstring(self.now.month)
		self['date']['day'] = self.now.day
		self['date']['year'] = self.now.year

	def getmonthstring(self, int_month):
		month_name = [
			(1, "January"),
			(2, "February"),
			(3, "March"),
			(4, "April"),
			(5, "May"),
			(6, "June"),
			(7, "July"),
			(8, "August"),
			(9, "September"),
			(10, "October"),
			(11, "November"),
			(12, "December")
		]
		for num, month in month_name:
			if num == int_month:
				self['date']['month'] = month
				break
			elif num > 12:
				self['date']['month'] = "Invalid Month Value"
				break

	def getdaystring(self, int_weekday):
		weekday_name = [
			(0, "Monday"),
			(1, "Tuesday"),
			(2, "Wednesday"),
			(3, "Thursday"),
			(4, "Friday"),
			(5, "Saturday"),
			(6, "Sunday")
		]
		for num, day in weekday_name:
			if num == int_weekday:
				self['date']['weekday'] = day
				break
			elif num > 6:
				self['date']['weekday'] = "Invalid Day Value"
				break
