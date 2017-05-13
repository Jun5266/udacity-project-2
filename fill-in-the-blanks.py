#-*- coding: utf-8 -*-
'''this function will replace the blanks in quit with right answers:
		Attibute:
				blank_name: No. of blanks
				answer_list: the list of right answers
				quiz: the body of the quiz passages'''
def show_answer(blank_name,answer_list,quiz):
	words_list = quiz.split()
	index = 0
	replace = []
	for word in words_list:
		if str(blank_name) in word:
			replace.append(answer_list[blank_name-1])
		else:
			replace.append(word)
		index += 1
	return ' '.join(replace)

'''judge the ansers offered by users.
		Attribute:
		quiz: the body of the quiz passages
		answer_list: the list of right answers'''
def answer_test(quiz, answer_list):
	index = 0
	times = 0
	print (quiz)
# python 3里面的print需要括号，2 不需要	
	while index < len(answer_list) and times < 5:
		user_input = input("Guess the answer for "+str(index+1)+": ")
		if user_input == answer_list[index]:
			print ('Nice job!')
			index += 1
			quiz = show_answer(index,answer_list,quiz)
			print (quiz)
		else:
			print('Please try again!')
			times += 1
	
	if times < 5:
		print ('Congratulations, you pass the quiz!')
	
	else:
		print ('Sorry, you failed!')
					
			

		

#the quiz passages and answers list
easy_quiz = '''Each morning, I get up early. When I wake up, I give 
thanks __1__ my achievements and the person I have become.
 My reflection __2__(remind) me to be grateful for the 
 unique characteristics that make me who I am. At times, 
 I may not feel pleased __3__ the characteristics that 
 I struggle to improve on. But that feeling doesn't remain 
 with me for long __4__ I tell myself that there is so much
  more I can celebrate about me and my life. '''
medium_quiz = '''When I am not __1__ (please) with my body weight, for example, 
I avoid always thinking about that feeling. Instead, I ask __2__ 
why at I plan to do about it. I am also learning to be happy __3__
 what I already have. My life and environment are really extensions
  of me — __4__ (result) from doing the best I can with the gifts 
  and challenges of my life’s journey.'''
hard_quiz = '''Today, I look in the mirror and see __1__ divine creation,
 I commit __2__ loving the person __3__ looks back at me because I
  am __2__ (true) blessed.'''
expert_quiz = '''What’s the hottest news recently? __1__is no doubt 
that it belongs to the icebucket challenge，which is
 __2__ (mean)to raise money to help the ALS patients
  who have trouble __3__ (move) because __4__ their hard muscles.'''

easy_answer = ['for','reminds','with','because']
medium_answer = ['pleased','myself','with','resulting']
hard_answer = ['a','to','who','truly']
expert_answer = ['There','meant','moving','of']

quiz_list = [easy_quiz,medium_quiz,hard_quiz,expert_quiz]
answers_list = [easy_answer,medium_answer,hard_answer,expert_answer]
user_input = input(
	"Welcome to the quiz!\nPlease choose your quiz level:\
	\n\t0--easy\n\t1--medium\n\t2--hard\n\t3--expert\n\t")
index = int(user_input)

answer_test(quiz_list[index],answers_list[index])


