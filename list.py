fruits = ["apple", "banana", "cherry","watermelon","blueberry"]
print(fruits[1])

fruits[1] = "blackcurrant"
print(fruits)

fruits[1:3] = ["kiwi", "mango", "pineapple"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.insert(3, "grape")
print(fruits)

tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)

fruits.remove("watermelon")
print(fruits)

fruits.pop(1)
print(fruits)

#del fruits
fruits.sort(reverse=True)
print(fruits)
#นายชยากร หยางตระกูล เลขที่ 4 ชั้น 6/14