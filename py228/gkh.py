price = {"энергия":1542,"отопление":1542,"горячая вода":92}

def show_price(usluga):
    print("цена на {0} = {1}".format(usluga, price[usluga]))

def est_usluga(usluga):
    if usluga in price:
        return True
    else:
        return False