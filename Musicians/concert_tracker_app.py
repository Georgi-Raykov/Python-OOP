from Musicians.band import Band
from Musicians.band_members.drummer import Drummer
from Musicians.band_members.guitarist import Guitarist
from Musicians.band_members.singer import Singer
from Musicians.concert import Concert


class ConcertTrackerApp:

    def __init__(self):

        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):

        valid_musicians = {'Guitarist': Guitarist, 'Drummer': Drummer, 'Singer': Singer}

        if musician_type not in valid_musicians:
            raise ValueError('Invalid musician type!')
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        musician = valid_musicians[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name):

        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")
        band = Band(name)

        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):

        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f'{place} is already registered for {genre} concert!')
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):

        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):

        band = self.__find_band_by_name(band_name)
        musician = self.__find_musician_by_name(musician_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):

        concert = self.__find_concert_by_place(concert_place)

        band = self.__find_band_by_name(band_name)

        valid_band = self.__valid_band(band)
        if not valid_band:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        if concert.genre == 'Rock':
            for musician in band.members:
                if musician.__class__.__name__ == 'Drummer' and 'play the drums with drumsticks' \
                        not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif musician.__class__.__name__ == 'Singer' and 'sing high pitch notes' not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif musician.__class__.__name__ == 'Guitarist' and 'play rock' not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == 'Metal':
            for musician in band.members:
                if musician.__class__.__name__ == 'Drummer' and 'play the drums with drumsticks' \
                        not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif musician.__class__.__name__ == 'Singer' and 'sing low pitch notes' not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif musician.__class__.__name__ == 'Guitarist' and 'play metal' not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == 'Jazz':
            for musician in band.members:
                if musician.__class__.__name__ == 'Drummer' and 'play the drums with drum brushes' \
                        not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif musician.__class__.__name__ == 'Singer' and 'sing low pitch notes' not in musician.valid_skills \
                        and 'sing high pitch notes' not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif musician.__class__.__name__ == 'Guitarist' and 'play jazz' not in musician.valid_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    def __find_concert_by_place(self, place):

        for concert in self.concerts:
            if concert.place == place:
                return concert
        return None

    def __valid_band(self, band_object):

        count_type_members = {'Drummer': 0, 'Guitarist': 0, 'Singer': 0}

        for band in band_object.members:
            if band.__class__.__name__ == 'Drummer':
                count_type_members[band.__class__.__name__] += 1
            elif band.__class__.__name__ == 'Guitarist':
                count_type_members[band.__class__.__name__] += 1
            elif band.__class__.__name__ == 'Singer':
                count_type_members[band.__class__.__name__] += 1
        if count_type_members['Drummer'] >= 1 and count_type_members['Guitarist'] >= 1 and \
                count_type_members['Singer'] >= 1:
            return True
        return False

    def __find_band_by_name(self, name):

        for band in self.bands:
            if band.name == name:
                return band
        return None

    def __find_musician_by_name(self, name):

        for musician in self.musicians:
            if musician.name == name:
                return musician
        return None
