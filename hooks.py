from . import __version__ as app_version

app_name = "theme_manager"
app_title = "Theme Manager"
app_publisher = "efeone"
app_description = "Theme Manger is an frappe app build for customising theme with ERPNext Support"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sherin@efeone.com"
app_license = "MIT"
app_logo_url = "/assets/theme_manager/images/sg-logo.png"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = [
	"/assets/theme_manager/scss/login.scss"
]
# app_include_js = "/assets/theme_manager/js/theme_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/theme_manager/css/theme_manager.css"
# web_include_js = "/assets/theme_manager/js/theme_manager.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "theme_manager/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Issue": "public/js/issue.js",
	"Item": "public/js/item.js",
	"Purchase Order": "public/js/purchase_order.js",
	"Sales Invoice": "public/js/sales_invoice.js",
	"Sales Order": "public/js/sales_order.js"
}

base_template = "templates/base.html"

website_context = {
	"favicon": 	"/assets/theme_manager/images/sg-favicon.png",
	"splash_image": "/assets/theme_manager/images/sg-favicon.png"
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "theme_manager.install.before_install"
# after_install = "theme_manager.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "theme_manager.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"theme_manager.tasks.all"
# 	],
# 	"daily": [
# 		"theme_manager.tasks.daily"
# 	],
# 	"hourly": [
# 		"theme_manager.tasks.hourly"
# 	],
# 	"weekly": [
# 		"theme_manager.tasks.weekly"
# 	]
# 	"monthly": [
# 		"theme_manager.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "theme_manager.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "theme_manager.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "theme_manager.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"theme_manager.auth.validate"
# ]
