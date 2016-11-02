class Human:
    def __init__(self,name,ears,iq,soul):
        self.name = name
        self.ears = ears
        self.iq = iq
        self.soul = soul
    
    def walk(self):
        print('Я хожу')

    def breath(self):
        print('Я дышу')

    def kill(self,somebody):
        print('{1} убил {0}'\
            .format(somebody.name,self.name))


tina = Human('Тинамагомед',2,120,True)
print(tina.name)
print(tina.soul)
# tina.soul = False
# print(tina.soul)
tina.walk()
gadzhi = Human('Гаджи',2,-500,False)
gadzhi.breath()
gadzhi.kill(tina)