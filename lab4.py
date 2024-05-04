#Створення класів
class Begin:
    def process_message(self):
        return "Begin"

class BI(Begin):
    def process_message(self):
        return "Big"

class M(Begin):
    def process_message(self):
        return "Men"

class C(Begin):
    def process_message(self):
        return "Cat"

class T(BI):
    def process_message(self):
        return "Bitter"

class E(BI, M, C):
    def process_message(self):
        return "Women"

class A(C):
    pass

class R(T, E):
    pass

class N(E, A):
    pass

def main():
    r_object = R()
    n_object = N()

    #Викликаємо обробник для класу R
    print("Message for R:", r_object.process_message())

    #Викликаємо обробник для класу N
    print("Message for N:", n_object.process_message())

#Виклик функції main
if __name__ == "__main__":
    main()
