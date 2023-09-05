amount = int(input("How many numbers wil you be entering? "))

numbers = []
for count in range(amount):
    numb = int(input("Enter your number:> "))
    numbers.append(numb)
print("\nYour numbers are",numbers)

#sorting the list of numbers:
def selfsort():
    count = 0
    for count in range(len(numbers)):
    	while count+1 <= len(numbers)-1:
    		if numbers[count]> numbers[count+1]:
                temporary = numbers[count+1]
                #print(temporary)
                numbers[count+1] = numbers[count]
                numbers[count] = temporary
    			#print(numbers)
    			count = count +1
    		elif numbers[count] < numbers[count+1] or numbers[count] == numbers[count+1]:
                count = count+1

for count in range(len(numbers)):
    selfsort()
print("From low to high that's", numbers)


#finding the median:

mid = len(numbers)//2

if len(numbers)%2 != 0:    #if it's odd
    median = numbers[mid]  #middle index is the length/2, rounded down. so if index ==2, the number is the third one in the list. it works because the len/2 is truncated
    print("\nThe median is",median)
else:
    median = (numbers[mid-1]+numbers[mid])/2 #if even. not the same as odd because truncation of len doesn't changeanything (so nothing is rounded down)
    print("\nThe median is",median)

    


