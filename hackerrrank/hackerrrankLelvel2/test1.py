class Car:
    def __init__(self, speed, unit):
        self.speed = speed
        self.unit = unit

    def __str__(self):
        return f"Car with the maximum speed of {self.speed} {self.unit}"

class Boat:
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return f"Boat with the maximum speed of {self.speed} knots"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    q = int(data[0])  # Number of queries

    for i in range(1, q + 1):
        query = data[i]
        parts = query.split()
        if parts[0] == "car":
            speed = int(parts[1])
            unit = parts[2]
            vehicle = Car(speed, unit)
        elif parts[0] == "boat":
            speed = int(parts[1])
            vehicle = Boat(speed)
        print(vehicle)

if __name__ == "__main__":
    main()
