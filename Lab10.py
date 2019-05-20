class TouristTour:
    tourWasCanceled = 0

    def __init__(self, country = "none", lengthInDays = "none", priceInEuro = "none", transport = "none", company = "none", month = "none"):
        self._country = country
        self._length = lengthInDays
        self._price = priceInEuro
        self._transport = transport
        self._company = company
        self._month = month

    def __del__(self):
        print("Я видалив місяць", self._month)

    def __str__(self):
        return"Country: {0}, Length {1}, price {2}, transport {3}, company {4}, month {5}.\n".format(self._country, self._length, self._price, self._transport, self._company, self._month)

    @staticmethod
    def canceledTours(numberOfCanceledTours):
        TouristTour.tourWasCanceled += numberOfCanceledTours


London = TouristTour("London", 4, 230, "Truck", "Airlines", "may")
Russia = TouristTour()

print("\n")
print(London)
print(Russia)

print("Tour was canceled - " + str(London.tourWasCanceled))
London.canceledTours(0)
print("Tour was canceled - " + str(London.tourWasCanceled))