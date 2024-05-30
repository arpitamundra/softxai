from ..models.course_offering import CourseOffering
from ..models.registration import Registration

class CourseRegistrationService:
    def __init__(self):
        self.course_offerings = {}
        self.registrations = {}

    def add_course_offering(self, course_title, instructor, date, min_employees, max_employees):
        course_offering_id = f"OFFERING-{course_title}-{instructor}"
        if course_offering_id in self.course_offerings:
            print("INPUT_DATA_ERROR")
            return

        course_offering = CourseOffering(course_title, instructor, date, min_employees, max_employees)
        self.course_offerings[course_offering.course_offering_id] = course_offering
        print(course_offering.course_offering_id)

    def register(self, email, course_offering_id):
        course_offering = self.course_offerings.get(course_offering_id)
        if not course_offering:
            print("INPUT_DATA_ERROR")
            return

        employee_name = email.split("@")[0]
        if len(course_offering.registrations) >= course_offering.max_employees:
            print("COURSE_FULL_ERROR")
            return

        registration = Registration(email, course_offering, employee_name, course_offering.course_title)
        self.registrations[registration.registration_id] = registration
        course_offering.registrations.append(registration.registration_id)
        print(f"{registration.registration_id} ACCEPTED")

    def allot_course(self, course_offering_id):
        course_offering = self.course_offerings.get(course_offering_id)
        if not course_offering:
            print("INPUT_DATA_ERROR")
            return

        sorted_registrations = sorted(course_offering.registrations)
        if len(sorted_registrations) < course_offering.min_employees:
            print("COURSE_CANCELED")

        for registration_id in sorted_registrations:
            registration = self.registrations.get(registration_id)
            status = "CONFIRMED" if len(sorted_registrations) >= course_offering.min_employees else "CANCELED"
            print(f"{registration.registration_id} {registration.email} {registration.course_offering_id} {course_offering.course_title} {course_offering.instructor} {course_offering.date} {status}")

    def cancel(self, registration_id):
        registration = self.registrations.get(registration_id)
        if not registration:
            print("INPUT_DATA_ERROR")
            return

        course_offering = self.course_offerings.get(registration.course_offering_id)
        if registration.registration_id in course_offering.registrations:
            course_offering.registrations.remove(registration.registration_id)
            del self.registrations[registration.registration_id]
            print(f"{registration.registration_id} CANCEL_ACCEPTED")
        else:
            print(f"{registration.registration_id} CANCEL_REJECTED")