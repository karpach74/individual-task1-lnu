class Students:
    def __init__(self, countg, countb):
        self.g = countg
        self.b = countb
    def __str__(self):
        return f' {'*' * self.g}({self.g}Д), {'*' * self.b}({self.b}Х)'
    def sum(self):
        return self.g + self.b
    def __sub__(self, count):
        return Students(max(0, self.g - count), max(0, self.b - count))
class Group(Students):
    def __init__(self, countg, countb, cipher):
        Students.__init__(self,countg, countb)
        self.c = cipher
    def specialisation(self):
        specialisations = {
            'МТС-21': 'Статистика',
            'МТМ-11': 'Математика',
            'МТП-41': 'Прикладна'
            }
        return specialisations.get(self.c, "Невідома спеціалізація")
    def __str__(self):
        return f"Група {self.c} ({self.specialisation()}): {Students.__str__(self)}"
    def __lt__(self, others):
        return self.sum() < others.sum()

class Groups:
    def __init__(self):
        self.list_of_groups = []
    def __str__(self):
        return "\n".join(str(group) for group in self.list_of_groups)
    def addGroup(self, countg, countb, cipher):
        group = Group(countg, countb, cipher)
        self.list_of_groups.append(group)
    def download_from_file(self, filename, countg, countb, cipher):
        with open(filename, "r", encoding = "utf-8") as file:
           for line in file:
               parts = line.strip().split(",")
               countg, countb, cipher = int(parts[0]), int(parts[1]), parts[2]
               group = Group(countg, countb, cipher)
               self.list_of_groups.append(group)
    def biggest_group(self, groups):
        biggest = groups[0]
        for group in groups[1:]:
            if group.sum() > biggest.sum():
                biggest = group
        return biggest
    def biggest_groups_by_specialisation(self):
        specialisations = {}
        for group in self.list_of_groups:
            spec = group.specialisation()
            if spec in specialisations:
                specialisations[spec].append(group)
            else:
                specialisations[spec] = [group]

        biggest_groups = {}
        for spec in specialisations:
            biggest_group = specialisations[spec][0]
            for group in specialisations[spec][1:]:
                if group.sum() > biggest_group.sum():
                    biggest_group = group
            biggest_groups[spec] = biggest_group

        print("Найбільші групи за кожною спеціальністю:")
        for spec in biggest_groups:
            print(biggest_groups[spec])
