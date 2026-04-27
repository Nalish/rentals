# Copyright (c) 2026, Nalish and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		color: DF.Data | None
		condition: DF.Rating
		insurance_expiry: DF.Date
		is_published: DF.Check
		licenseplate: DF.Data | None
		make: DF.Data
		model: DF.Data
		name: DF.Int | None
		route: DF.Data | None
		status: DF.Literal["Active", "Out of service", "Sold", "Crushed"]
		title: DF.Data | None
		vehicle_image: DF.AttachImage | None
		year: DF.Int
	# end: auto-generated types

	pass
