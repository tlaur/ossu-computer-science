class Wizard():
    def __init__(self, name) -> None:
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house) -> None:
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defence Against the Dark Arts")

if __name__ == "__main__":
    main()