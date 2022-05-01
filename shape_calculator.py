class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width+2*self.height

    def get_diagonal(self):
        return (self.width ** 2+self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('*'*self.width+'\n')*self.height

    def get_amount_inside(self, shape):
        if(self.height < shape.height or self.width < shape.width):
            return 0
        return (int(self.height / shape.height)) * (int(self.width / shape.width))

    def __repr__(self):
        return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def __repr__(self):
        return 'Square(side='+str(self.width)+')'
