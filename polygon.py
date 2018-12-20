import math
def polygon(e,n):
      c = n * e
      a = (1/4) * n * pow(e,2) * (1/math.tan(math.pi/n))
      return c,a
while 1:
    print(polygon(int(input("Kenar Uzunlugu : ")) , int(input("Kenar Sayisi : "))))
