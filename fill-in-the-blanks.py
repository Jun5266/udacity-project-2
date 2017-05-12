# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1

#-*- coding: utf-8 -*-
#把答案替换进文章
def show_answer(blank_name,answer_list,quiz):
	'''输入为：空格编号，答案列表和测试文章。输出替换正确答案后的文章'''
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

#判断用户输入是否正确并给出对应结果
def answer_test(quiz, answer_list):
	'''输入为：测试内容和答案列表。输出为判断回答是否正确的结果'''
	index = 0
	times = 0
	print (quiz)

	
	while index < len(answer_list) and times < 5:
		user_input = input("Guess the answer for "+str(index+1)+": ")
		if user_input == answer_list[index]:
			print ('Nice job!')
			index += 1
			times = times
			quiz = show_answer(index,answer_list,quiz)
			print (quiz)
		else:
			print('Please try again!')
			times += 1
			index = index
	
	if times < 5:
		print ('Congratulations, you pass the quiz!')
	
	else:
		print ('Sorry, you failed!')
					
			

		

#判断用户选择难度
#不同难度的测试列表和对应答案
quiz1 = '''Each morning, I get up early. When I wake up, I give 
thanks __1__ my achievements and the person I have become.
 My reflection __2__(remind) me to be grateful for the 
 unique characteristics that make me who I am. At times, 
 I may not feel pleased __3__ the characteristics that 
 I struggle to improve on. But that feeling doesn't remain 
 with me for long __4__ I tell myself that there is so much
  more I can celebrate about me and my life. '''
quiz2 = '''When I am not __1__ (please) with my body weight, for example, 
I avoid always thinking about that feeling. Instead, I ask __2__ 
why at I plan to do about it. I am also learning to be happy __3__
 what I already have. My life and environment are really extensions
  of me — __4__ (result) from doing the best I can with the gifts 
  and challenges of my life’s journey.'''
quiz3 = '''Today, I look in the mirror and see __1__ divine creation,
 I commit __2__ loving the person __3__ looks back at me because I
  am __2__ (true) blessed.'''
quiz4 = '''What’s the hottest news recently? __1__is no doubt 
that it belongs to the icebucket challenge，which is
 __2__ (mean)to raise money to help the ALS patients
  who have trouble __3__ (move) because __4__ their hard muscles.'''

answer1 = ['for','reminds','with','because']
answer2 = ['pleased','myself','with','resulting']
answer3 = ['a','to','who','truly']
answer4 = ['There','meant','moving','of']

quiz_list = [quiz1,quiz2,quiz3,quiz4]
answers_list = [answer1,answer2,answer3,answer4]
user_input = input(
	"Welcome to the quiz!\nPlease choose your quiz level:\
	\n\t0--easy\n\t1--medium\n\t2--hard\n\t3--expert\n\t")
index = int(user_input)

answer_test(quiz_list[index],answers_list[index])


