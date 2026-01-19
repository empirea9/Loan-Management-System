import csv 
import os

#NO RECORDS CHECK FUNCTION - TO CHECK IF THE CSV FILE IS EMPTY
def no_records_check():
     f=open("loan.csv","r",newline='') 
     acct=csv.reader(f) 
     c=0
     for i in acct: 
          if i!=["CUSTOMER ID","NAME","LOAN AMOUNT", "LOAN TIME", "INTEREST"]:
               c=1
               break
     f.close()

     #FOR EMPTY FILE
     if c==0:
          print("No records found. Please add customer records first.")
          print('----------------------------------------------------------------------')
          return True
     
     #FOR NON-EMPTY FILE
     else:
          return False

#HEADING FUNCTION - TO WRITE THE FIELDNAMES TO THE CSV FILE
def heading():

     #ERROR HANDLING - TO CHECK IF THE CSV FILE EXISTS AND IS NOT EMPTY
     if not os.path.exists("loan.csv") or os.path.getsize("loan.csv") != 0:
          return
     if no_records_check()==True:
          return
     
     #TO CREATE THE CSV FILE AND ADD FIELDNAMES
     f=open("loan.csv","w+", newline='')
     w=csv.writer(f)
     l=["CUSTOMER ID","NAME","LOAN AMOUNT", "LOAN TIME", "INTEREST"]
     w.writerow(l) 
     f.close() 

#ERROR HANDLING FUNCTION - TO CHECK IF A VALUE IS FLOAT
def is_float(value):
     try:
          float(value)
          return True
     except ValueError:
          return False
     
#ERROR HANDLING FUNCTION - 
def wrong_input():
     print("INVALID INPUT(S), PLEASE TRY AGAIN")
     print('----------------------------------------------------------------------')
     wp=(input("Press Enter to Continue:"))
     print('----------------------------------------------------------------------')
     return

#DATA INPUT FUNCTION - TO INPUT DATA AND WRITE IT TO THE CSV FILE
def data():
     f=open("loan.csv","a",newline='')
     w=csv.writer(f)
     n=(input("Enter number of customers: "))
     print('----------------------------------------------------------------------')

     #ERROR HANDLING - TO CHECK IF THE INPUT IS A DIGIT
     if n.isdigit()==False:
          print("INVALID NO. OF CUSTOMERS, PLEASE TRY AGAIN")
          print('----------------------------------------------------------------------')
          wp=(input("Press Enter to Continue:"))
          print('----------------------------------------------------------------------')
          f.close()
          return
     
     #DATA INPUT OPERATION
     for x in range(int(n)): 
          a=input("Enter the customer ID: ")
          n=input("Enter the name: ")
          b=input("Enter the loan amount: ₹")
          c=input("Enter the interest rate (%): ")
          d=input("Enter the loan time (in months): ")
          print('----------------------------------------------------------------------')
          
          #ERROR HANDLING - TO CHECK IF THE INPUTS ARE OF CORRECT TYPE
          if a.isdigit()==False:
               wrong_input()
               f.close()
               return
          k=n.split()
          for i in k:
               if i.isalpha()==False:
                    wrong_input()
                    f.close()
                    return
          if is_float(b)==False:
               wrong_input()
               f.close()
               return
          if is_float(c)==False:
               wrong_input()
               f.close()
               return
          if d.isdigit()==False:
               wrong_input()
               f.close()
               return
          
          #INPUTTING DATA INTO CSV FILE
          l=[int(a),n,float(b),int(d),float(c)] 
          w.writerow(l) 
     wp=(input("Press Enter to Continue:"))
     f.close() 

