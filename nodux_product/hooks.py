# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nodux_product"
app_title = "Nodux Product"
app_publisher = "NODUX"
app_description = "Custom product"
app_icon = "octicon octicon-file-directory"
app_color = "dark green"
app_email = "tatianaq@nodux.ec"
app_license = "MIT"
fixtures = ["Item"]

doctype_js = {
        "Item": "product/item.js"
}
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nodux_product/css/nodux_product.css"
# app_include_js = "/assets/nodux_product/js/nodux_product.js"

# include js, css files in header of web template
# web_include_css = "/assets/nodux_product/css/nodux_product.css"
# web_include_js = "/assets/nodux_product/js/nodux_product.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nodux_product.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nodux_product.install.before_install"
# after_install = "nodux_product.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nodux_product.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Item": {
		"validate": "nodux_product.item_custom.calculate_cost_with_tax"
        #"validate": "nodux_product.item_custom.calculate_list_with_tax"
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nodux_product.tasks.all"
# 	],
# 	"daily": [
# 		"nodux_product.tasks.daily"
# 	],
# 	"hourly": [
# 		"nodux_product.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nodux_product.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nodux_product.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nodux_product.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nodux_product.event.get_events"
# }
