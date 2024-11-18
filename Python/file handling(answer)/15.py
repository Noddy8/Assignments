#EX- 15 Check Whether of Mobile number.
try:
    mn = int(input("Enter The Number :"))
    mn = str(mn)
    if int(mn[0])>5 and len(mn)== 10:
        print("It's Correct.")
    elif int(mn[0])<6:
        raise Exception("Invalid Number. Number Must start from 6,7,8 or 9.")
    else:
        raise Exception("Invalid Number. Number Must be a 10 Digit.")
except Exception as e:
    print(e)

