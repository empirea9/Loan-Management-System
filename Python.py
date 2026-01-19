def c_words(): 
     f = open("STORY.TXT", "r") 
     content = f.read() 
     
    upper_count = 0 
     lower_count = 0 
 
     for ch in content: 
          if ch.isupper():     # Check if the character is uppercase 
               upper_count += 1 
          elif ch.islower():   # Check if the character is lowercase 
               lower_count += 1 
    
     print("No. of upper case letters are:", upper_count) 
     print("No. of lower case letters are:", lower_count) 
     
     f.close() 
 
       c_words()  