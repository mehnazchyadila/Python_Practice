class triangle:
    base = ""
    height = ""


    def calculate_area(self,base,height):
        self.base = base
        self.height = height
        result = .5 * self.base * self.height
        print(result)


t1 = triangle()
t1.calculate_area(10,20)

t2 = triangle()
t2.calculate_area(20,30)

