# import frappe
#
# import erpnext.education.utils as utils
#
# no_cache = 1
#
#
# def get_context(context):
# 	try:
# 		program = frappe.form_dict["program"]
# 		course_name = frappe.form_dict["name"]
# 	except KeyError:
# 		frappe.local.flags.redirect_location = "/lms"
# 		raise frappe.Redirect
#
# 	context.education_settings = frappe.get_single("Education Settings")
# 	course = frappe.get_doc("Course", course_name)
# 	context.program = program
# 	context.course = course
#
# 	context.topics = course.get_topics()
# 	context.has_access = utils.allowed_program_access(context.program)
# 	context.progress = get_topic_progress(context.topics, course, context.program)
#
#
# def get_topic_progress(topics, course, program):
# 	progress = {topic.name: utils.get_topic_progress(topic, course.name, program) for topic in topics}
# 	return progress



# --------------------------------- content.py -----------------------------------------


import frappe

# import erpnext.education.utils as utils
import vidhyapeeth.www.my_utils as utils

no_cache = 1


def get_context(context):
	try:
		program = frappe.form_dict["program"]
		course_name = frappe.form_dict["name"]
	except KeyError:
		frappe.local.flags.redirect_location = "/learning"
		raise frappe.Redirect

	context.education_settings = frappe.get_single("Education Settings")
	course = frappe.get_doc("Course", course_name)
	context.program = program
	context.course = course
	context.topics = course.get_topics()
	context.has_access = utils.allowed_program_access(context.program)
	context.progress = get_topic_progress(context.topics, course, context.program)

	# ---------------------------------------------

	data = frappe.db.sql(f"""
		SELECT log.parent, i.image FROM `tabInstructor Log` log
		INNER JOIN `tabInstructor` i
		ON log.parent = i.name
		WHERE course = '{course_name}'
		""")
	context.data = data

	# context.instructor = list(list(data[0]))[0]
	# context.instructor_img = list(list(data[0]))[1]

	# ------------------------------------------- #

	# context.education_settings = frappe.get_single("Education Settings")
	# context.instructor = frappe.get_doc("Instructor")

	# context.topics = course.get_topics()
	# context.has_access = utils.allowed_program_access(context.program)
	# context.progress = get_topic_progress(context.topics, course, context.program)


def get_topic_progress(topics, course, program):
	
	progress = {topic.name: utils.get_topic_progress(topic, course.name, program) for topic in topics}
	return progress
