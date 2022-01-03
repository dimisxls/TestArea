
class Storey:
    def __init__(self, people=0):
        self.people = people


class Building:
    def __init__(self, number_storeys):
        self.storeys = [Storey() for _ in range(number_storeys)]    #   Δημιουργεί μια Λίστα με αντικείμενα απο την κλάση Storey
        print(type(self.storeys))       # Λίστα
        print(type(self.storeys[0]))    # Κλάση Storey

    def add_people(self, storey, people):
        self.storeys[storey].people += people

    def print_people(self):
        for i in range(len(self.storeys)):
            print(f"Storey {i}: {self.storeys[i].people} people")


b = Building(4)     # Δημιουργεί μια λίστα με 4 κενά αντικείμενα κλάσης Storey

b.add_people(0, 2)  #   Βάζει τιμές στο 0 αντικείμενο της λίστας
b.add_people(1, 3)  #   Βάζει τιμές στο 1 αντικείμενο της λίστας
b.add_people(2, 6)  #   Βάζει τιμές στο 2 αντικείμενο της λίστας

b.print_people()
