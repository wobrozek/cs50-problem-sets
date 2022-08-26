
"""
implement a class details here: https://cs50.harvard.edu/python/2022/psets/8/jar/
"""
class Jar:
    def __init__(self,capacity=12):
        if capacity <0:
            raise ValueError("Invalid capacity")
        self.__capacity = capacity
        self.__size=0

    def __str__(self):
        return "🍪"*self.__size

# that function is using seter that controls size < capacity
    def deposit(self,n):
        self.size+=n


    def withdraw(self,n):
        if self.__size-n>=0:
            self.__size-=n
        else:
            raise ValueError("You do not have enough cookies in a jar ")

    @property
    def capacity(self):
        return self.__capacity

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        if size > self.__capacity:
            raise ValueError("You do not have enough space in a jar")
        self.__size = size


def main():
    jar=Jar()
    jar.deposit(2)

if __name__ =="__main__":
    main()