# Function to parse the schedule, find free times for each student, and search by day and session
def find_free_schedule(input_text):
    lines = input_text.strip().split("\n")
    formatted_output = ""
    all_sessions = {"Senin": ["1", "2", "3", "4"],
                    "Selasa": ["1", "2", "3", "4"],
                    "Rabu": ["1", "2", "3", "4"],
                    "Kamis": ["1", "2", "3", "4"],
                    "Jumat": ["1", "2", "3", "4"]}
    
    student_free_schedule = {}  # To keep track of free schedule for each student
    
    for line in lines:
        data = line.strip().split("\t")
        nim = data[0]
        name = data[1]
        
        occupied_schedule = {day: [] for day in all_sessions.keys()}
        for i in range(3, len(data), 2):
            session_info = data[i].split(", ")
            day = session_info[0]
            session_time = session_info[1]
            occupied_schedule[day].append(session_time.split()[-1]) 
        
        free_schedule = {day: [s for s in all_sessions[day] if s not in occupied_schedule[day]] 
            for day in all_sessions.keys()}
        student_free_schedule[name] = free_schedule
        
        formatted_output += f"{name} - {nim}\n"
        for day, free_sessions in free_schedule.items():
            if free_sessions:
                formatted_output += f"{day} {', '.join(free_sessions)}\n"
        formatted_output += "\n" 

    return formatted_output.strip(), student_free_schedule, lines

def search_free_students(free_schedule_data, day, session, original_lines):
    free_students = []
    for student, schedule in free_schedule_data.items():
        if session in schedule.get(day, []):
            free_students.append(student)
    
    # Retrieve NIM for the free students
    free_students_with_nim = []
    for student in free_students:
        # Search for NIM based on student name
        matching_lines = [line for line in original_lines if line.startswith(student)]
        if matching_lines:
            data = matching_lines[0].strip().split("\t")
            nim = data[0]
            free_students_with_nim.append(f"{student} - {nim}")
        else:
            free_students_with_nim.append(f"{student}")

    return free_students_with_nim

# Reading input from a file
file_path = 'mahasiswa/data_if.txt'  # Ensure this file exists in the same directory
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Processing schedule and displaying formatted free schedule
formatted_output, free_schedule_data, lines = find_free_schedule(input_text)
print(formatted_output)

# Searching for students who are free on a specific day and session
day = input("Cari hari (e.g., Senin, Selasa): ")
session = input("Cari sesi kosong (e.g., 1, 2, 3, 4): ")

# Displaying the result
free_students = search_free_students(free_schedule_data, day, session, lines)
print(f"\nMahasiswa yang free hari {day} pas sesi {session}:")
print("\n".join(free_students) if free_students else "Pada sesi semua.")
