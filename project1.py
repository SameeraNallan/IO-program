import os
class clerk:
        
       
    def create(self):
        
        clerk=open("clerk.txt","x")
        c=open("clerk.txt","a")
        self.id=input('Enter the ID: ')
        self.name=input('Enter the Name: ')
        self.age=input('Enter the Age: ')
        self.salary=input('Enter the Salary: ')
        self.desig='Clerk'
        c.write(self.id)
        c.write(self.name)
        c.write(self.age)
        c.write(self.salary)
        c.write(self.desig)
        c.close()

    def display(self):            
                print('***********Clerk************')
                cl=open("clerk.txt",'r')
                print(cl.read())
                print('***********************')                
                
        

class manager:        
       
    def create(self):
        
        
        
        manager=open("manager.txt","x")
        m=open("manager.txt","a")
        self.id=input('Enter the ID: ')
        self.name=input('Enter the Name: ')
        self.age=input('Enter the Age: ')
        self.salary=input('Enter the Salary: ')
        self.desig='Manager'
        m.write(self.id)
        m.write(self.name)
        m.write(self.age)
        m.write(self.salary)
        m.write(self.desig)
        m.close()
            
    def display(self):
            
                print('*********Manager**************')
                ma=open("manager.txt",'r')
                print(ma.read())
                print('***********************')
            
       
class tester:
        
    def create(self):         
                
        tester=open("tester.txt","x")
        t=open("tester.txt","a")
        self.id=input('Enter the ID: ')
        self.name=input('Enter the Name: ')
        self.age=input('Enter the Age: ')
        self.salary=input('Enter the Salary: ')
        self.desig='Tester'
        t.write(self.id)
        t.write(self.name)
        t.write(self.age)
        t.write(self.salary)
        t.write(self.desig)
        t.close()
        
    def display(self):
           
                print('***********Tester************')
                te=open("tester.txt",'r')
                print(te.read())
                print('***********************')
                
       

class developer:
      
    def create(self):
            
        
        
        developer=open("developer.txt","x")
        d=open("developer.txt","a")
        self.id=input('Enter the ID: ')
        self.name=input('Enter the Name: ')
        self.age=input('Enter the Age: ')
        self.salary=input('Enter the Salary: ')
        self.desig='Developer'
        d.write(self.id)
        d.write(self.name)
        d.write(self.age)
        d.write(self.salary)
        d.write(self.desig)
        d.close()
    def display(self):
            
                print('**********Developer*************')
                de=open("developer.txt",'r')
                print(de.read())
                print('***********************')

T=tester()
D=developer()
M=manager()
C=clerk()


       
while True:
        
    print('Choose the options:\n 1.Create \n 2.Display \n 3. Exit')
          
    opt=int(input('Enter the option: '))
    if opt==1:
        print('1. Clerk')
        print('2. Manager')
        print('3. Tester')
        print('4. Developer')
        n=int(input('Enter the option: '))
        if n==1:
           if os.path.exists("clerk.txt"):
               print('Clerk data already exists');
               continue
           else:
                C.create()
                continue
        elif n==2:
            if os.path.exists("manager.txt"):
               print('Manager data already exists');
               continue
            else:
                M.create()
                continue
        elif n==3:
            if os.path.exists("tester.txt"):
               print('Tester data already exists');
               continue
            else:
                T.create()
                continue
        elif n==4:
            if os.path.exists("developer.txt"):
               print('Developer data already exists');
               continue
            else:
                D.create()
                continue
        else:
            print('Wrong option')
        continue

    elif opt==2:
        
        print('1. Clerk')
        print('2. Manager')
        print('3. Tester')
        print('4. Developer')
        n=int(input('Enter the option:'))
        if n==1:
            if os.path.exists("clerk.txt"):
                
                C.display()
                continue
            else:
                C.create()
                C.display()
                continue
        
        elif n==2:
           if os.path.exists("manager.txt"):
               M.display()
               continue
           else:
                M.create()
                M.display()
                continue
        elif n==3:
            if os.path.exists("tester.txt"):
               T.display()
               continue
            else:
                T.create()
                T.display()
                continue
        elif n==4:
            if os.path.exists("developer.txt"):
               D.display()
               continue
            else:
                D.create
                D.display()
                continue
        else:
            print('Wrong option')
        continue
        

    
            
       
    elif opt==3:
        print('ThankYou...........')
        break

    else:
        print('Wrong option')
        




































    
        











    
    

    
