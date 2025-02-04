from quiz import run_quiz
from user import User

def main():
    user_name = input('Enter User name: ')
    user = User(user_name)
    print(f'Welcome to python quiz {user.name}!!')
    run_quiz(user)

if __name__== "__main__":
    main()