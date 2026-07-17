from discount_service import DiscountService
from diwali import Diwali
from holi import Holi

diw = Diwali()
hol = Holi()

dis = DiscountService(diw)
dis.process_discount()
dis.change_strategy(hol)
dis.process_discount()