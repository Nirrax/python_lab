from clinic import Patient, Clnic

clinic = Clnic()

p1 = Patient("Kowalski", "Andrzej", 43, "Anemia")
p2 = Patient("Nowak", "Barbara", 21, "Cancer")
p3 = Patient("Wisniewski", "Jan", 35, "Diabetes")

clinic.add_patient(p1)
clinic.add_patient(p2)
clinic.add_patient(p3)
clinic.show_queue()

clinic.sort_patients_by_surname()
clinic.show_queue()

clinic.sort_patients_by_age()
clinic.show_queue()

clinic.delete_patient()
clinic.show_queue()

clinic.delete_patient()
clinic.delete_patient()
clinic.show_queue()