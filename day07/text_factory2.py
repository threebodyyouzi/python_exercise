class Vendor:
    def __init__(self,em,ph):
        self.em=em
        self.ph=ph
class BearToy:
    def __init__(self,name,size,color):
        #实例化时,将会自动调用init方法
        self.name=name
        self.size=size
        self.color=color
        # self.Vendor=Vendor(em,ph)
    def sing(self):
        print("I am %s and I am %s" % (self.size,self.color))
class NewBearToy(BearToy):
    # def run(self):
    #     print("call ")
    # pass
    def __init__(self,name,size,color,date):
        super(NewBearToy,self).__init__(name,size,color)
        self.date=date
    def run(self):
        print("run u clear boy")

if __name__ == '__main__':
    # big=NewBearToy("small","blue","admin@tedu.com","400100123456")
    # print(big.Vendor.ph)
    # big.run()
    big =NewBearToy("bearA","small","white","20181115")
    big.sing()
    big.run()