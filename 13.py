# Question: Complete the script so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.
# my_range = range(1, 21)
# Expected output: 
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'] 


my_range = range(1, 21)
my_list = []
for num in range(1,21):
    my_list.append(str(num))

print(my_list)

# 2nd solution

print(list(map(str, my_range)))