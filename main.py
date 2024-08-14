import random as r

dict = {
 "1":"Stone",
 "0":"Paper",
 "-1":"Scissors"
}

def check(k1, k2):
  if k1 == k2:
    return 0
  elif k1 == 1 and k2 == 0:
    return k2
  elif k1 == 1 and k2 == -1:
    return k1
  elif k1 == 0 and k2 == -1:
    return k2
  elif k1 == 0 and k2 == 1:
    return k1
  elif k1 == -1 and k2 == 1:
    return k2
  elif k1 == -1 and k2 == 0:
    return k1
if __name__ == '__main__':
 score_a = 0
 score_b = 0

 while True:
   try:
    a = int(input("""
Enter 1 for Stone
Enter 0 for Paper
Enter -1 for Scissors

Press any key other than those mentioned to exit and view results

Enter your choice: 
"""))
    b = r.randint(-1,1)
    if check(a,b) == 0:
     pass
    elif check(a,b) == a:
     score_a += 1
    elif check(a,b) == b:
     score_b += 1

    print(f"""
    Your Choice: {dict[str(a)]}
    Computer's Choice: {dict[str (b)]}
    
    {"+1 For Player" if check(a,b) == a else ("+1 for computer" if check(a,b) == b  else 'Draw') }
    
    Your Score: {score_a}
    Computer's Score :{score_b}
    """)
   except:
     print("------Game Results-------\n")
     if score_a > score_b:
       print("You Won")
     elif score_a < score_b:
       print("Computer Won")
     else:
       print("Draw")
     print(f"Player: {score_a}\nComputer: {score_b}")
     
  
     
    
  
    
    