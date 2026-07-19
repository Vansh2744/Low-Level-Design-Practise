from waiter import Waiter
from chef import Chef
from burger import Burger
from pizza import Pizza

ch = Chef()
wt = Waiter()

bur = Burger(ch)
piz = Pizza(ch)

wt.give_food(bur)
wt.give_food(piz)