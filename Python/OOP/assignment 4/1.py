pi = 22/7
class Circle:

  def __init__(self, a, b, r):
    self.x = a
    self.y = b
    self.r = r

  def Area(self):
    return pi * self.r**2

  def Perimeter(self):

    return 2 * pi * self.r

  def testBelongs(self, x, y):
    distance = ((x - self.x)**2 + (y - self.y)**2)**(1/2)
    if distance < self.r:
      return True
    else:
      return False

circleC = Circle(0, 0, 3)

print("Area of the circle: ", circleC.Area())
print("Perimeter of the circle: ", circleC.Perimeter())
print("Does the point (1,1) belongs to the circle: ", circleC.testBelongs(1, 1))
