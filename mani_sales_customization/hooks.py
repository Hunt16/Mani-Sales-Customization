from . import __version__ as app_version

app_name = "mani_sales_customization"
app_title = "Mani Sales Customization"
app_publisher = "Akhilaminc"
app_description = "Mani Sales Customization"
app_email = "vivekthakor1690@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mani_sales_customization/css/mani_sales_customization.css"
# app_include_js = "/assets/mani_sales_customization/js/mani_sales_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/mani_sales_customization/css/mani_sales_customization.css"
# web_include_js = "/assets/mani_sales_customization/js/mani_sales_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mani_sales_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "mani_sales_customization.utils.jinja_methods",
#	"filters": "mani_sales_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mani_sales_customization.install.before_install"
# after_install = "mani_sales_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mani_sales_customization.uninstall.before_uninstall"
# after_uninstall = "mani_sales_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mani_sales_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"mani_sales_customization.tasks.all"
#	],
#	"daily": [
#		"mani_sales_customization.tasks.daily"
#	],
#	"hourly": [
#		"mani_sales_customization.tasks.hourly"
#	],
#	"weekly": [
#		"mani_sales_customization.tasks.weekly"
#	],
#	"monthly": [
#		"mani_sales_customization.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "mani_sales_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "mani_sales_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "mani_sales_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"mani_sales_customization.auth.validate"
# ]
