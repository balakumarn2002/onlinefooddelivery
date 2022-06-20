print("Online food  Order")
restaurant=["1.NBK \n2.MS \n"]
OnlinePay=["1.GPay\n2.Phonpe"]
drink=["1.Juice\n2.Coffe\n3.Tea"]
pay=["1.Online\n2.Offline"]
i=["1.Veg\n2.Non-Veg\n3.drinks"]
Vegt=["1.Lemon rice\n2.Tomato rice\n3.Idli\n4.Dhosai\n5.Appam\n6.Rava-Upma\n7.Mushroom Briyani\n8.Coconut Rice\n9.Vada Curry"]
nonveg=["1.Chicken Briyani\n2.Chicken 65\n3.Mutton Briyani\n4.Fish dhish\n5.Butter Chicken\n6.Malabar Fish Briyani\n7.Thandoori Lamb chops\n8.Mutton Korma"]
way=["1.Home Delivery\n2.Take Away"]
print(*restaurant,sep='\n\t')
r=str(input("Select ur restaurant :"))
Cost=0
t=0
z=0
if r=="NBK":
    print("NBK restaurant is chosen")
elif r=="MS":
    print("MS restaurant is chosen") 
name=str(input("Enter ur Name      :"))
date=str(input("Enter Date         :"))
email=str(input("Enter Email id    :"))
contact=int(input("Enter Mobile no :"))
def veg():
    print(*Vegt,sep='\n\t')
    V=int(input("Enter ur item           :"))
    n=int(input("Enter no of item u want :"))
    if V==1:
         print(" ur item is Lemon rice")
         Cost=n*70
         return Cost
    elif V==2:
          print("ur item is Tomato rice")
          Cost=n*80
          return Cost
    elif V==3:
          print("ur item is Idli")
          Cost=n*15
          return Cost
    elif V==4:
          print("ur item is Dhosai")
          Cost=n*20
          return Cost
    elif V==5:
          print("ur item is Appam")
          Cost=n*35
          return Cost 
    elif V==6:
          print("ur item is Rava-Upma")
          Cost=n*45
          return Cost
    elif V==7:
          print("ur item is Mushroom Briyani")
          Cost=n*90
          return Cost8
    elif V==8:
          print("ur item is Coconut rice")
          Cost=n*50
          return Cost
    elif V==9:
          print("ur item is Vada-Curry")
          Cost=n*50
          return Cost
def Nonveg():
    print(*nonveg,sep='\n\t')
    non=int(input("Enter ur item   :"))
    no=int(input("Enter no of item :"))
    if non==1:
      print(" ur non-veg is  Chicken briyani")
      Cost=no*80
      return Cost
    elif non==2:
        print("ur non veg is Chicken 65")
        Cost=no*90
        return Cost
    elif non==3: 
         print("ur non-veg is Mutton Briyani")
         Cost=no*100
         return Cost
    elif non==4: 
         print("ur non-veg is  Fish dhish ")
         Cost=no*100
         return Cost
    elif non==5: 
         print("ur non-veg is  Butter Chicken")
         Cost=no*100
         return Cost
    elif non==6: 
         print("ur non-veg is  Malabar Fish Briyani  ")
         Cost=no*100
         return Cost
    elif non==7: 
         print("ur non-veg is Thandoori Lamb chops ")
         Cost=no*100
         return Cost
    elif non==8: 
         print("ur non-veg is Mutton Korma")
         Cost=no*100
         return Cost
def drinks():
    print(*drink,sep='\n\t')
    d=int(input("Enter drinks item  u want :"))
    b=int(input("Enter no of items         :"))
    if d==1:
        print(" ur item is juice")
        Cost=b*15
        return Cost
    elif d==2:
        print("ur item is coffee")
        Cost=b*10 
        return Cost
    elif d==3: 
        print("ur item is Tea")
        Cost=b*8
        return Cost
