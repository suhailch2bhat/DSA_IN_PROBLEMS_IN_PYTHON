# BASIC PROGRAM ON CLASS
# CLASS IS NOTHING BLUE PRINT
# class dog:
#    def __init__(self,name):
#        self.name=name
#    def what_is_your_name(self):
#         print("what_is_your_name",self.name)    
# tomy=dog("tomyGG")
# tomy.what_is_your_name() 
# 

#  Single inheritance:
# Python example to show the working of multiple
# inheritance
#  Multiple inheritance:
# BASIC
# class A:
#     def A(self):
#         print('This is class A.')        
# class B:
#     def B(self):
#         print('This is class B.')        
# class C(A,B):
#     def C(self):
#         print('This is class C which inherits features of both classes A and B.')
# o = C()
# o.A()
# o.B()
# o.C()
#  SOME STARDARNT EX
# class length:
#     l = 0
#     def length(self):  
#         return self.l
# class breadth:
#     b = 0
#     def breadth(self):
#         return self.b
# class rect_area(length, breadth):
#     def r_area(self):
#         print("The area of rectangle with length "+str(self.l)+" units and breadth "+ 
#               str(self.b)+" units is "+str(self.l * self.b)+" sq. units.")
# o = rect_area()
# o.l = int(input("Enter the required length for rectangle: "))
# o.b = int(input("Enter the required breadth for rectangle: "))
# o.r_area()
# Syntax of Multilevel Inheritance
# class base:
#     //member of base class
#    // functions of base class
#     Pass
# class derived1(base):
#    // members of derived1 class + base class
#   // functions of derived1 class + base class
#    pass
# class derived2(derived1):
#    // members of derived2 class + derived1 class + base class
#   // functions of derived2 class + derived1 class + base class
#    Pass
# Multilevel Inheritance Works in Python
# class Parent:
#    def __init__(self,name):
#      self.name = name
#    def getName(self):
#      return self.name
# class Child(Parent):
#    def __init__(self,name,age):
#      Parent.__init__(self,name)
#      self.age = age
#    def getAge(self):
#      return self.age
# class Grandchild(Child):
#    def __init__(self,name,age,location):
#      Child.__init__(self,name,age)
#      self.location=location
#    def getLocation(self):
#      return self.location
# gc = Grandchild("Srinivas",24,"Hyderabad")
# print(gc.getName(), gc.getAge(), gc.getLocation())
# Syntax:

# class Parent_class_Name:
    
#       #Parent_class code block

# class Child_class_Name(Parent_class_name):
     
#       #Child_class code block
# class Parent_class(object): 
       
#     # Constructor 
#     def __init__(self, name, id): 
#         self.name = name 
#         self.id = id
   
#     # To fetch employee details 
#     def Employee_Details(self): 
#         return self.id , self.name
   
#     # To check if this  is a valid employee 
#     def Employee_check(self): 
#         if self.id > 500000:
#            return " Valid Employee "
#         else:
#            return " Invalid Employee "
   
   
# # derived class or the sub class
# class Child_class(Parent_class): 
    
#     def End(self):
#         print( " END OF PROGRAM " ) 
      
# # Driver code 
# Employee1 = Parent_class( "Employee1" , 600445)  # parent class object
# print( Employee1.Employee_Details() , Employee1.Employee_check() ) 
# Employee2 = Child_class( "Employee2" , 198754) # child class object 
# print( Employee2.Employee_Details() , Employee2.Employee_check() ) 
# Employee2.End()
# Polymorphism in Python
# class Tree:
    # def tree_type(self):
    # print("There_are_many_types_of_trees.")
    # def grass(self):
    # print("Most of the grasses have no_category.")
    # class herbs(Tree):
    # def tree_type(self):
    # print("herbs are also one form of tree and plant.")
    # class root(Tree):
    # def tree_type(self):
    # print("root don’t lie in any tree category.")
# obj_tree = Tree()
# obj_gr = root()
# obj_herbs = herbs()
# obj_tree.tree_type()
# obj_gr.grass()
# obj_herbs.tree_type()
# obj_herbs.tree_type()
# obj_gr.tree_type()
# obj_herbs.grass()
# IF YOU LEARN SOME THING LEARN WEBSITE NAME{EDUCBA}