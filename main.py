from question_model import Question
from data import question_data

'''
Good example of converting a dictionary within a list to a list of objects.
Also great example of splitting a project into manageable parts, e.g.
Model / Data / Main / SP 15/04/2022
'''

question_bank = []

for question in question_data:
    # The short way
    question_bank.append(Question(question["text"], question["answer"]))
    # The long way
    # question_text = question["text"]
    # question_answer = question["answer"]
    # new_question = Question(question_text, question_answer)
    # question_bank.append(new_question)

for question in question_bank:
    print(question.answer)