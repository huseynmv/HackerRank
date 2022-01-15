
import sys
def carParkingRoof(cars, k):
    cars.sort()
    n = len(cars)
    x = sys.maxsize
    for i in range(n-k+1):
        x = min(x, cars[i+k-1] -cars[i])
    print(x+1)

cars = [6,2,12,7]
k=3

carParkingRoof(cars, k)


