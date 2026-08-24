class Student:

    def __init__(self, student_id, name, age, class_name, marks=0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.class_name = class_name
        self.marks = marks

    def display_info(self):
        print("\n------ Student Details ------")
        print(f"ID      : {self.student_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Class   : {self.class_name}")
        print(f"Marks   : {self.marks}")
    

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "class_name": self.class_name,
            "marks": self.marks
        }