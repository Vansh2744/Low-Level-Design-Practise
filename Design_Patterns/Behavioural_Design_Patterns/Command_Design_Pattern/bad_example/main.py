from chef import Chef
from waiter import Waiter

ch = Chef()
wait = Waiter(ch)

wait.cook_food("burger")
wait.cook_food("french fries")
