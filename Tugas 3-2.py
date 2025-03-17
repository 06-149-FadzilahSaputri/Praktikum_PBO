import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type  

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type  

class Child(Father, Mother):
    def __init__(self, father_blood, mother_blood):
        Father.__init__(self, father_blood)
        Mother.__init__(self, mother_blood)

        self.child_blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        alel_ayah = random.choice(self.blood_type)  
        alel_ibu = random.choice(self.blood_type)

        kombinasi = {alel_ayah, alel_ibu} 

        if kombinasi == {"A"}:
            return "A"
        elif kombinasi == {"B"}:
            return "B"
        elif kombinasi == {"A", "B"}:
            return "AB"
        elif kombinasi == {"O"}:
            return "O"
        elif kombinasi == {"A", "O"}:
            return "A"
        elif kombinasi == {"B", "O"}:
            return "B"

    def __str__(self):
        return f"Golongan darah anak: {self.child_blood_type}"

golongan_ayah = input("Masukkan golongan darah ayah (A, B, AB, atau O): ").upper()
golongan_ibu = input("Masukkan golongan darah ibu (A, B, AB, atau O): ").upper()

anak = Child(golongan_ayah, golongan_ibu)

print(anak)
