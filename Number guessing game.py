#Number guesssing game:

from math import log2
import random
low=int(input("Enter your lower range: "))
high=int(input("Enter your high range: "))
ran_Num=random.randint(low,high)
Total_Gue=1
condition=True

while(condition):
 Min_No_of_Guessing= log2(high-low+ 1)   
 gue_Num=int(input("Enter your guessing number: "))   
 if gue_Num>ran_Num:
    print("Try Again!! You guessed too high")
 elif gue_Num<ran_Num:
    print("Try Again!! You guessed too low")
 else:
    print("Congratulation!! You find it at {}th attempts!!".format(Total_Gue))
    condition=False
 if Min_No_of_Guessing==Total_Gue:
    condition=False 
 Total_Gue=Total_Gue+1
 
if ran_Num!=gue_Num:
    print("Better luck next time!!")
 

            
    
     
    
    
    
