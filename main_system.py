class Food:
    items=[]
    def add_food(self):
        self.fid=int(input('Enter the FoodID : '))
        self.fname=input('Enter the FoodName : ').lower()      
        self.ftype=input('Enter the FoodType(Veg/Non-Veg) : ').lower()
        self.fprice=int(input('Enter the food price : '))
        Food.items.append([self.fid,self.fname,self.ftype,self.fprice])     
        

    def __del__(self):
        for i in Food.items:
            if i[0]==self.fid:
                Food.items.remove(i)
        
    @classmethod   
    def update_food(cls):
        n=int(input('Enter the FoodID to be updated : '))
        for i in cls.items:
            if i[0]==n:
                i[1]=input(f'Enter the FoodName  (previous FoodName : {i[1]}) : ')
                i[2]=input(f'Enter the FoodType(Veg/Non-Veg) (previous FoodType : {i[2]}) : ')
                i[3]=int(input(f'Enter the food price  (previous Food price: {i[3]}) : '))
                print('Food item updated.')
        else:
            print('Invalid FoodId')
        
                   
    @classmethod
    def show_food_list(cls):
        print(cls.items)
        
    @classmethod
    def show_food_list_by_Id(cls,Id):
        for i in cls.items:
            if i[0]==Id:
                print(i)
                
    @classmethod
    def show_food_list_by_Name(cls,Name):
        for i in cls.items:
            if i[1]==Name.lower():
                print(i)
                
    @classmethod
    def show_food_list_by_Type(cls,Type):
        for i in cls.items:
            if i[2]==Type.lower():
                print(i)
                
                
    @classmethod
    def sort_food_list_by_name(cls):
        l1=[]
        l1=cls.items+l1
        l1.sort(key=lambda x:x[1])
        print(l1)
        
    @classmethod
    def sort_food_list_by_price(cls):
        l1=[]
        l1=cls.items+l1
        l1.sort(key=lambda x:x[3])
        print(l1)
    
