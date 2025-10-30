"""
    Matrix
    An one level abstraction of vectors Featuring vectors bundles and tranformative linear functions
    Serving transformations via defined numbers and computations
    handeling vectors combinations
"""
from Vector import *


# Required objects abstraction layer

class Matrix(list):
    """
    Matrix Abstraction on top of vector element
    Functionality 
        1. Representing transformation
        2. Abstraction of computations for solving equation
        3. Handeling fiting and equations abstractions for ML
    """

    def __init__(self, rows=None):
        m = []
        if self.shape(rows):
            for row in rows:
                v = Vector(row)
                self.append(v)
        else:
            print("Matrix cant be initiated with given input")
        

    def __str__(self):
        return "\n".join(str(row) for row in self)

    def shape(self, matrix=None):
        if matrix == None:
            matrix = self
        n = len(matrix)
        check = 1
        m = len(matrix[0])
        for row in matrix[1:]:
            if len(row) != m:
                check *= 0
        if check:
            shape = (n, m)
            return shape
        else:
            print("Matrix is not valid and contains unambeguis things")
            return None
            
            

    def scale_with(self, number):
        scalled = []
        for row in self:
            row.scale_with(number)
            scalled.append(row)
        self.clear()
        self.extend(scalled)

    def transpose(self):
        """
            Legendary DSA question is to find the transpose without making copy of matrix
            Making algorithm for making transpose of the matrix
             Making transpose with filter of having square matrix with fetching the collums of the matrix
        """
        if len(self) == len(self[0]):
            transpose = self.colums()
            return transpose
        else:
            print("It should be square matrix for transpose")

    def colums(self):
        columns = []
        # Initialize collums via doubel iteration
        iter_column = 0
        
        while iter_column < len(self[0]):
            column_element = []
            for row in self:
                column_element.append(row[iter_column])
            iter_column += 1
            columns.append(column_element)

        return Matrix(columns)
    
    def get_rank(self, info=False): # Working do give rank information with the required information
        """
        Fetching rank of the matrix is to know about
        how many collums are independent, check it via dependecy method of vectors
        Procedure ~
            + Iterate through collums
                - Set the source collum and with them their respective target column
                - check all Dependecy of other collum with the target collum

                  Fetch rank of the matrix > Make list of collum vectors and iterate to the vectros to see dependency
        """
        columns = self.colums()
        rank = 1
        dependecy_map = {}

        col1 = columns[0] # Making dependency check with one
        independent = 1

        dependent_rows = []

        for col2 in columns:
            if not(col1.equal_to(col2)):
                d = col1.dependecy_with(col2, option=2)
                print(f"dependency : {d}")
                if d != 0:
                    print(f"goes with this option")
                    independent *= 0
                    info = (d, col2)
                    print(f"information : {info}")
                    dependent_rows.append(info)

            if independent == 0:
                rank += 1
        
        if info:
            return rank, dependent_rows
        else:
            return rank

# Making Linear Algebra basic tools

def solve_matrix(matrix, target_vector):
    """
        Solving Matrix with respect to the target vector, 
        make Augmented matrix and solve it via reducing it to row echelion form,
        And then map the finding

        Procedure
            1. Make augmented matrix
            2. Find leader row
            3. reduce other rows via row operations
    """
    augmented_matrix = []
    for row, element in zip(matrix, target_vector):
        augment_row = list(row)
        augment_row.append(element) # making augmented matrix

        augment_row = Vector(augment_row)
        augmented_matrix.append(augment_row)

    print(f"Augmented matrix to solve : {augmented_matrix}")

    # Searching for leader row out of the matrix
    

    



l = [[1, 3, 9] , [1, 6, 9], [1, 9, 9]]

m = Matrix(l)
print(f"Rank of the matrix : {m.get_rank(info=True)} ")


