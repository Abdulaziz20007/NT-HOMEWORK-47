# Talaba nomli klass e'lon qiling va unda
# property:   `name, age`
# Kurs nomli klass e'lon qiling va unda
# property:   `kurs_name, kurs_teacher, talabalar_soni=0, talabalar=[]`
# methods:    `add(new_student), delete(new_student), info_kurs()`
# Sizning vazifangiz:

# 1. 2ta Kurs e'lon qilasizlar va har bitta kursga 10tadan talaba qo'shish kerak
# 2. 2ta talabani kursdan haydash kerak

class Talaba():
    id = 1
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.id = Talaba.id
        Talaba.id += 1


class Teacher():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Kurs():
    def __init__(self, kurs_name, kurs_teacher, talabalar_soni=0, talabalar=[]) -> None:
        if type(kurs_teacher) != Teacher:
            raise TypeError("O'qituvchi ma'lumotlari class turida bo'lishi kerak!")
        self.kurs_teacher = kurs_teacher
        self.kurs_name = kurs_name
        self.talabalar_soni = talabalar_soni
        self.talabalar = talabalar
    
    def add_student(self, talaba):
        # self.talabalar.append({'id': talaba.id, 'name': talaba.name, 'age': talaba.age})
        if talaba in self.talabalar:
            print("Bu talaba avval qo'shilgan")
        else:
            self.talabalar.append(talaba)
            self.talabalar_soni += 1

    def delete_student(self, talaba):
        # self.talabalar = list(filter(lambda x: x['id'] != id, self.talabalar))
        if talaba in self.talabalar:
            self.talabalar.remove(talaba)
        else: 
            print('Kursda bunday talaba mavjud emas!')
        self.talabalar_soni = len(self.talabalar)
    
    def info(self):
        print("----------------------------")
        print("Kurs nomi:", self.kurs_name)
        print("Kurs o'qituvchisi:", self.kurs_teacher.name, self.kurs_teacher.age, 'yosh')
        print("Talabalar soni:", self.talabalar_soni)
        if self.talabalar_soni == 0:
            print("Talabalar mavjud emas!")
        else:
            print("----------------------------")
            print('Talabalar:')
            for i in self.talabalar:
                print("Id:", i.id, "Ism:", i.name, "Yosh:", i.age)
        print("----------------------------")

    def change_teacher(self, teacher: Teacher):
        if not isinstance(teacher, Teacher):
            print("O'qituvchi ma'lumotlari class turida bo'lishi kerak!")
        else:
            self.kurs_teacher = teacher

talaba1 = Talaba('1-Talaba_ismi', 15)
teacher1 = Teacher("Asad", 21)
teacher2 = Teacher("Murod", 29)
kurs1 = Kurs("1-Kurs", teacher1)
kurs2 = Kurs("2-Kurs", teacher2)
temp_names = [["Alice", 29], ["Bob", 34], ["Charlie", 27], ["Diana", 42], ["Edward", 31], ["Fiona", 22], ["George", 38], ["Hannah", 25], ["Iris", 30], ["Jack", 45], ["Karen", 33], ["Liam", 28], ["Mia", 26], ["Noah", 37], ["Olivia", 40], ["Paul", 32], ["Quincy", 24], ["Rachel", 35], ["Sam", 29], ["Tina", 41], ["Ursula", 27], ["Victor", 44]]

for i in range(10):
    kurs1.add_student(Talaba(temp_names[i][0], temp_names[i][1]))

kurs1.info()

for i in range(10, 20):
    kurs2.add_student(Talaba(temp_names[i][0], temp_names[i][1]))

kurs2.info()

kurs1.delete_student(kurs1.talabalar[0])
kurs1.delete_student(kurs1.talabalar[1])
kurs1.info()

kurs2.delete_student(kurs2.talabalar[0])
kurs2.delete_student(kurs2.talabalar[1])
kurs2.info()