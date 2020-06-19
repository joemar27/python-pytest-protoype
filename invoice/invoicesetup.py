from printformat import printoutformat
from calculate import calculateinvoiceitems

class Invoice(printoutformat.PrintoutFormat):

	def __init__(self):
		super(Invoice, self).__init__()

	def createinvoice(self, items):
		receipt = calculateinvoiceitems.CalculateTotal()
		total, item_list = receipt.gettotal(items)
		tax_on_items = total * .0975
		sub_total = "Sub Total:{ellipses}${total_amt}\n".format(
			ellipses = self.spacecount(' ', 49, "Sub Total:"),
			total_amt = total
			)
		sales_tax = "Sales Tax:{ellipses}{tax_percent}\n".format(
			ellipses = self.spacecount(' ', 50, "Sales Tax:"),
			tax_percent = "9.75%"
			)
		tax_total = "Tax Total:{ellipses}${tax_total}\n".format(
			ellipses = self.spacecount(' ', 49, "Tax Total:"),
			tax_total = tax_on_items
			)
		total = "Total:{ellipses}${total_w_tax}".format(
			ellipses = self.spacecount(' ', 49, "Total:"),
			total_w_tax = receipt.calctax(total, tax_on_items)
			)
		date_str = "{weekday} {month} {day}, {year}\n\n".format(
			weekday = receipt['date']['weekday'],
			month = receipt['date']['month'],
			day = receipt['date']['day'],
			year = receipt['date']['year']
			)
		date_str += "{item_str}\n".format(item_str = item_list)
		date_str += sub_total
		date_str += sales_tax
		date_str += tax_total
		date_str += total
		return date_str
