class SagaImg:
    def __init__(self,*args):
        if len(args) == 1:
            print('открываем пикчу',args[0])
        elif len(args) == 2:
            print('открываем пикчу размерами',args[0],args[1])
        else:
            print('Создайте картинку по координатом или по назвванию')
            raise TypeError

img1 = SagaImg('котик.jpg')
img1 = SagaImg(10,20)
img1 = SagaImg(10,20,94)