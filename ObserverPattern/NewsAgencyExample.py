from NewsPublisher import NewsPublisher
from Subscriber import SMSSubscriber, EmailSubscriber, AnyOtherSubscriber


if __name__ == "__main__":
    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("\nSubscribers: ", news_publisher.subscribers())

    news_publisher.addNews('Hello World!')
    news_publisher.notifySubscribers()

    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.addNews('New World!!')
    news_publisher.notifySubscribers()
