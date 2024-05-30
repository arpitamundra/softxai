# import sys
#
# # Constants
# COURSE_FULL_ERROR = "COURSE_FULL_ERROR"
# CANCEL_ACCEPTED = "CANCEL_ACCEPTED"
# CANCEL_REJECTED = "CANCEL_REJECTED"
# INPUT_DATA_ERROR = "INPUT_DATA_ERROR"
# COURSE_CANCELED = "COURSE_CANCELED"
# ACCEPTED = "ACCEPTED"
#
#
# class Course:
#     def __init__(self, name, instructor, date, min_employees, max_employees):
#         self.course_name = name
#         self.instructor = instructor
#         self.date = int(date)  # Convert date to integer
#         self.min_employees = int(min_employees)
#         self.max_employees = int(max_employees)
#         self.course_offering_id = f"OFFERING-{name}-{instructor}"
#         self.registrations = []
#
#     def add_registration(self, email):
#         if self.is_full():
#             return COURSE_FULL_ERROR
#         else:
#             self.registrations.append(email)
#             return f"REG-COURSE-{email.split('@')[0]}-{self.course_name}", ACCEPTED
#
#     def cancel_registration(self, registration_id):
#         if not self.is_cancelable():
#             return CANCEL_REJECTED
#         else:
#             if registration_id in self.registrations:
#                 self.registrations.remove(registration_id)
#                 return CANCEL_ACCEPTED
#             else:
#                 return CANCEL_REJECTED
#
#     def is_cancelable(self):
#         return not self.date
#
#     def is_full(self):
#         return len(self.registrations) >= self.max_employees
#
#     def is_canceled(self):
#         return len(self.registrations) < self.min_employees
#
#
# class CourseOffering:
#     def __init__(self, course):
#         self.course = course
#
#     def allot_course(self):
#         status = COURSE_CANCELED if self.course.is_canceled() else ACCEPTED
#         for reg in self.course.registrations:
#             yield (reg, f"OFFERING-{self.course.course_name}-{self.course.instructor}",
#                    self.course.course_name, self.course.instructor, self.course.date, status)
#
#
# class CourseManager:
#     def __init__(self):
#         self.courses = {}
#
#     def add_course(self, name, instructor, date, min_employees, max_employees):
#         course = Course(name, instructor, date, min_employees, max_employees)
#         self.courses[course.course_offering_id] = course
#         return course.course_offering_id
#         # self.courses[course.name] = course
#         # return course
#
#     def register_for_course(self, email, course_name):
#         if course_name not in self.courses:
#             return INPUT_DATA_ERROR
#         else:
#             return self.courses[course_name].add_registration(email)
#
#     def cancel_registration(self, registration_id):
#         for course in self.courses.values():
#             result = course.cancel_registration(registration_id)
#             if result == CANCEL_ACCEPTED:
#                 return result
#         return CANCEL_REJECTED
#
#     def allot_courses(self):
#         for course in self.courses.values():
#             offering = CourseOffering(course)
#             yield from offering.allot_course()
#
#
# def parse_command(command):
#     return command.split()
#
#
# def main(input_file):
#     course_manager = CourseManager()
#     with open(input_file, 'r') as f:
#         for line in f:
#             command, *params = parse_command(line.strip())
#             if command == "ADD-COURSE-OFFERING":
#                 print(course_manager.add_course(*params))
#                 # print(course_management.add_course_offering(*params))
#
#             elif command == "REGISTER":
#                 print(course_manager.register_for_course(*params))
#             elif command == "CANCEL":
#                 print(course_manager.cancel_registration(*params))
#             elif command == "ALLOT-COURSE":
#                 for details in course_manager.allot_courses():
#                     print(*details)
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python script.py input_file.txt")
#         sys.exit(1)
#     input_file = sys.argv[1]
#     main(input_file)
# # main("/Users/arpitamundra/PycharmProjects/python practice /input.txt")



import sys

# Constants
COURSE_FULL_ERROR = "COURSE_FULL_ERROR"
CANCEL_ACCEPTED = "CANCEL_ACCEPTED"
CANCEL_REJECTED = "CANCEL_REJECTED"
INPUT_DATA_ERROR = "INPUT_DATA_ERROR"
COURSE_CANCELED = "COURSE_CANCELED"
ACCEPTED = "ACCEPTED"


class Course:
    def __init__(self, name, instructor, date, min_employees, max_employees):
        self.name = name
        self.instructor = instructor
        self.date = int(date)
        self.min_employees = int(min_employees)
        self.max_employees = int(max_employees)
        self.registrations = []
        self.course_offering_id = f"OFFERING-{name}-{instructor}"

    def add_registration(self, email):
        if self.is_full():
            return COURSE_FULL_ERROR
        else:
            registration_id = f"REG-COURSE-{email.split('@')[0]}-{self.name}"
            self.registrations.append(registration_id)
            return registration_id, ACCEPTED

    def cancel_registration(self, registration_id):
        if self.is_cancelable():
            if registration_id in self.registrations:
                self.registrations.remove(registration_id)
                return CANCEL_ACCEPTED
            else:
                return CANCEL_REJECTED
        else:
            return CANCEL_REJECTED

    def is_cancelable(self):
        return not self.date

    def is_full(self):
        return len(self.registrations) >= self.max_employees

    def is_canceled(self):
        return len(self.registrations) < self.min_employees


class CourseOffering:
    def __init__(self, course):
        self.course = course

    def allot_course(self):
        status = COURSE_CANCELED if self.course.is_canceled() else ACCEPTED
        for reg in self.course.registrations:
            yield (reg, f"OFFERING-{self.course.name}-{self.course.instructor}",
                   self.course.name, self.course.instructor, self.course.date, status)


class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, name, instructor, date, min_employees, max_employees):
        course = Course(name, instructor, date, min_employees, max_employees)
        # self.courses[course.course_offering_id = f"OFFERING-{name}-{instructor}"] = course
        self.courses[course.course_offering_id] = course
    def register_for_course(self, email, course_name):
        if course_name in self.courses:
            return self.courses[course_name].add_registration(email)
        else:
            return INPUT_DATA_ERROR

    def cancel_registration(self, registration_id):
        for course in self.courses.values():
            result = course.cancel_registration(registration_id)
            if result == CANCEL_ACCEPTED:
                return result
        return CANCEL_REJECTED

    def allot_courses(self):
        for course in self.courses.values():
            offering = CourseOffering(course)
            yield from offering.allot_course()


def parse_command(command):
    return command.split()


def main(input_file):
    course_manager = CourseManager()
    with open(input_file, 'r') as f:
        for line in f:
            command, *params = parse_command(line.strip())
            if command == "ADD-COURSE-OFFERING":
                course_manager.add_course(*params)
            elif command == "REGISTER":
                print(course_manager.register_for_course(*params))
            elif command == "CANCEL":
                print(course_manager.cancel_registration(*params))
            elif command == "ALLOT-COURSE":
                for details in course_manager.allot_courses():
                    print(*details)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file.txt")
        sys.exit(1)
    input_file = sys.argv[1]
    main(input_file)
