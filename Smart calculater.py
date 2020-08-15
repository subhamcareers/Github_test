#Arguments with one or more values
def verdict(m1,m2,m3):
    total=m1+m2+m3
    if total>=15000:
        print("Yes You can purchase a smartphone")
    else:
        print("Sorry! you've gotto save more.")
    return
teach=int(input("Fees that you get from teaching: Rs. "))
saving=int(input("Savings that have: Rs. "))
salary=int(input("Your current Salary: Rs. "))
verdict(teach,saving,salary)
