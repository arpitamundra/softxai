class Registration:
    def __init__(self, email, course_offering, employee_name, course_title):
        self.email = email
        self.course_offering_id = course_offering.course_offering_id
        self.registration_id = f"REG-COURSE-{employee_name}-{course_title}"