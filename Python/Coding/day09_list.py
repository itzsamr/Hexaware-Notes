# marks = [98,75,40,80,90,45,80,60]
# print(len(marks))
# print(marks[:4])
# print(marks[::-1])
# marks.append(78)
# print(marks)

# Add 65 after 40
# sci = 65
# marks.insert(3, sci)
# print(marks)

price_list = [1000, 1500, 400]
price_list_copy = price_list ## Copy by reference
price_list1 = [1000, 1500, 400]
 
price_list_copy.append(600)
price_list.append(700)
price_list1.append(800)
 
print(price_list, price_list_copy, price_list1)