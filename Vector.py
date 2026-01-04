'''
    Vector
    - Handles calculation calls

    Targets
    1. constructing vector
    2. Computing functions
        - length
        - angle
        - direction / unit vector
    3. representation
        - transpose
        - basic operations of addition and multiplication
'''
import math

class Vector:
    ''' Takes list of numbers and forms vector object with
        Functions
        1. length() --> length of vector from origin
        2. angle() --> angle from origion of projection
        3. unit() --> unit vector
        4. transpose() --> transpose of vector
        5. add(Vector V) --> Adds the vector
        6. multiply(Vector v) --> multiple of vector
    '''
    def __init__(self, number_list):
        self.vector = []
        # Initialise vector
        for num in number_list:
            self.vector.append(float(num))

        # Vector basic qualities

    def length(self):
        squared_sum = 0
        for num in self.vector:
            squared_sum += num ** 2
        return math.sqrt(squared_sum)  # returns the length

    def angle(self):
        """
            compute angle with dimentions of sides of the vector 
            or generalised way to find the direction
        """
        print("under development")
        return None 

    def unit(self):
        """
            unit of vector = vector * 1/vector.length
        """
        length = self.length()
        unit_vector = self.scaler_multiply(1/length)
        return unit_vector  # Unit vector

    def add(self, v):
        if len(self.vector) != len(v.vector):
            print("Length missmatch with required input")
            return None
        result_vector = []
        i = 0
        for i in range(0,len(v.vector)):
            elem1 = self.vector[i]
            elem2 = v.vector[i]
            result = elem1 + elem2
            result_vector.append(result)
        return result_vector
# TODO We can generalise the two list iterations and operations unit
    def multiply_with(self, v):
        if len(self.vector) != len(v.vector):
            print("Length missmatched")
            return None
        i = 0
        product_vector = []
        for i in range(0, len(v.vector)):
            elem1 = self.vector[i]
            elem2 = v.vector[i]
            result = elem1 * elem2
            product_vector.append(result)
        return product_vector  # Prodcut vector output

        
    def scaler_multiply(self, number):
        scalled_vector = []
        number = float(number)
        for num in self.vector:
            scalled_vector.append(num * number)
        return scalled_vector

v = [3,4]
v1 = Vector(v)

