Indian = ["Gujarati Thali", "Punjabi Thali","Dosa", "Aamras", "Shrikhand-puri"]
Italian = ["Pasta", "Pizza", "Panini", "Lasagna"]
American = ["Burger", "NYC Pizza", "French fries", "Cheeseburger", "hotdog"]
Mexican = ["Tacos", "Burrito bowl", "Mexican rice", "Nachos with cheese dip"]
Chinese = ["Manchurian","Hakka noodles", "Soup","Fried rice"]

str = input("Name your dish: ")
if str in Indian:
    print("Your dish is in Indian")
elif str in Italian:
    print("your dish is Italian")
elif str in American:
    print("Your dish is American")
elif str in Mexican:
    print("Your dish is Mexican")
elif str in Chinese:
    print("Your dish is some Chinese")
else:
    print("Your dish does not belong here, Please choose from the menu:)")