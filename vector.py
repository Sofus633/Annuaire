import math


class Vector3:
    def __init__(self, vect=[0, 0, 0]):
        self.vec = vect
        
    def updpos(self, vect):
        return [vect[0] + self.vec[0], vect[1] + self.vec[1], vect[2] + self.vec[2]]
    def __add__(self, vect):    
        return Vector3([vect.vec[0] + self.vec[0], vect.vec[1] + self.vec[1], vect.vec[2] + self.vec[2]])
    def __mul__(self, num):
        return Vector3((num * self.vec[0], num *  self.vec[1], num *  self.vec[2]))
    def __str__(self):
        return f"{self.vec[0]}, {self.vec[1]}, {self.vec[2]}"
    def magnitude(self):
        return math.sqrt(self.vec[0]**2 + self.vec[1]**2 + self.vec[2]**2)
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector3((0, 0, 0))  # Handle zero vector
        return Vector3((self.vec[0] / mag, self.vec[1] / mag, self.vec[2] / mag))
    def neg(self, dir):
        if dir in ("xy", "yx"):
            return Vector3((-self.vec[0], -self.vec[1], self.vec[2]))
        if dir == "y":
            return Vector3((self.vec[0], -self.vec[1], self.vec[2]))
        if dir == "x":
            return Vector3((-self.vec[0], self.vec[1], self.vec[2]))
        else:
            raise Exception(f"neg {dir} n'existe pas essayer x ou y")
        
if __name__ == "__main__":
    
    vec1 = Vector3([10, 0, 9])
    vec2 = Vector3([80, 9, 0])
    vec1 += vec2
    print(vec1)