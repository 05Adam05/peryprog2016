pizzas = {"ассорти":210,"маргарита":200,"пепперони":190}

def zakazat(zakaz,summa):
    print("Вы заказываете {0} pf {1} р".format(zakaz,pizzas[zakaz]))
    summa += pizzas[zakaz]
    return summa 
