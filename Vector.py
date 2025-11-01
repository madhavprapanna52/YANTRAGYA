"""
    Making Vector Encapsulation for Project

    Vector properties
    1. Basic vector computations and fundamental operations
    2. Making basic fundamental abstractions of the vector object

    --- 
    
"""
import math


class Vector(list):
    '''
        Object discriptions and methods overview and planning
        Properties
            1. Information stored -> numbers

        Functions
            1. Fetch information about vector
            2. Change the vectors condition
            3. Construct a new vector
                - copy, new creation , automatic, from existing
            4. Basic fundamental operations on vector based on them
    '''
    def __init__(self, numbers=None):
        if numbers:
            # Making elements float before adding
            for e in numbers:
                if type(e) == int:
                    e = float(e)
                    self.append(e)
                elif type(e) == float:
                    self.append(e)
                else:
                    print("Vectors of numbers are only supported")

    def equal_to(self, v):
        i = 0
        check = 1
        if len(v) == len(self):
            for num in self:
                if num != v[i]:
                    check *= 0
                i += 1
            if check == 1:
                return True
            else:
                return False

    def scale_with(self, number):
        scalled = []
        for element in self:
            scalled_element = number * element 
            scalled.append(scalled_element)
        print(scalled)
        self.clear() # Clear the existing
        self.extend(scalled)

    def inner_product(self, vector, type="Standard"):
        '''
            Chain inner products with other operations for real beauty of flexibility with different set of products rule with spaces respecitves
        '''
        if (len(vector) == len(self)) and (type(vector) == Vector):
            i = 0
            product_output = []

            for e in self:
                p = float(vector[i] * e)
                product_output.append(p)
                i += 1
            return Vector(product_output)
        else:
            print("Either you messed with length or its not vector -_-")
            return None
    
    def dependecy_with(self, vector, option=1):  # Dependency check are working fine
        '''
        Tested working dependency checking logic *U*


        Make dependecy analysis at vector level for ease in row echelion form reduction operations further
        Functions discriptions and scope
            > Making dependecy validations for other operations of projects function
            > Making Vector based map output if required
            > additive dependency 
            > multiplicative dependency of the vectors

        Dependency parsing part
        Additive dependency
            ~ Which number can map via addition the given number 
                -> Compute the equation for the following respective we have n equatioins with one unknown ,
                if difference of all of the numbers are same then they have one addition dependency other then they dont ^-^

        '''
        print(f"input set : {vector} and {self}")
        dependency = 1
        # Cases require optimisation as  same flow is repeated over all of the checks
        match option:
            case 1:  # Also checks for the subtractioin of the number
                check = int(vector[0]) - int(self[0])

                for x1,x2 in zip(self[1:],vector[1:]):
                    if float(x2 - x1) != check:
                        dependency *= 0

                if dependency == 0:
                    return 0
                else:
                    return check

            case 2:
                check = int(vector[0] / self[0]) # Fixed whole set of errrors out of float based dependency

                for x1, x2 in zip(self[1:], vector[1:]):
                    if (x2 / x1) != check:
                        dependency *= 0
                if dependency == 0:
                    return 0
                else:
                    print(f"Dependency with multiplication {check}")
                    return check  # Multiplication dependency



