#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Giddeon
#
# Created:     20/05/2020
# Copyright:   (c) Giddeon 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
x = 1
y = "2"
z = 3
sum = 0
for i in (x,y,z):
    if isinstance(i, int):
        sum += i
print (sum)
if __name__ == '__main__':
    main()
