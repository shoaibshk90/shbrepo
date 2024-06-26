"""         PROJECT ON ATM              """
# name = "shoaib"
# password = "1234"
# user_name = input("enter a name")
# user_password = input("enter a password")

# s = """
# 1.credit card
# 2.debit card
# 3.mini statement
# 4.exit
# """
# amount = 2000
# if name == user_name and password == user_password:
#           while True:
#                     print(s)
#                     option = int(input("enter a option"))
#                     if option==1:
#                            credit_amount = float(input("enter a amount"))
#                            print("amount after credit",amount+credit_amount)
#                     elif option==2:
#                               debit_amount = float(input("enter the amount"))
#                               print("amount after debit",amount-debit_amount)
#                     elif option==3:
#                               print("mini statement",amount)
#                     elif option==4:
#                               break
# else:
#           print("incorrect")



"""  project on supermarket bill generation """

# from datetime import datetime

# name = input("enter your name")

# # list of items

# lists = '''
# Rice    Rs 20/kg
# Sugar   Rs 30/kg
# Salt    Rs 20
# Oil     Rs 80/liter
# Paneer  Rs 110/kg
# Maggi   Rs 50
# Boost   Rs 90
# Colgate Rs 85
# '''
# # decleration

# price = 0
# pricelist = []
# totalprice = 0
# finalprice = 0
# ilist = []
# qlist = []
# plist = []

# #rates for items

# items = {'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,
# 'maggi':50,
# 'boost':90,
# 'colgate':85}
# option = int(input("for list of items press 1 :"))
# if option == 1:
#           print(lists)
# for i in range(len(items)):
#           inp1 = int(input("if you want to buy press 1 or 2 for exit:"))
#           if inp1 == 2:
#                     break
#           if inp1 == 1:
#                     item=input("Enter your items")
#                     quantity=int(input("Enter a quantity:"))
#                     if item in items.keys():
#                               price=quantity*(items[item])
#                               pricelist.append((item,quantity,items,price))
#                               totalprice+=price
#                               ilist.append(item)
#                               qlist.append(quantity)
#                               plist.append(price)
#                               gst=(totalprice*5)/100
#                               finalamount = gst+totalprice
#                     else:
#                               print("sorry you entered items is not available")
#           else:
#                     print("you entered wrong number")
#           inp=input("can i bill the items yes or no:")
#           if inp=='yes':
#                     pass
#                     if finalamount!=0:
#                               print(25*"=","shoaib supermarket",25*"=")
#                               print(28*" ","ravindranagar")
#                               print("name:",name,30*" ","date:",datetime.now())
#                               print(75*"-")
#                               print("sno",8*' ','items',8*" ",'qunatity',3*" ",'price',)
#                               for i in range(len(pricelist)):
#                                         print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
#                               print(75*"-")
#                               print(50*" ",'TotalAmount','Rs',totalprice)
#                               print("gst amount",40*" ",'Rs',gst)
#                               print(75*"-")
#                               print(50*" ","finalamount",'Rs',finalamount)
#                               print(75*"-")
#                               print(20*" ","thanks for visiting")
#                               print(75*"-")

                              

                    


