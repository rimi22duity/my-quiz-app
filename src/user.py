class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, increment=1):
        self.score += increment

    def get_score(self):
        return self.score
    
    def __str__(self):
        return f"User: {self.name} Score:{self.score}"