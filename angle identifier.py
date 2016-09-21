print("Enter any anguler values")
a=int(input("Enter the angle="))
if 0<a<90:
    print("Your enter angle present in first  quadrent")
elif 90<a<180:
    print("Your enter angle present in second quadrent")
elif 180<a<270:
    print("Your enter angle present third  quadrent")
elif 270<a<360:
    print("Your enter angle present in fourth  quadrent")
else:
    print("This is a quadrental angle")
