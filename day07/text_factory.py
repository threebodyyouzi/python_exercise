class BearToy:
    def __init__(self,size,color):
        #实例化时,将会自动调用init方法
        self.size=size
        self.color=color
    def sing(self):
        print("I am %s and I am %s" % (self.size,self.color))
if __name__ == '__main__':
    big =BearToy("Large","Brown")
    second=BearToy("Middle","Red")
    # print(BearToy.big.size)
    print(big.size)
    print(big.color)
    big.sing()
    second.sing()