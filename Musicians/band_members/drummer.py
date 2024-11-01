from Musicians.band_members.musician import Musician


class Drummer(Musician):

    valid_skills = ['play the drums with drumsticks', 'play the drums with drum brushes', 'read sheet music']

    def __init__(self, name, age):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill):

        if new_skill not in self.valid_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f'{new_skill} is already learned!')
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."
