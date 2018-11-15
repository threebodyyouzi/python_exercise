class Book:
    def __init__(self,name,author,page):
        self.name=name
        self.author=author
        self.page=page
    def __str__(self):
        return "<<%s>>" % self.name
    def __call__(self):
        print("<<%s>> is written by %s" % (self.name,self.author))

if __name__ == '__main__':
    core=Book("Hello","world",10000)
    print(core)
    core()