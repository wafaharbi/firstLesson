
# ------  The fifth day challenges------- #

# initilize the variables x , y ,z to their value

x = "apple"
y = "orange"
z = "limon"

basket = x + y + z   #combine the three values  
 
print(basket)        #print appleorangelimon

print("\n")


# _____  print two character of basket   ________  

n = 2    # number of splitting characters

basket=[basket[i:i+n] for i in range(0 , len(basket) , n)]

print(basket)    #That print ['ap', 'pl', 'eo', 'ra', 'ng', 'el', 'im', 'on']


print("\n")


basket = [x , y, z]
n = [5]

basket = [basket[sum(n[:i]):sum(n[:i+1])] for i in range(len(n))]
print("The word in seperated word", basket)        #print apple orange limon