#DATA MODIFY FUNCTION - TO MODIFY A PARTICULAR RECORD IN THE CSV FILE
def modify():

     #ERROR HANDLING - TO CHECK IF THE CSV FILE IS EMPTY
     if no_records_check()==True:
          return 
     
     #MODIFY OPERATION
     f=open("loan.csv", "r") 
     stud=csv.reader(f) 
     r=input("Enter Customer ID to modify: ")
     print('----------------------------------------------------------------------')

     #ERROR HANDLING - TO CHECK IF THE INPUT IS A DIGIT
     if r.isdigit()==False:
          wrong_input()
          f.close()
          return
     
     #MODIFY OPERATION
     lines=[] 
     for i in stud: 
          lines.append(i) 
     f.close() 
     f=open("loan.csv", "w", newline='') 
     w=csv.writer(f) 
     for i in lines:
          if i[0]==r: 
               a=input("Enter the customer ID: ")
               n=input("Enter the name: ")
               b=input("Enter the loan amount: ₹")
               c=input("Enter the interest rate (%): ")
               d=input("Enter the loan time (in months): ")
               print('----------------------------------------------------------------------')
          
          #ERROR HANDLING - TO CHECK IF THE INPUTS ARE OF CORRECT TYPE
               if a.isdigit()==False:
                    wrong_input()
                    f.close()
                    return
               k=n.split()
               for i in k:
                    if i.isalpha()==False:
                         wrong_input()
                         f.close()
                         return
               if is_float(b)==False:
                    wrong_input()
                    f.close()
                    return
               if is_float(c)==False:
                    wrong_input()
                    f.close()
                    return
               if d.isdigit()==False:
                    wrong_input()
                    f.close()
                    return

               #INPUTTING DATA INTO CSV FILE
               l=[int(a),n,float(b),int(d),float(c)] 
               w.writerow(l) 
               print("Record Modified Successfully, Customer ID:",a," Name:",n," Loan Amount:",b," Loan Time:",d," Interest Rate:",c)

          else:
               w.writerow(i) 
     print('----------------------------------------------------------------------')
     wp=(input("Press Enter to Continue:"))
     f.close()

#DISPLAY FUNCTION - TO DISPLAY THE CONTENTS OF THE CSV FILE
def display():

     #ERROR HANDLING - TO CHECK IF THE CSV FILE IS EMPTY
     if no_records_check()==True:
          return
     
     #DISPLAY OPERATION
     f=open("loan.csv","r",newline='') 
     acct=csv.reader(f) 
     for i in acct: 
          if i==["CUSTOMER ID","NAME","LOAN AMOUNT", "LOAN TIME", "INTEREST"]:
               continue
          else:
               print("Customer ID:",i[0]," Name:",i[1]," Loan Amount:",i[2]," Loan Time:",i[3]," Interest Rate:",i[4])
          print('----------------------------------------------------------------------')
     wp=(input("Press Enter to Continue:"))
     f.close() 

#SEARCH FUNCTION - TO SEARCH FOR A PARTICULAR RECORD IN THE CSV FILE
def search(): 

     #ERROR HANDLING - TO CHECK IF THE CSV FILE IS EMPTY
     if no_records_check()==True:
          return
     
     #SEARCH OPERATION
     a=0
     f=open("loan.csv", "r") 
     stud=csv.reader(f) 
     r=input("Enter Customer ID to search: ")
     print('----------------------------------------------------------------------')

     #ERROR HANDLING - TO CHECK IF THE INPUT IS A DIGIT
     if r.isdigit()==False:
          print("INVALID CUSTOMER ID, PLEASE TRY AGAIN")
          print('----------------------------------------------------------------------')
          wp=(input("Press Enter to Continue:"))
          print('----------------------------------------------------------------------')
          f.close()
          return
     
     #SEARCH OPERATION
     for i in stud: 
          if i[0]==r:
               print("Customer ID:",i[0]," Name:",i[1]," Loan Amount:",i[2]," Loan Time:",i[3]," Interest Rate:",i[4])
               a=1
     if a==0:
          print("Record Not Found!")
     print('----------------------------------------------------------------------')
     wp=(input("Press Enter to Continue:"))
     f.close() 

#DELETE FUNCTION - TO DELETE A PARTICULAR RECORD FROM THE CSV FILE
def delete(): 

     #ERROR HANDLING - TO CHECK IF THE CSV FILE IS EMPTY
     if no_records_check()==True:
          return
     f=open("loan.csv", "r") 
     stud=csv.reader(f) 
     r=input("Enter Customer ID to delete ('all' to delete all records): ")
     print('----------------------------------------------------------------------')

     #ERROR HANDLING - TO CHECK IF THE INPUT IS A DIGIT
     if r.lower()!='all':
          if r.isdigit()==False:
               print("INVALID CUSTOMER ID, PLEASE TRY AGAIN")
               print('----------------------------------------------------------------------')
               wp=(input("Press Enter to Continue:"))
               print('----------------------------------------------------------------------')
               f.close()
               return
     
     #IF R='all' - DELETE ALL RECORDS
     if r.lower()=='all':
          f.close()
          f=open("loan.csv", "w", newline='') 
          w=csv.writer(f) 
          l=["CUSTOMER ID","NAME","LOAN AMOUNT", "LOAN TIME", "INTEREST"]
          w.writerow(l) 
          print("All Records Deleted Successfully")
          print('----------------------------------------------------------------------')
          wp=(input("Press Enter to Continue:"))
          print('----------------------------------------------------------------------')
          f.close()
          return
     
     #DELETE OPERATION
     lines=[] 
     for i in stud: 
          lines.append(i) 
     f.close() 
     f=open("loan.csv", "w", newline='') 
     w=csv.writer(f) 
     if i[0]==r: 
          print("Deleted Record:","Customer ID:",i[0]," Name:",i[1]," Loan Amount:",i[2]," Loan Time:",i[3]," Interest Rate:",i[4]) 
     else:
          print("Record Not Found")
     for i in lines:
          if i[0]!=r: 
               w.writerow(i) 
     print('----------------------------------------------------------------------')
     wp=(input("Press Enter to Continue:"))
     f.close()

