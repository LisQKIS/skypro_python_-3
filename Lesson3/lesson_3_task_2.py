from smartphone import Smartphone
catalog = []

catalog.append(Smartphone("Apple", "iPhone 12", "+79266666666"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79266666666"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79266666666"))
catalog.append(Smartphone("OnePlus", "7 Pro", "+79266666666"))
catalog.append(Smartphone("Google", "Pixel 4", "+79266666666"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")