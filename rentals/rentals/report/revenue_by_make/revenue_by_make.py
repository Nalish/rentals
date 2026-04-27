# Copyright (c) 2026, Nalish and contributors
# For license information, please see license.txt

import frappe
from frappe import _





def execute(filters: dict | None = None):
    columns = [
        {"fieldname": "make", "label": "Make", "fieldtype": "Data"},
        {"fieldname": "total_revenue", "label": "TOTAL Revenue", "fieldtype": "Currency"}
    ]

    data = frappe.db.sql("""
        SELECT 
            v.make AS make,
            SUM(rb.total_amount) AS total_revenue
        FROM `tabRide Booking` rb
        JOIN `tabVehicle` v ON rb.vehicle = v.name
        WHERE rb.docstatus = 1
        GROUP BY v.make
    """, as_dict=True)


	

    return columns, data,"Here is the Report"


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Column 1"),
			"fieldname": "column_1",
			"fieldtype": "Data",
		},
		{
			"label": _("Column 2"),
			"fieldname": "column_2",
			"fieldtype": "Int",
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return [
		["Row 1", 1],
		["Row 2", 2],
	]