while True: 
    print(*i,sep='\n\t')
    choice=int(input("Enter ur choice:"))
    if choice==1:
       z=veg()
       print(z)
    elif choice==2:
       z= Nonveg()
       print(z)
    elif choice==3:
       z=drinks()
       print(z)
    c=str(input("If u want one more item:(Yes or No) "))
    if c=="Yes":
        t=t + z 
        print("Amount:",t)
        continue
    else: 
        t=t + z 
        print("Total Amount:",t)
        break
Address=str(input("Enter ur Address:"))
State=str(input("Enter ur State    :"))
pin=int(input("Enter ur pin Code   :"))
print(*way,sep='\n\t')
w=int(input("Select the way        :"))
if w==1:
   d=50
   total=t+d
   print(*pay,sep='\n\t')
   PayDelivery_method = int(input("\n\tSELECT YOUR PAYMENT METHOD : "))            
   if PayDelivery_method == 1:
              print("\n\t--------Online Payment-------")
              print("\t Delivery Charge:",d)
              print(*OnlinePay,sep='\n\t')
              Pay_Online_Payment=int(input("Choose the payment way: "))
              if Pay_Online_Payment == 1:
                  D=int(input("Enter the your UPI Pin: "))
                  otp=int(input("Enter OTP"))
                  print("\n\tPAYMENT PROCESSING..........")
                  print("\n\tPAYMENT IS DONE..")
                  print("\n\tTotal Price:Rs.",t)
                  print("\n\tRECEIPT:")
                  print("\n\tA/C XXXX5567 linked to card")
                  print("\n\tXXXX3455 debited Rs",total) 
                  print("\n\tAvl Bal : 6,565") 
              elif Pay_Online_Payment == 2 :
                     UPI=int(input("Enter the your UPI Pin: "))
                     otp=int(input("Enter OTP"))
                     print("\n\tPAYMENT PROCESSING................")
                     print("\n\tPAYMENT IS DONE..")
                     print("\n\tTotal Price:Rs.",t)
                     print("\n\tRECEIPT:")
                     print("\n\tA/C XXXX5567 linked to card")
                     print("\n\tXXXX3455 debited Rs",total) 
                     print("\n\tAvl Bal : 6,565") 
   else: 
           print("\n\tCASH DELIVERY / TO PAY ")
           print("\n\tDELIVERY CHARGE: ",d)
           print("\n\tTotal Price:Rs.",total)
           print("Amount has been recieved Successfully")
elif w==2:
   print(*pay,sep='\n\t')
   PayDelivery_method = int(input("\n\tSELECT YOUR PAYMENT METHOD : "))            
   if PayDelivery_method == 1:
              total=t
              print(*OnlinePay,sep='\n\t')
              Pay_Online_Payment=int(input("Choose the payment way: "))
              if Pay_Online_Payment == 1:
                  print("\n\t GPay")
                  PIN=int(input("Enter Pin: "))
                  print("OTP has been Successfully sent")
                  otp=int(input("Enter ur OTP:"))
                  print("\n\tPAYMENT PROCESSING................")
                  print("\n\tPAYMENT IS DONE...")
                  print("\n\tRECEIPT:")
                  print("From ",r,"Restaraunt U Have Purchased items")
                  print("\n\tA/C XXXX5567 linked to card")
                  print("\n\tXXXX3455 debited Rs",total) 
                  print("\n\tAvl Bal : 6,565") 
              elif Pay_Online_Payment == 2 :
                   print("\n\t PhonePay ")
                   UPI=int(input("Enter Pin: "))
                   print("OTP has been Successfully sent")
                   otp=int(input("Enter OTP   :")) 
                   print("\n\tPAYMENT PROCESSING...........")
                   print("\n\tPAYMENT IS DONE..")
                   print("\n\tRECEIPT:")
                   print("\n\tA/C XXXX4567 linked to card")
                   print("\n\tXXXX4533 debited Rs",total) 
                   print("\n\tAvl Bal : 4,565") 
   else: 
           print("\n\tTO PAY ")
           print("\n\tTotal Price:Rs.",total)
           print("Amount has been recieved Successfully")


print("Hi",name)
print("Thanks for Ordering from ",r,"Restaraunt")
print("Your Food Delivery has been Confirmed and")
print("Should be ready within 25 min.We will let")
print("U know when it is on its way to you")
