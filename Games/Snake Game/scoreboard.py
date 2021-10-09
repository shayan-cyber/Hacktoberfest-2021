from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Oxygen Mono', 14, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.updated_score()
            
    def updated_score(self):
        self.clear()
        with open("Projects\Snake-Game\data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.updated_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score 
            with open("Projects\Snake-Game\data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.updated_score()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)