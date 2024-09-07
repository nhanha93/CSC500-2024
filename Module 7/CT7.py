course_rooms = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}
def course_info(course_number):
    if course_number in course_rooms and course_number in course_instructors and course_number in course_times:
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        time = course_times[course_number]
        print(f"Course: {course_number}")
        print(f"Room: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {time}")
    else:
        print(f"Course {course_number} not found.")

user_input = input("Enter the course number: ")
course_info(user_input)
