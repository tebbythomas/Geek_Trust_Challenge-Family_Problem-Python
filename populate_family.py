'''
Description: This class is used to contruct the family tree according 
to the problem definition. The root is created first - King Shan.
All subsequenet family members are added via two operations:
1. Add child
2. Add spouse
'''

from person import Person
from family_functions import Family_Functions as Fam_Func


class Populate_Family:
    def populate_family(self, shan):
        obj = Fam_Func()
        obj.add_spouse(shan, Person("Anga", "Female"))
        anga = obj.find_person(shan, "Anga")
        if anga is not None:
            obj.add_child(anga, Person("Chit", "Male"))
            obj.add_child(anga, Person("Ish", "Male"))
            obj.add_child(anga, Person("Vich", "Male"))
            obj.add_child(anga, Person("Aras", "Male"))
            obj.add_child(anga, Person("Satya", "Female"))
        chit = obj.find_person(shan, "Chit")
        if chit is not None:
            obj.add_spouse(chit, Person("Amba", "Female"))
        vich = obj.find_person(shan, "Vich")
        if vich is not None:
            obj.add_spouse(vich, Person("Lika", "Female"))
        aras = obj.find_person(shan, "Aras")
        if aras is not None:
            obj.add_spouse(aras, Person("Chitra", "Female"))
        satya = obj.find_person(shan, "Satya")
        if satya is not None:
            obj.add_spouse(satya, Person("Vyan", "Male"))
        amba = obj.find_person(shan, "Amba")
        if amba is not None:
            obj.add_child(amba, Person("Dritha", "Female"))
            obj.add_child(amba, Person("Tritha", "Female"))
            obj.add_child(amba, Person("Vritha", "Male"))
        dritha = obj.find_person(shan, "Dritha")
        if dritha is not None:
            obj.add_spouse(dritha, Person("Jaya", "Male"))
        lika = obj.find_person(shan, "Lika")
        if lika is not None:
            obj.add_child(lika, Person("Vila", "Female"))
            obj.add_child(lika, Person("Chika", "Female"))
        chitra = obj.find_person(shan, "Chitra")
        if chitra is not None:
            obj.add_child(chitra, Person("Jnki", "Female"))
            obj.add_child(chitra, Person("Ahit", "Male"))
        jnki = obj.find_person(shan, "Jnki")
        if jnki is not None:
            obj.add_spouse(jnki, Person("Arit", "Male"))
        satya = obj.find_person(shan, "Satya")
        if satya is not None:
            obj.add_child(satya, Person("Asva", "Male"))
            obj.add_child(satya, Person("Vyas", "Male"))
            obj.add_child(satya, Person("Atya", "Female"))
        asva = obj.find_person(shan, "Asva")
        if asva is not None:
            obj.add_spouse(asva, Person("Satvy", "Female"))
        vyas = obj.find_person(shan, "Vyas")
        if vyas is not None:
            obj.add_spouse(vyas, Person("Krpi", "Female"))
        if dritha is not None:
            obj.add_child(dritha, Person("Yodhan", "Male"))
        if jnki is not None:
            obj.add_child(jnki, Person("Laki", "Male"))
            obj.add_child(jnki, Person("Lavnya", "Female"))
        satvy = obj.find_person(shan, "Satvy")
        if satvy is not None:
            obj.add_child(satvy, Person("Vasa", "Male"))
        krpi = obj.find_person(shan, "Krpi")
        if krpi is not None:
            obj.add_child(krpi, Person("Kriya", "Male"))
            obj.add_child(krpi, Person("Krithi", "Female"))
    