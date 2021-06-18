from Trip import Trip


class VeniceTrip(Trip):
    def setTransport(self):
        print("Take a boat and find your way in the Grand Canal")

    def day1(self):
        print("Visit St Mark's Basilica in St Mark's Square ")

    def day2(self):
        print("Appreciate Doge's Palace")

    def day3(self):
        print("Enjoy the food near the Rialto Bridge")

    def returnHome(self):
        print("Get souvenirs for friends and get back")


class MaldivesTrip(Trip):
    def setTransport(self):
        print("On foot, on any island, Wow!!")

    def day1(self):
        print("Enjoy the marine life of Banana Reef")

    def day2(self):
        print("Go for the water sports and snorkelling")

    def day3(self):
        print("relax on the beach and enjoy the sun")

    def returnHome(self):
        print("Don't feel like leaving the beach..")
