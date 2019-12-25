score = input("Enter Score between 0.0 to 1.0: ")
try:
    s=float(score)
    
except:
    print("error:enter numeric values between 0 & 1")
    quit()
    

if s>1:
    print("Score out of range")
elif s<0:
    print("Score out of range")
            
elif s>=0.9:
    print("A")
elif s>=.8:
    print("B")
elif s>=.7:
    print("C")            
elif s>=.6:
    print("D")
elif s<.6:
    print("F")
else:
    print("error")  # here else is not reqd s all condiions are covered i think
