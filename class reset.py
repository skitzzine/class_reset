print ("DISCLAIMER: THIS SOFTWARE VERSION IS UNSTABLE AS THERE ARE BUGS YET TO BE FIXED. THIS VERSION IS JUST A SLIGHT IMPROVISATION FROM THE PREVIOUS ONE.")
print ("ver:0.1.2(1224)")
print ("app developed by Percy, Daniel and fellow contributor(s).")
import random
#data
males =  ["Nam Anh", "Xuan Hung", "Quang Huy", "Bao Lam", "Gia Binh", "Gia Vinh", "Nguyen Khanh", "Tri Duc", "An Huy", "Lan Hoang", "Ich Tue", "Minh Duong", "Anh Dung", "Hoang Minh"]
females = ["Vi An", "Ha Anh", "Thuy Duong", "Khanh Huyen", "Thanh Ha", "Minh Khue", "Minh Thu", "Ha Uyen", "Uyen Nhi", "Khanh Ngoc", "Ngan Thi", "Bao Lan", "Khanh Trang", "Khanh Van", "Thao Nguyen"]
emc1_class = males+females
group_leaders = ["Tri Duc", "Gia Binh", "Ngan Thi", "Anh Dung"]
groups = ["group_1", "group_2", "group_3", "group_4"]
group_size =  [7,7,7,8]
#first round of shuffling 
random.shuffle(males) 
random.shuffle(females)
#second round of shuffling cus y not :)) 
for _ in range(4):
    random.shuffle(emc1_class) 
groups = [[] for _ in range (len(group_size))]
for i, size in enumerate(group_size):
    males_count = size // 2 
    females_count = size - males_count
    while len(groups[i]) < size:
        for group_members in list(emc1_class):
            if group_members in group_leaders and any(m in group_leaders for m in groups[i]):
                continue
        groups[i].append(group_members)
        emc1_class.remove(group_members)
        if len(groups[i]) > size:
            break
     #round three of shuffling, now for groups. i love randomisation.
random.shuffle(groups[i])
#ui for user
for i, group in enumerate(groups):
    while True:
        user_input = input(f"Do you want to see Group {i+1}? Push 'Enter' to continue:")
        if user_input == ("fuck you", "nigger", "nope", "nuh uh", "those who know :skull", "faggot", "retard", "retarded faggot", "shut up nigger", "nigger nigga nigger"):
            print("shut up idiot")
            continue
        elif len(user_input) > 0:
            print("i said push enter, not elaborate your whole life.")
            continue
        else:
            print("Here you go!")
            print(f"Group {i+1}: {group}")
        user_input = input("Do you want me to repeat? (y/n):")
        if user_input == "y":
            print("Alright! Here you go!")
            print(f"Group {i+1}:{group}")
            break
        if user_input == "n":
            print ("Ok then!")
            break
        if user_input not in ("y", "n"):
            print("TYPE Y OR N.")
            continue