from question_model import Question
from data import question_data

'''
Good example of converting a dictionary within a list to a list of objects.
Also great example of splitting a project into manageable parts, e.g.
Model / Data / Main / SP 15/04/2022
'''

question_bank = []

for question in question_data:

    question_bank.append(Question(question["text"], question["answer"]))

for question in question_bank:
    print(question.answer)