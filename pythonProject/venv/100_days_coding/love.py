name1=input("Enter your name  :").lower()
name2=input("Enter your parterns name :").lower()
count_t = name1.count("t") + name2.count("t")
count_r = name1.count("r") + name2.count("r")
count_u = name1.count("u") + name2.count("u")
count_e = name1.count("e") + name2.count("e")


count_l = name1.count("l") + name2.count("l")
count_o = name1.count("o") + name2.count("o")
count_v = name1.count("v") + name2.count("v")

first_number = count_t+count_r+count_u+count_e
second_number = count_l+count_o+count_v+count_e
r1 = str(first_number)
r2 =str(second_number)
print(f"Love percentage is {r1+r2}")
