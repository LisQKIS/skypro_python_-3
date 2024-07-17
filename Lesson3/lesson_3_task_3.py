from adress import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Берюзовский бульвар", "19", "19")
to_address = Address("654321", "Санкт-Петербург", "Чернышевский проспект", "45", "45")

mailing = Mailing(to_address, from_address, 450, "TRACK12345678")

print(mailing)