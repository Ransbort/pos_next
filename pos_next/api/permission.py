import frappe


def has_app_permission():
	"""Gate for the POS Next icon on the Frappe Apps screen (see
	add_to_apps_screen in hooks.py). This file was missing from this
	branch entirely - without it, frappe.boot.get_app_data() fails to
	import this path on every single desk boot, which breaks desk
	access for every user on the site, not just POS staff. Defaults to
	permissive (matches what Frappe itself does when an app omits
	has_permission from its add_to_apps_screen entry at all): anyone who
	can log into the desk sees the icon. Tighten this to an explicit
	role check if you want it hidden from non-POS staff specifically.
	"""
	return True
