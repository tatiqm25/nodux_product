# -*- coding: utf-8 -*-
# Copyright (c) 2015, NODUX and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe import _

class Item(Document):
	def search_taxes(self):
        if self.item_group
            tax = frappe.db.sql("""select tax from `tabItemGroup`
    			where item_group_name = %s)""",
    			(self.item_group)
    		if not item:
    			frappe.throw(_("Group {0} is not tax").format(self.item_group))
            print "Taxes ", tax
    		self.taxes = tax[0]
