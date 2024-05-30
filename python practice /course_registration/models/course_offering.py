class CourseOffering:
    def __init__(self, course_title, instructor, date, min_employees, max_employees):
        self.course_title = course_title
        self.instructor = instructor
        self.date = date
        self.min_employees = min_employees
        self.max_employees = max_employees
        self.course_offering_id = f"OFFERING-{course_title}-{instructor}"
        self.registrations = []