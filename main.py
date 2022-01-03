class Ab1(object):
    def __init__(self, h1, w1):
        self.val1=5
        self.height=h1
        self.width=w1

    def gothere(self):
        self.val1 = 6
        self.width /= 2


class Bb1(Ab1):
    def __init__(self, g1, g2):
        super().__init__(g1, g2)
        self.width *= 2


    #   super().__init__()
    #   pass


f = Bb1(72, 56)
f.gothere()
print(f.height, f.width)

