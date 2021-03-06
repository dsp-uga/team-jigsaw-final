import re
import csv
"""
This reads in all the files from the Kaggle test.csv file and generates a file
listing all the filtered words encountered along with a basic count
"""
def run(kaggleTestFile,testCountOutputFile):
    results = {}
    words = []
    
    lineCount = 0
    
    with open(kaggleTestFile, mode='r') as csv_file:
    	csv_reader = csv.DictReader(csv_file)
    	for row in csv_reader:
    		if lineCount == 0:
    			lineCount += 1
    		lineCount += 1
    		row["comment_text"] = re.sub('[^a-zA-Z0-9]+',' ', \
                 row["comment_text"])
    		row["comment_text"] = re.sub('\s+',' ',row["comment_text"])
    		row["comment_text"] = re.sub('^\s+','',row["comment_text"])
    		row["comment_text"] = re.sub('\s+$','',row["comment_text"]).lower()
    
    		arr = row["comment_text"].split(' ')
    
    		for j in range(0,len(arr)):
    			if len(arr[j]) > 250:
    				continue
    			if len(arr[j]) == 0:
    				continue
    			if arr[j] not in results:
    				results[arr[j]] = 0
    				words.append(arr[j])
    			results[arr[j]] += 1
    	csv_file.close()
    
    words.sort()
    with open(testCountOutputFile,mode="w") as output:
    	for word in words:
    		output.write(word+","+str(results[word])+"\n")
    	output.close()
