from invoice import invoicesetup


def getreceipt(items):
	invoice = invoicesetup.Invoice()
	receipt = invoice.createinvoice(items)
	print(receipt)


if __name__ == '__main__':
	listofitems = [
		("bread", 1.22),
		("milk", .98),
		("cheese", 1.05),
		("coffee", 1.08)
	]
	getreceipt(listofitems)
