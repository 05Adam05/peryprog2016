import gkh
usluga = input("Введите услугу жкх: ")
if gkh.est_usluga(usluga):
    gkh.show_price(usluga)
else:
   print("Нет такой услуги, дебил")   