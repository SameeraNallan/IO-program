while True:
    class clerk:
        
       
        def __init__(self):
            self.id=int(input('Enter the ID: '))
            self.name=input('Enter the Name: ')
            self.age=int(input('Enter the Age: '))
            self.salary=int(input('Enter the Salary: '))
            self.desig='Clerk'

        def display(self):            
                print('***********************')
                print('ID:',self.id)
                print('Name:',self.name)
                print('Age:',self.age)
                print('Salary:',self.salary)
                print('Designation:',self.desig)
                print('***********************')                
                
        def risesalary(self):
            sal=self.salary
            nsal=sal+(sal*0.05)
            print('The raised salary is:',nsal)


    class manager:        
       
        def __init__(self):
            self.id=int(input('Enter the ID: '))
            self.name=input('Enter the Name: ')
            self.age=int(input('Enter the Age: '))
            self.salary=int(input('Enter the Salary: '))
            self.desig='Manager'
            
        def display(self):
            
                print('***********************')
                print('ID:',self.id)
                print('Name:',self.name)
                print('Age:',self.age)
                print('Salary:',self.salary)
                print('Designation:',self.desig)
                print('***********************')
            
        def risesalary(self):
            sal=self.salary
            nsal=sal+(sal*0.2)
            print('The raised salary is:',nsal)


    class tester:
        
        def __init__(self):
            
            self.id=int(input('Enter the ID: '))
            self.name=input('Enter the Name: ')
            self.age=int(input('Enter the Age: '))
            self.salary=int(input('Enter the Salary: '))
            self.desig='Tester'
            
        def display(self):
           
                print('***********************')
                print('ID:',self.id)
                print('Name:',self.name)
                print('Age:',self.age)
                print('Salary:',self.salary)
                print('Designation:',self.desig)
                print('***********************')
                
        def risesalary(self):
            
            sal=self.salary
            nsal=sal+(sal*0.1)
            print('The raised salary is:',nsal)


    class developer:
      
        def __init__(self):
            
            self.id=int(input('Enter the ID: '))
            self.name=input('Enter the Name: ')
            self.age=int(input('Enter the Age: '))
            self.salary=int(input('Enter the Salary: '))
            self.desig='Developer'
            
        def display(self):
            
                print('***********************')
                print('ID:',self.id)
                print('Name:',self.name)
                print('Age:',self.age)
                print('Salary:',self.salary)
                print('Designation:',self.desig)
                print('***********************')
                            
        def risesalary(self):
            sal=self.salary
            nsal=sal+(sal*0.15)
            print('The raised salary is:',nsal)   
    
    
    print('Choose the options:\n 1.Create \n 2.Display \n 3. Rise Salary \n 4. Exit')
          
    opt=int(input('Enter the option:'))
    if opt==1:
        print('1. Clerk')
        print('2. Manager')
        print('3. Tester')
        print('4. Developer')
        n=int(input('Enter the option:'))
        if n==1:
            
            c=clerk()
            continue
        
        elif n==2:
            m=manager()
            continue
        
        elif n==3:
            t=tester()
            continue
            
        elif n==4:
            d=developer()
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
            
            c.display()
            continue
        
        elif n==2:
            m.display()
            continue
        
        elif n==3:
            t.display()
            continue
            
        elif n==4:
            d.display()
            continue
            
        else:
            print('Wrong option')
        continue
        

    elif opt==3:
        print('1. Clerk')
        print('2. Manager')
        print('3. Tester')
        print('4. Developer')
        n=int(input('Enter the option:'))
        if n==1:
            
            c.risesalary()
            continue
        
        elif n==2:
            m.risesalary()
            continue
        
        elif n==3:
            t.risesalary()
            continue
            
        elif n==4:
            d.risesalary()
            continue
            
        else:
            print('Wrong option')
        continue  
               

    elif opt==4:
        print('ThankYou...........')
        break

    else:
        print('Wrong option')
        




































    
        











    
    

    
