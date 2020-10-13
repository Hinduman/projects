''' This program scans the sample questions from file 'LabelledData.txt' file
	and seperates questions based on what,when,who or yes/no types
	then based on this data the user question is judged.
	Error=20%-10% i.e In 10 questions, 2 or 1 answer's might not match with theorical judgement
	If more number of different questions are typed in file, in format that is followed, error might decrease'''

def func(arg,arg1):#this function counts the word resemblance between arg and arg1
	cnt=0
	for x in arg.split():
		if x in arg1:
			cnt+=1
	return cnt

#below variables stores the what, when, yes/no questions.
what,when,affir=[],[],[]
#below loop scans the file, line by line and stores first 3 words of every line in different variables
for x in open('LabelledData.txt'):
        temp=x.split()
        if temp[-1] == 'what':
                what.extend(temp[:3])
        elif temp[-1] == 'when':
                when.extend(temp[:3])
        elif temp[-1] == 'affirmation':
                affir.extend(temp[:3])
else:#after the loop is finished the data stored in variables are filtered, removing the less frequent words.
        what=' '.join(set(filter(lambda x:True if what.count(x) > 20 else False,what)))
        when=' '.join(set(filter(lambda x:True if when.count(x) > 5 else False,when)))
        affir=' '.join(set(filter(lambda x:True if affir.count(x) > 5 else False,affir)))

#below line takes input from user
var=input()
#below if block counts the occurance of words in variables and outputs the type of question
if var.split()[0].lower() == 'what' and func(var,what) >= 2:
	print('"what?" question type')
elif func(var,when) >= 2:
	print('"when?" question type')
elif func(var,affir) >= 2:
	print('"Yes/No?" question type')
elif var.split()[0].lower() == 'who':
	print('"Who?" question type')
else:
	print('"Unknown" question type')

