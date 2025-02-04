import os
import json
from user import User
import random

resource_folder = os.path.join(os.path.dirname(__file__), '..', 'db')
json_file_path = os.path.join(resource_folder, 'questions.json')

with open(json_file_path, 'r') as file:
    questions_data = json.load(file)

def run_quiz(user: User):
    random.shuffle(questions_data)
    nums_questions = len(questions_data)
    
    for q in questions_data:
        print(q['question'])
        for ops in q['options']:
            print(ops)
        print()
        
        user_ans = input('Enter your answer: ')
        if (check_answer(user_ans, q['answer'])):
            print('Correct!')
            user.update_score(1)
        else:
            print('Incorrect!')
    print()
    print(f'{user.name}\'s got total Score: {user.get_score()}/{nums_questions}')

def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer.upper()