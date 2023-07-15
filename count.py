# count = 0;  
# import required module
import os
# assign directory
directory = 'economicprinciples.org/'

# iterate over files in
# that directory
sum = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
	# checking if it is a file
    if os.path.isfile(f):
	    # print(f)
        count = 0
        
        print(f)
#Opens a file in read mode  
        file = open("{}".format(f), encoding="utf-8")    
        #Gets each line till end of file is reached  
        for line in file:  
            #Splits each line into words  
            words = line.split(" ");  
            #Counts each word  
            count = count + len(words);  
            sum+= len(words)
        print("Number of words present in given file: " + str(count));  
        file.close();  
print("Total number of words present in all given files: " + str(sum));  

