class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News:", self.__latestNews
