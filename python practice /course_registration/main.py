import sys
from services.course_registration_service import CourseRegistrationService

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    course_registration_service = CourseRegistrationService()

    try:
        with open(input_file, "r") as file:
            for line in file:
                command, *args = line.strip().split()
                if command == "ADD-COURSE-OFFERING":
                    course_title, instructor, date, min_employees, max_employees = args
                    course_registration_service.add_course_offering(course_title, instructor, date, int(min_employees), int(max_employees))
                elif command == "REGISTER":
                    email, course_offering_id = args
                    course_registration_service.register(email, course_offering_id)
                elif command == "ALLOT-COURSE":
                    course_offering_id = args[0]
                    course_registration_service.allot_course(course_offering_id)
                elif command == "CANCEL":
                    registration_id = args[0]
                    course_registration_service.cancel(registration_id)
                else:
                    print("INPUT_DATA_ERROR")
    except FileNotFoundError:
        print(f"File not found: {input_file}")

if __name__ == "__main__":
    main()