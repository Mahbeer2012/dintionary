# initialise dictionary
test_dict = {'codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'codingal' : 1}

#printing oringinal dictionary
print("the oringinal dictionary :" + str(test_dict))

#initialize value
k = 2

# using loop
# selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

# printing result
print("frequency of k is :" + str(res))
