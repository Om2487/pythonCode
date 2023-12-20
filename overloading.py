class square:
    def __init__(self,side):
        self.side=side
    def __add__(squareone,square2):
        return ((4*squareone.side)+ (4*square2.side))


squareone=square(5)
square2=square(10)
print("Sum of the side of both the squares =",squareone+square2)