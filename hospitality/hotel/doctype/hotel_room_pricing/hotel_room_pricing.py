# Copyright (c) 2023, ZeltenLabs and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import format_date
from datetime import datetime


class HotelRoomPricing(Document):
	def before_save(self):
		# if title is not set, set it to self.from_date - self.to_date
		if not self.title:
			self.title = datetime.strptime(self.from_date, '%Y-%m-%d').strftime('%b %d, %Y') + "-" + datetime.strptime(self.to_date, '%Y-%m-%d').strftime('%b %d, %Y')
