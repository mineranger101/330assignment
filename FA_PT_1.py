#check is locked true?
def LockCheck(key, LockStatus):
    if key == 1 and LockStatus is True: 
        print("Unlocked")
        return False



    elif key == 4 and LockStatus is False: 
        print("Locked")
        return True


    else:
        if (key == 1) or (key == 4): 
            if LockStatus is True:
                print("Locked")
            else:
                print("Unlocked")
        return LockStatus
def getDigit(number, n):
    return number[n]
def main():
    Code = "40061"  #Student ID: A204(40061)
    LockStatus = True 
    State = 0  


    print("Part 1")
    print(" The code is XXXXX1 for unlock and XXXXX4 for lock \n",
	    " Where XXXXX is the students ID in the case for this assignment \n",
	    "as soon as the last valid digit is entered you will receive and output")
    print("Input Passcode:")
    while(True):
        val = input(" ")
        key = getDigit(Code, State)
   
    
        if val is key: 
            State += 1
        else: 
            State = 0
        if State == 5: 
            Value = int(input("key- "))
            LockStatus = LockCheck(Value, LockStatus)
            State = 0 


if __name__ == "__main__":
    main()
