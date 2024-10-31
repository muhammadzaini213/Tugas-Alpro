def find_free_schedule(input_text):
    lines = input_text.strip().split("\n")
    formatted_output = ""
    all_sessions = {"Senin": ["1", "2", "3", "4"],
                    "Selasa": ["1", "2", "3", "4"],
                    "Rabu": ["1", "2", "3", "4"],
                    "Kamis": ["1", "2", "3", "4"],
                    "Jumat": ["1", "2", "3", "4"]}
    
    student_free_schedule = {}  # Menyimpan jadwal kosong setiap mahasiswa
    
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
    
    # Mengambil NIM untuk mahasiswa yang kosong
    free_students_with_nim = []
    for student in free_students:
        matching_lines = [line for line in original_lines if line.startswith(student)]
        if matching_lines:
            data = matching_lines[0].strip().split("\t")
            nim = data[0]
            free_students_with_nim.append(f"{student} - {nim}")
        else:
            free_students_with_nim.append(f"{student}")

    return free_students_with_nim

def count_free_students_per_day_and_session(free_schedule_data):
    all_sessions = ["1", "2", "3", "4"]
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    
    free_count = {day: {session: 0 for session in all_sessions} for day in days}
    
    # Hitung jumlah mahasiswa yang bebas pada setiap sesi di setiap hari
    for day in days:
        for session in all_sessions:
            free_count[day][session] = sum(1 for schedule in free_schedule_data.values() if session in schedule.get(day, []))
    
    return free_count

# Membaca file input
file_path = 'data_if.txt'  # Pastikan file ini ada di direktori yang sama
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Memproses jadwal dan menampilkan jadwal kosong yang diformat
formatted_output, free_schedule_data, lines = find_free_schedule(input_text)
print("Jadwal Kosong Setiap Mahasiswa:")
print(formatted_output)

# Menghitung jumlah mahasiswa yang kosong pada setiap hari dan sesi
free_count = count_free_students_per_day_and_session(free_schedule_data)

# Menampilkan jumlah mahasiswa kosong untuk setiap hari dan sesi dengan pemisahan hari
print("\nJumlah mahasiswa yang kosong pada setiap hari dan sesi:")
for day, sessions in free_count.items():
    print(f"Hari {day}:")
    for session, count in sessions.items():
        print(f"Sesi {session}: {count} mahasiswa kosong.")
    print("\n")  # Baris kosong setelah setiap hari

# Optional: Pencarian mahasiswa yang kosong pada hari dan sesi tertentu
day = input("Cari hari (e.g., Senin, Selasa): ")
session = input("Cari sesi kosong (e.g., 1, 2, 3, 4): ")

# Menampilkan hasil
free_students = search_free_students(free_schedule_data, day, session, lines)
print(f"\nMahasiswa yang free hari {day} pas sesi {session}:")
print("\n".join(free_students) if free_students else "Pada sesi semua.")
