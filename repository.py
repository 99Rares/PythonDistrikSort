import pickle
from termcolor import colored
from Range import range as ra
from Distrikt import Distrikt as dist


# noinspection SpellCheckingInspection
class reopsitory:
    """
    Diese Klasse analysiert die Daten aus der Datei
    """

    def __init__(self):
        self.__houses = []

    def __iter__(self):
        return iter(self.__houses)

    def __next__(self):
        lenght = len(self.__houses) - 1
        yield lenght
        while lenght >= 0:
            yield lenght
            lenght -= 1
            return next(self)
        raise StopIteration

    def readFrom_csv(self):
        """
        Die Funktion liset die Daten aus der Datei
        """
        try:
            with open('housing.csv', 'r') as data_csv:
                reader = data_csv.readlines()
        except FileNotFoundError or FileExistsError as e:
            print(str(e))
        return reader

    def parseData(self, reader):
        """
        Die Funktion bearbeitet die gelesenen Daten und speicher diese in eine Liste
        """
        try:
            printfile = open("houses", "wb")
            pickle.dump(reader, printfile)
            printfile.close()
        except UnboundLocalError as e:
            print(str(e))

        try:
            readFile = open("houses", "rb")
            inText = pickle.load(readFile)
            readFile.close()
            inText = [l.split(',') for l in inText]
        except EOFError as e:
            print(str(e))
        return inText

    def initHouse(self, inPut):
        """
        Speichert die Daten in der Datei
        """
        try:
            ID = 0
            for para in inPut:
                try:
                    houses = dist(para[0], para[1], para[2], para[3], para[4], para[5], para[6], para[7], para[8],
                                  para[9], ID)
                    self.add_house(houses)
                except ValueError:
                    pass
                ID += 1
        except UnboundLocalError as e:
            print(str(e))

    def grosste_bevolk(self):
        """
        Sucht die grosste Bevolkerung
        """
        max_pop_list = [dist.population for dist in self.__houses]
        try:
            max_pop = max(max_pop_list)
            max_pop_ID = max_pop_list.index(max_pop)
            x = str(self.__houses[max_pop_ID].population)
            print(self.__houses[max_pop_ID].__str__())
            return x
        except ValueError as e:
            print(str(e))

    def kleinste_bevolk(self):
        """
        Sucht die kleinste Bevolkerung
        """
        max_pop_list = [dist.population for dist in self.__houses]
        try:
            min_pop = min(max_pop_list)
            min_pop_ID = max_pop_list.index(min_pop)
            x = str(self.__houses[min_pop_ID].population)
            print(self.__houses[min_pop_ID].__str__())
            return x
        except ValueError as e:
            print(str(e))

    def grosste_einwohner_bedroom(self):
        """
        Sucht die grosste Anzahl von Einwohner pro Schlafzimmer
        """
        max_ein_bedroom_list = [dist.population / dist.total_bedrooms for dist in self.__houses]
        try:
            max_ein_bedroom = max(max_ein_bedroom_list)
            max_ein_bedroom_id = max_ein_bedroom_list.index(max_ein_bedroom)
            x = str(self.__houses[max_ein_bedroom_id].population / self.__houses[
                max_ein_bedroom_id].total_bedrooms)
            print(self.__houses[max_ein_bedroom_id].__str__())
            return x
        except ValueError as e:
            print(str(e))

    def kleinste_einwohner_bedroom(self):
        """
        Sucht die kleinste Anzahl von Einwohner pro Schlafzimmer
        """
        min_ein_bedroom_list = [dist.population / dist.total_bedrooms for dist in self.__houses]
        try:
            min_ein_bedroom = min(min_ein_bedroom_list)
            min_ein_bedroom_id = min_ein_bedroom_list.index(min_ein_bedroom)
            x = str(self.__houses[min_ein_bedroom_id].population / self.__houses[
                min_ein_bedroom_id].total_bedrooms)
            print(self.__houses[min_ein_bedroom_id].__str__())
            return x
        except ValueError as e:
            print(str(e))

    def avrage_einwohner_bedroom(self):
        """
        Sucht die durchschnittliche Anzahl von Einwohner pro Schlafzimmer
        """
        try:
            x = str(sum(dist.population / dist.total_bedrooms for dist in self.__houses) / len(self.__houses))
            return x
        except ZeroDivisionError as e:
            print(str(e))

    def avrage_age(self):
        """
        Berechnet den durchschnittlichen Alter
        """
        try:
            x = str(
                sum(dist.housing_median_age for dist in self.__houses) / len(self.__houses))
            return x
        except ZeroDivisionError as e:
            print(str(e))

    def avrage_income(self):
        """
        Berechnet den durchschnittlichen Einkommen
        """
        try:
            x = str(sum(dist.median_income for dist in self.__houses) / len(self.__houses))
            return x
        except ZeroDivisionError as e:
            print(str(e))

    def ocean_proxy(self):
        """
        ketegorisiert die Distrikte nach der nehe am ozean
        """
        try:
            ocean_proximity = set(dist.ocean_proximity for dist in self.__houses if dist.ocean_proximity != '')
            ocean_proximity_list = list(ocean_proximity)
            check = lambda a, b: a == b
            summ_ocean_proximity = []
            nr = sum(check(ocean_proximity_list[0], dist.ocean_proximity) for dist in self.__houses)
            summ_ocean_proximity.append(nr)
            nr = sum(check(ocean_proximity_list[1], dist.ocean_proximity) for dist in self.__houses)
            summ_ocean_proximity.append(nr)
            nr = sum(check(ocean_proximity_list[2], dist.ocean_proximity) for dist in self.__houses)
            summ_ocean_proximity.append(nr)
            nr = sum(check(ocean_proximity_list[3], dist.ocean_proximity) for dist in self.__houses)
            summ_ocean_proximity.append(nr)
            nr = sum(check(ocean_proximity_list[4], dist.ocean_proximity) for dist in self.__houses)
            summ_ocean_proximity.append(nr)

            for i in range(len(ocean_proximity_list)):
                print(str(ocean_proximity_list[i]) + ' sind: ' + str(summ_ocean_proximity[i]) + ' Hauser')
        except IndexError as e:
            print(str(e))

    def price_nearOcean(self):
        """
        Zeigt der Preis der Hauser die "nearOcean" sind
        """
        price1 = [str(dist.median_house_value) for dist in self.__houses if dist.ocean_proximity == "NEAR OCEAN"]
        print(price1)

    def test(self):
        try:
            assert self.grosste_bevolk() == '35682.0'
            assert self.kleinste_bevolk() == '3.0'
            assert self.grosste_einwohner_bedroom() == '1492.0'
            assert self.kleinste_einwohner_bedroom() == '0.07045009784735812'
            assert self.avrage_einwohner_bedroom() == '2.910410531328602'
            assert self.avrage_age() == '28.634511800998922'
            assert self.avrage_income() == '388.2720776662402'
        except AssertionError:
            print(colored('AssertionError', 'red'))

    def priceErhohen(self):
        """
        Erhoht der Preis der Hauser die "nearOcean" sind
        """
        self.price_nearOcean()
        try:
            haus = list(map(lambda dist: self.updatePreis(dist, dist.median_house_value + (
                    0.1 * dist.median_house_value)) if dist.ocean_proximity == "NEAR OCEAN" else self.updatePreis(
                dist, dist.median_house_value), self.__houses))
        except AssertionError as e:
            print(str(e))
        return haus

    @staticmethod
    def updatePreis(house, newPrice):
        """
        Aktualisiert der Preis der Bestellung
        """
        try:
            house.median_house_value = newPrice
        except Exception as e:
            print(str(e))

    def report(self, i_long, i_lat, i_val):
        """
        Schreibt die Distrikte, die in einen gegebenen Interval sind
        """

        i_hauser = list(filter(lambda
                                   x: i_lat.start < x.latitude < i_lat.stop and i_long.start < x.longitude < i_long.stop and i_val.start < x.median_house_value < i_val.stop,
                               self.__houses))
        file = "report.csv"
        self.schreiben(i_hauser, file)

    def schreiben(self, list, file):
        with open(file, "w")as out:
            out.writelines([dist.__str__() + '\n' for dist in list])

    def add_house(self, house):
        """
        Add element to list
        """
        self.__houses.append(house)

    def sorting(self):
        sortedDistrikt = sorted(self.__houses, key=lambda x: (x.ocean_proximity, x.median_house_value))
        self.schreiben(sortedDistrikt, 'sort.csv')

    @staticmethod
    def moglicheKriterien():
        """
        Die Funktion liefert das Kriterium nach dem man filtriert
        """
        option = ['=', '>=', '<=', '<', '>', 'Range']
        print(colored(option, 'yellow'))
        key = input(colored('Wehle ein Kriterium: ', 'yellow'))
        if key not in option:
            print(colored('ERROR: Kriterium nicht gefunden', 'red'))
        return key

    @staticmethod
    def moglicheSpalten():
        """
        Die Funktion liefert das Kriterium nach dem man filtriert
        """
        option = ["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population",
                  "households", "median_income", "median_house_value", "ocean_proximity"]
        print(colored(option, 'green'))
        key = input(colored('Wehle eine Spalte: ', 'yellow'))
        if key not in option:
            print(colored('ERROR: Spalte nicht gefunden', 'red'))
        return key

    def filtering_prep(self, spalte, kriterium):
        """
        Funktion fur das Vorbereiten der Filtrierung
        """

        option = ['=', '>=', '<=', '<', '>', 'Range']
        try:
            if spalte == "ocean_proximity":
                while kriterium == 'Range':
                    kriterium = input(colored('Wahle ein anderes Kriterium (>=, <=, =, <, >)', 'yellow'))
                key = input(colored('Wahle aus der 5 Kategorien: ', 'yellow'))
            elif kriterium == 'Range':
                key = ra(float(input('start: ')), float(input('\nstop: ')))
            elif kriterium in option:
                key = float(input(colored('Wert nach dem man filtrieren will:', 'yellow')))
        except ValueError as e:
            print(str(e))
        try:
            self.filtering(spalte, kriterium, key)
        except UnboundLocalError as e:
            print(str(e))

    def filtering(self, spalte, kriterium, key):
        """
        Filter fur die Spalten:
        """
        filterList = []
        if kriterium == "<":
            filterList = list(
                filter(lambda d: d.__dict__["_Distrikt__" + spalte] < key, self.__houses))
        elif kriterium == ">":
            filterList = list(
                filter(lambda d: d.__dict__["_Distrikt__" + spalte] > key, self.__houses))
        elif kriterium == "<=":
            filterList = list(
                filter(lambda d: d.__dict__["_Distrikt__" + spalte] <= key, self.__houses))
        elif kriterium == ">=":
            filterList = list(
                filter(lambda d: d.__dict__["_Distrikt__" + spalte] >= key, self.__houses))
        elif kriterium == "=":
            filterList = list(
                filter(lambda d: d.__dict__["_Distrikt__" + spalte] == key, self.__houses))
        elif kriterium == "Range":
            filterList = list(
                filter(lambda d: ra.start < d.__dict__["_Distrikt__" + spalte] < ra.stop, self.__houses))
        self.schreiben(filterList, 'filter.csv')

    def run(self):
        """
        Die Funktion ruft die Methoden der Klasse auf
        """
        self.initHouse(self.parseData(self.readFrom_csv()))
        print(colored('\n' + 'Grosste Bevolkerung:', 'blue'))
        print(self.grosste_bevolk(), end='')
        print(colored('\n' + 'Kleinste Bevolkerung:', 'blue'))
        print(self.kleinste_bevolk(), end='')
        print(colored('\n' + 'Grosste Anzahl von Einwohner pro Schlafzimmer:', 'blue'))
        print(self.grosste_einwohner_bedroom(), end='')
        print(colored('\n' + 'Kleinste Anzahl von Einwohner pro Schlafzimmer:', 'blue'))
        print(self.kleinste_einwohner_bedroom(), end='')
        print(colored('\n' + 'Durchschnittliche Anzahl von Einwohner pro Schlafzimmer:', 'blue'))
        print(self.avrage_einwohner_bedroom(), end='')
        print(colored('\n' + 'Durchschnittlichen Alter:', 'blue'))
        print(self.avrage_age(), end='')
        print(colored('\n' + 'Durchschnittlichen Einkommen:', 'blue'))
        print(self.avrage_income(), end='')
        print(colored('\n' + 'Anzahl von Distrikte aus jeder Kategorie:', 'blue'))
        self.ocean_proxy()
        print(colored('\n' + 'Preiserhohung:', 'red'))
        self.priceErhohen()
        self.price_nearOcean()
        self.sorting()
        self.filtering_prep(self.moglicheSpalten(), self.moglicheKriterien())

        try:
            print(colored('longitude: ', 'yellow'))
            start = -119  # input('start: ')
            stop = -118  # input('stop: ')
            i_long = ra(start, stop)
            print(colored('latitude: ', 'yellow'))
            start = 30  # input('start: ')
            stop = 34  # input('stop: ')
            i_lat = ra(start, stop)
            print(colored('median_house_value: ', 'yellow'))
            start = 50000  # input('start: ')
            stop = 60000  # input('stop: ')
            i_val = ra(start, stop)
            self.report(i_long, i_lat, i_val)
        except ValueError as e:
            print(str(e))
            self.test()
