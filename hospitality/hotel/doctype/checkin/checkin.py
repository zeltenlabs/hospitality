# Copyright (c) 2023, ZeltenLabs and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



class Checkin(Document):
	def after_insert(self):
		# Check if the linked field is set in the current document
		if self.reservation:
			reservation = frappe.get_doc("Hotel Room Reservation", self.reservation)
			reservation.status = "Checked-In"
			reservation.save()
