class Point2D:

    def __init__(self, points):
        self.points = points
        self.x = points[0]
        self.y = points[1]
    
    def getX(self):
        return self.points[0]

    def getY(self):
        return self.points[1]

    def __str__(self):
        return f"[{self.x},{self.y}]"