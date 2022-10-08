#OTP generator from odd places of a given number by squaring the digit in position

number=input()
length_num=len(number)
#print(length_num )
res=""
#print(res)
for i in range(1,length_num,2): #for odd positions
    res+=str(int(number[i]) **2)
    #print("square of odd places:"+res)
    
print("OTP is:"+(res[0:8]))