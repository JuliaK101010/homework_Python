from address import Address
from mailing import Mailing

from_address = Address("101000", "Москва", "Тверская", "12", "5")
to_address = Address("190000", "Санкт-Петербург", "Невский пр.", "25", "10")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track="TRACK12345"
)


print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
