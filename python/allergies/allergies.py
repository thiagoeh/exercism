class Allergies(object):
    def __init__(self, score):
        self.allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128,
        }
        self.score = score

    def is_allergic_to(self, item):
        return (self.allergens[item] & self.score) > 0

    @property
    def lst(self):
        allergens_list = []
        for allergen in self.allergens:
            if (self.allergens[allergen] & self.score) > 0:
                allergens_list.append(allergen)
        return allergens_list