#INTEREST CALCULATION FUNCTION - TO CALCULATE THE LOAN DETAILS
def calculate_interest():

     #ERROR HANDLING - TO CHECK IF THE CSV FILE IS EMPTY
     if no_records_check()==True:
          return   
     
     #CALCULATION OPERATION
     f=open("loan.csv","r",newline='') 
     acct=csv.reader(f) 
     r=input("Enter Customer ID to calculate interest for: ")
     print('----------------------------------------------------------------------')

     #ERROR HANDLING - TO CHECK IF THE INPUT IS A DIGIT
     if r.isdigit()==False:
          print("INVALID CUSTOMER ID, PLEASE TRY AGAIN")
          print('----------------------------------------------------------------------')
          wp=(input("Press Enter to Continue:"))
          print('----------------------------------------------------------------------')
          f.close()
          return
     
     #DISPLAYING DETAILS AND CALCULATING LOAN
     c=1
     for i in acct: 
          if i[0]==r:
               principal=float(i[2])
               time=float(i[3])
               rate=float(i[4])
               interest=(principal*rate*time/12)/100
               total_amount=principal+interest
               print("Customer ID:",i[0]," Name:",i[1])
               print("Principal Amount: ₹",principal)
               print("Time (in months):",time)
               print("Rate of Interest (%):",rate)
               print("Interest Amount: ₹",interest)
               print("Total Amount to be Paid: ₹",total_amount)
               c=0
               print('----------------------------------------------------------------------')

     #ERROR HANDLING - IF RECORD NOT IN CSV FILE
     if c==1:
          print("Record Not Found!")
          print('----------------------------------------------------------------------')    
     wp=(input("Press Enter to Continue:"))
     f.close()

#CALLING THE HEADING FUNCTION TO CREATE FIELDNAMES IN THE CSV FILE
heading()

#MAIN MENU OF PROGRAM 
while True: 
     print("************************************************************************") 
     print("                         LOAN MANAGEMENT SYSTEM                         ")
     print("************************************************************************")
     print("MENU OPTIONS:")
     print("1 - INPUT RECORD")
     print("2 - DISPLAY RECORDS")
     print("3 - SEARCH RECORD")
     print("4 - MODIFY RECORD")
     print("5 - DELETE RECORD")
     print("6 - CALCULATE LOAN")
     print("7 - EXIT")
     print("**********************************************************************")
     ch=(input("Enter Your Choice: ")) 
     print('----------------------------------------------------------------------')

     #ERROR HANDLING - TO CHECK IF THE INPUT IS A DIGIT
     if ch.isdigit()==False:
          print("INVALID CHOICE, PLEASE TRY AGAIN")
          print('----------------------------------------------------------------------')
          wp=(input("Press Enter to Continue:"))
          print('----------------------------------------------------------------------')
          continue

     #MENU OPTIONS
     if int(ch)==1: 
          data() 
     if int(ch)==2: 
          display() 
     if int(ch)==3: 
          search()
     if int(ch)==4: 
          modify() 
     if int(ch)==5: 
          delete()
          #TO ASK USER IF THEY WANT TO DELETE ANOTHER RECORD
          que=input("Delete Another Record? (y/n) default=n): ")
          print('----------------------------------------------------------------------')
          if que.lower()=='y'or que.lower()=='yes':
                    delete()
     if int(ch)==6:
          calculate_interest()
     if int(ch)==7: 
          print("THANK YOU")
          break

     #ERROR HANDLING - TO CHECK FOR INVALID MENU CHOICES
     elif int(ch) not in [1,2,3,4,5,6,7]:
          print("INVALID CHOICE, PLEASE TRY AGAIN")
          print('----------------------------------------------------------------------') 
          wp=(input("Press Enter to Continue:"))
          print('----------------------------------------------------------------------')    
