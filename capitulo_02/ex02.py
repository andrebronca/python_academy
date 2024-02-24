a = 123.456789
b = 15
c = 1234456789
print("%5.3e"% (a))
print("%10.3e"% (a))
print("%15.3e"% (a))
print("%-15.3e"% (a))
print("%5.3e"% (a))
print("%o"% (b))
print("%5.3o"% (b))
print("%x"% (b))
print("%X"% (b))
print("%10x"% (b))
print("%10.3x"% (b))
print("%x%%"% (b))
print("%d"% (c))
print("%d,"% (c))
print("{0:4,d}".format(c))
print("{0:06d}".format(123))
print("{0:4,.5f}".format(123456789.123456789))
print()

print("this book costs {0:f} only".format(150.99))
print("this book costs {0:8f} only".format(150.99))
print("this book costs {0:.2f} only".format(150.99))
print("this book costs {0:.3f} only".format(150.99))
print("this book costs {0:.0f} only".format(150.99))
print("this book costs {0:e} only".format(150.99))
print("this book costs {0:1} only".format(150.99))
print("this book costs {0:d} only".format(150))
print("this book costs {0:8d} only".format(150))
print("this book costs {0:o} only".format(150))     #octal
print("this book costs {0:b} only".format(150))     #binary
print("{:d}".format(-15))
print("{:=7d}".format(-15))
print("{:=7d}".format(15))