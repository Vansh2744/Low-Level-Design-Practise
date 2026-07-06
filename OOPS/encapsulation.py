class Subscription:
    def __init__(self, is_subscribed, amount_paid):
        self.__is_subscribed = is_subscribed
        self.__amount_paid = amount_paid

    def info(self):
        print(f"Subscribed : {self.__is_subscribed}  Amount : {self.__amount_paid}")

sub = Subscription(False, 0)
sub.__is_subscribed = True
sub.__amount_paid = 999
sub.info()
