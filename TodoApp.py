from abc import ABC,abstractmethod
class InputError(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message

class TodoApp():
    def __init__(self,name,email):
        self.name = name
        self.email = email

    @abstractmethod
    def __AddTodo(self,title,date,isDone=False):
        pass
    
    @abstractmethod
    def __updateTodo(self,id,key,value):
        pass
    
    @abstractmethod
    def __deleteTodo(self,id):
        pass
    
    @abstractmethod
    def __viewTodos(self):
        pass
    @abstractmethod
    def __CreateCategory(self,name):
        pass

class MyTodoApp(TodoApp):
    
    def __init__(self,name,email):
        super().__init__(name,email)
        self.initialTodos = [
            {
            "id" : 101,
            "title" : 'Computer Network final exam',
            "date" : '22-12-2024',
            "category": 'Exam',
            "isDone" : False

            },
             {
            "id" : 102,
            "title" : 'Object Oriented Programming 2',
            "date" : '24-12-2024',
            "category": 'Exam',
            "isDone" : False

            },
            {
            "id" : 103,
            "title" : 'Computer Architecture and Organization',
            "date" : '28-12-2024',
            "category": 'Exam',
            "isDone" : False

            },

        ]
        self.initialCategories = ['Exam','Quiz','Report submission']
        self.idTop = 104
        self.Todos = []
        self.categories = []
        self.Todos.extend(self.initialTodos)
        self.categories.extend(self.initialCategories)
    def welcomeUI(self):
        print(f'-^-Welcome Mr.${self.name} to your todo list-^-')
        print('What do you want to do?')
        print("1. Add Todo")
        print("2. View Todo")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Categories")
        print("0. Exit")

    def __AddTodo(self,title,date,category,isDone=False):
        # super().__init__(self.title,self.date,self.isDone,self.todoId)
        todo = {
            "id" : self.idTop,
            "title" : title,
            "date" : date,
            "category": category,
            "isDone" : isDone
        }
        self.Todos.append(todo)
        self.idTop += 1
    def __updateTodo(self,id, key, value):
        for todo in self.Todos:
            if todo["id"] == id:
                todo["key"] = value
    def __deleteTodo(self,id):
        for todo in self.Todos:
            if todo["id"] == id:
                self.Todos.remove(todo)
                return 1
        return 0   
    def __viewTodo(self,todo):
        for key,value in todo.items():
            print(f"{key.capitalize()} : {value}")
            print("---------------------")
    def find_todo(self,id):
        for todo in self.Todos:
            if(todo['id'] == id):
                return todo
            return None
    def find_category(self,category):
        if category in self.categories: 
            return category
        return None
    def __CreateCategory(self, name):
        if(self.find_category(name) is None):
            self.categories.append(name)
            print("Category added successfully!!")
            return
        print("Category alredy exists or other error occurs")
    def __findCategoryTodos(self,categoryName):
        CategoryTodos = []
        for todo in self.Todos:
            if(todo['category'] == categoryName):
                CategoryTodos.append(todo)
        return CategoryTodos
    def Actions(self):
        while(True):
            self.welcomeUI()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1 :
                    title = input("Enter Todo Title: ")
                    date = input("Enter Due Date: ")
                    category = input("Enter category: ")
                    if self.find_category(category) is None:
                        print(category ,"Does not exits! ")
                        userChoice = input("wanna create this category (Y/N)?: ")
                        if(userChoice == 'y' or userChoice == 'Y'):
                            self.__CreateCategory(category)
                        else:
                            continue
                    self.__AddTodo(title,date,category,False)
                elif choice == 2:
                    if (len(self.Todos) <= 0):
                        print("No Todo exists!! ")
                        continue
                    for todo in self.Todos:

                        self.__viewTodo(todo)
                        print("=********************=\n")
                elif choice == 3:
                    id = int(input("Enter id of the todo :"))
                    todo = self.find_todo(id)
                    if todo is None:
                        raise InputError("Todo not found!!")
                    print("-----------------")
                    print ("Current Todo title:", todo['title'])
                    print ("Due date:", todo['date'])
                    print("Category: ",todo['category'])
                    print("-----------------")

                    print("1. Update title")
                    print("2. Update date")
                    print("3. Mark as done")
                    print("4. Exit")
                    choice = input("Enter your choice: ")
                    if(choice ==1 ):
                        print ("Current Todo title:", todo['title'])
                        print("Enter new title")

                        title = input("title")
                        self.__updateTodo(id,"title",title)
                    if(choice == 2):
                        print ("Current Due date:", todo['date'])
                        date = input('Enter new due date (dd-mm-yy) : ')
                        self.__updateTodo(id,'date',date)
                    if(choice == 3):
                        print("Is Done? : ",todo['isDone'])
                        status =  input("Are you sure ? want to mark it as done (Y/N)? : ") == 'y'
                        if(status == 'Y' or status == 'y'):
                            self.__updateTodo(id,'isDone',status)
                        print('exiting......')
                    else:
                        continue
                    
                elif choice == 4:
                    id = int(input("Enter id of the todo: "))

                    returned = self.__deleteTodo(id)
                    if(returned):
                       print("Todo deletion successfull")
                    else:
                       print("Something went wrong! todo not found!! ")
                elif choice == 5:
                    print("Select your operation ")
                    print("1. Add Category")
                    print("2. View Category")
                    print("3. view todos in category wise")
                    categoryChoice = int(input("enter your choice: "))
                    if(categoryChoice == 1):
                        newCategory = input('Enter category name: ')
                        if self.find_category(newCategory) :
                            raise InputError("Catrgory already exits and can't be duplicated")
                        self.__CreateCategory(newCategory)
                    elif (categoryChoice == 2):
                        print('=======================')
                        print("-^- All categories -^-")
                        for category in self.categories:
                            print(category)
                        print("===================")
                    elif (categoryChoice == 3):
                        for category in self.categories:
                            todos = self.__findCategoryTodos(category)
                            print('=================')
                            print('',category)
                            print('=============')
                            if todos :
                                for todo in todos:
                                    self.__viewTodo(todo)
                                    print("***************")
                            else:
                                print('No todos in this category')
                    else:
                        raise InputError("Invalid input")
                elif choice == 0:
                    print("closing the app.......")
                    break
                else:
                    raise InputError("Invalid Input")
            except Exception:
                print("Invalid Choice")
                continue
Enamul = MyTodoApp("Enamul","H@hdf")
Enamul.Actions()

