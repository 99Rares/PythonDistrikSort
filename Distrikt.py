class Distrikt:
    """
    Klasse fur den Objekt Distrikt. 
    Attribute: longitude (float), latitude (float), housing_median_age (float), 
    total_rooms (float), total_bedrooms (float), population (float), households (float), median_income (float), 
    median_house_value (float), ocean_proximity (string), ID (int) 
    """

    def __init__(self, longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households,
                 median_income, median_house_value, ocean_proximity, ID):
        self.__longitude = float(longitude)
        self.__latitude = float(latitude)
        self.__housing_median_age = float(housing_median_age)
        self.__total_rooms = float(total_rooms)
        self.__total_bedrooms = float(total_bedrooms)
        self.__population = float(population)
        self.__households = float(households)
        self.__median_income = float(median_income)
        self.__median_house_value = float(median_house_value)
        self.__ocean_proximity = ocean_proximity[:-1]
        self.__ID = int(ID)

    def __str__(self):
        """
        Die Funktion andert die print-Methode fur den Objekt Distrikt
        """
        return 'Distrikt Nr: ' + str(self.__ID) +' ' + 'Located at: ' + str(self.__longitude) + ' ' + str(self.__latitude) + \
               ' ' + 'housing_median_age: ' + str(self.__housing_median_age) + \
               ' ' + 'total_rooms: ' + str(self.__total_rooms) + \
               ' ' + 'total_bedrooms: ' + str(self.__total_bedrooms) + \
               ' ' + 'population: ' + str(self.__population) + \
               ' ' + 'households: ' + str(self.__households) + \
               ' ' + 'median_income: ' + str(self.__median_income) + \
               ' ' + 'median_house_value: ' + str(self.__median_house_value) + \
               ' ' + 'ocean_proximity: ' + str(self.__ocean_proximity)

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, long):
        self.__longitude = long

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, lati):
        self.__latitude = lati

    @property
    def housing_median_age(self):
        return self.__housing_median_age

    @housing_median_age.setter
    def housing_median_age(self, house):
        self.__housing_median_age = house

    @property
    def total_rooms(self):
        return self.__total_rooms

    @total_rooms.setter
    def total_rooms(self, total):
        self.__total_rooms = total

    @property
    def total_bedrooms(self):
        return self.__total_bedrooms

    @total_bedrooms.setter
    def total_bedrooms(self, total):
        self.__total_bedrooms = total

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, popul):
        self.__population = popul

    @property
    def households(self):
        return self.__households

    @households.setter
    def households(self, house):
        self.__households = house

    @property
    def median_income(self):
        return self.__median_income

    @median_income.setter
    def median_income(self, inc):
        self.__median_income = inc

    @property
    def median_house_value(self):
        return self.__median_house_value

    @median_house_value.setter
    def median_house_value(self, val):
        self.__median_house_value = val

    @property
    def ocean_proximity(self):
        return self.__ocean_proximity

    @ocean_proximity.setter
    def ocean_proximity(self, ocean):
        self.__ocean_proximity = ocean

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        self.__ID = ID


