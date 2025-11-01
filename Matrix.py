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

        BUG Making moduler rank finding system , dependency parsing mechanism is being broken now 0_o
        """
        columns = self.colums()
        rank = 1
        dependecy_map = {}

        col1 = columns[0] # Error fixed
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

def dependency_parsing(colum, columns):
    """
    input : Vector list as columns
    output : Dependency count
    """
    c = 0
    for t in columns:
        print(f"Dependency parsing working for {t} and {colum} for fetching multiplicatioin relation")
        d = colum.dependecy_with(t,option=2) # fetching multiplication dpendency
        print(f"We have fetched the dependency number with above inputs to get {d}")
        if d != 0:
            c += 1  # BUG Dependency parsing should be limmited with just integers based maping it goes to fraction and ruins the dependency matrix computation 
    # result intuation : How much times out colum is the columns
    return c 

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
    for row, element in zip(matrix, target_vector): # BUG making iteration error
        augment_row = list(row)
        augment_row.append(element) # making augmented matrix

        augment_row = Vector(augment_row)
        augmented_matrix.append(augment_row)

    print(f"Augmented matrix to solve : {augmented_matrix}") # Working * * 

    """
        Making Reduced Row echelion form via one depth rule of geting pivots
        reducing other rows based on multiplication based depndency to get leading 1 row for every row,
        Making reduction and noting steps,
        
        Procedure
        finding leader row -> Parse all rows via dependency parsing for the dependency number and fetch the highest for leader
    """
    
    # finding leader row with most dependency
    dependency_map = {}
    m = 0
    for row in augmented_matrix:
        d = dependency_parsing(row, augmented_matrix) # Getting number of dependency 
        print(f"Dependency parsing output for the row : {row} results {d}")
        dependency_map[str(row)] = d 
        if d > m:
            m = d 
    # Got max with leader row 
    if m == 0:
        print("Either testing matrix dont make sence for geting dependency thing")
        return None 
    else:
        # fetching respective row
        key = [k for k, v in dependency_map.items() if v == m] # fetching respective key via dictionary
        print(f"Leader row : {list(key)}")

    

    



l = [[1, 1, 1] , [2, 2, 2], [3, 3, 3]]

m = Matrix(l)
x = Vector([1, 2, 3])

print("Testing solve matrix")
solve_matrix(m, x)



