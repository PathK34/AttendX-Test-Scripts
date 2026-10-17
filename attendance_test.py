def mark_attendance(student_id, status):
    if not student_id:
        return "Student ID is required"

    if status not in ["Present", "Absent"]:
        return "Invalid attendance status"

    return f"Attendance marked: {status}"


print(mark_attendance("ST101", "Present"))
print(mark_attendance("", "Present"))
print(mark_attendance("ST102", "Unknown"))