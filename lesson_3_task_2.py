from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79234567890"),
    Smartphone("Xiaomi", "13T", "+79345678901"),
    Smartphone("Google", "Pixel 9", "+79456789012"),
    Smartphone("Huawei", "P60 Pro", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
