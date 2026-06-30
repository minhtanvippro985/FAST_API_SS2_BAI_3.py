from fastapi import FastAPI

app = FastAPI()


students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students/active")
def get_active_students():
    active_students = []
    for people in students:
        if people['status'] == "active":
            active_students.append(people)
        
    if len(active_students) == 0:
        return {
            "message" : "Không có sinh viên nào đang học",
            "data" : [] 
        }
    else:
        return{
            "message" : "Danh sách sinh viên đang học",
            "data" : active_students
        }
    
#input của bài toán là đường dẫn path
#output là hiển thị chỉ học sinh hiện đang học
# điều kiện để xác định sinh viên đang học là có "status" = "active"