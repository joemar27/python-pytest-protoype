from project_datetime import invoicedatetime

class CalculateTotal(invoicedatetime.DateTime):

	def __init__(self):
		super(CalculateTotal, self).__init__()

	def gettotal(self, item_list):
		total = 0
		item_tally = ""
		for item, price in item_list:
			total = total + price
			ellipses = '.' * (50 - len(item))
			item_tally += "{}{}{}\n".format(item, ellipses, price)
		return (total, item_tally)

	def calctax(self, total, tax_on_items):
		return round((total + tax_on_items), 2)
