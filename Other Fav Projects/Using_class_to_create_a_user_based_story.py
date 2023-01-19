class story:
    def __init__(self):
        self.b1=self.b1="1._____"
        self.b2=self.b2="2._____"
        self.b3=self.b3="3._____"
        self.b4=self.b4="4._____"
        self.b5=self.b5="5._____"
        self.b6=self.b6="6._____"
        self.b7=self.b7="7._____"
        self.b8=self.b8="8._____"
        self.b9=self.b9="9._____"
    
    def BlankStory(self):
        # print(f"""Once upon a {self.b1} there {self.b2} so {self.b3} and {self.b4}.\nThis {self.b5} was heard by {self.b6} and {self.b7} so {self.b8} did {self.b9}.""")
        return f"Once upon a {self.b1} there {self.b2} so {self.b3} {self.b4}.\nThis {self.b5} was heard by {self.b6} and {self.b7} so {self.b8} did {self.b9}."
    
    def UserWroteStory(self,b1,b2,b3,b4,b5,b6,b7,b8,b9):
        print(f"Once upon a {b1} there {b2} so {b3} {b4}.\nThis {b5} was heard by {b6} and {b7} so {b8} did {b9}.")

blanklist=["","","","","","","","",""]
    
s1=story()
print(s1.BlankStory())
for i in range(len(blanklist)):
    print(f"Blank {i+1}: ")
    blanklist[i]=input()

s1.UserWroteStory(blanklist[0],blanklist[1],blanklist[2],blanklist[3],blanklist[4],blanklist[5],blanklist[6],blanklist[7],blanklist[8])