# Copyright (c) 2023, ZeltenLabs and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, add_days
from dateutil.rrule import rrule, DAILY
import datetime


class HotelRoom(Document):
	pass

@frappe.whitelist()
def get_occupancy_data(room_name):
    # Fetch all reservations.
    reservations = frappe.get_all('Hotel Room Reservation', fields=['name', 'from_date', 'to_date'])

    # Filter out reservations that do not include the room.
    reservations_for_room = []
    for reservation in reservations:
        rooms = frappe.get_all('Hotel Room Reservation Detail', filters={'parent': reservation.name, 'hote_room': room_name}, fields=['hote_room'])
        if rooms:
            reservations_for_room.append(reservation)

    # Sort the reservations by from_date.
    reservations_for_room.sort(key=lambda r: r.from_date)

    # Initialize the data points dictionary.
    data_points = {}

    # Iterate over the reservations and count the number of reservations for each date.
    for reservation in reservations_for_room:
        start_date = getdate(reservation['from_date'])
        end_date = getdate(reservation['to_date'])

        for dt in rrule(DAILY, dtstart=start_date, until=end_date):
            timestamp = int(dt.timestamp())
            if timestamp in data_points:
                data_points[timestamp] += 1
            else:
                data_points[timestamp] = 1

    return data_points