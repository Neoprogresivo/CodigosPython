import math as m

class Punto:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def getX(self):
        return self.x     
    def getY(self):
        return self.y 
    def setX(self, x):
        self.x = x 
    def setY(self, y):
        self.y = y

    def __str__(self):
        return f"{self.getX()} {self.getY()}"

def distanciaEuclidiana(a, b):
    return m.sqrt(m.pow((b.getX() - a.getX()),2) + m.pow((b.getY() - a.getY()),2))

p = Punto()
p.setX(4)
p.setY(3)
print(p)

q = Punto()
q.setX(-3)
q.setY(-4)
print(q)

distancia = distanciaEuclidiana(p,q)
print(distancia)