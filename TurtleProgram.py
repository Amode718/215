# Turtle Program representation & execution
# Prof. O & CPTR-215
# 2020-12-02 first draft
# 2020-12-04 adding inheritance

from turtle import *


class TurtleCommand:
    pass

class MoveCommand(TurtleCommand):
    def __init__(self, distance=100, direction="F"):
        self.distance = distance
        self.direction = direction
    def __str__(self):
        if self.direction == "F":
            return f"forward({self.distance})"
        else:
            return f"back({self.distance})"
    def __repr__(self):
        return f"MoveCommand({self.distance}, {self.direction!r})"
    def execute(self):
        forward(self.distance if self.direction == "F" else -self.distance)

class TurnCommand(TurtleCommand):
    def __init__(self, angle=90, direction="R"):
        self.angle = angle
        self.direction = direction
    def __str__(self):
        if self.direction == "R":
            return f"right({self.angle})"
        else:
            return f"left({self.angle})"
    def __repr__(self):
        return f"TurnCommand({self.angle}, {self.direction!r})"
    def execute(self):
        if self.direction == "R":
            right(self.angle)
        else:
            left(self.angle)

class ClearCommand(TurtleCommand):
    def __init__(self):
        pass
    def __repr__(self):
        return f"ClearCommand()"
    def __str__(self):
        return "clear()"
    def execute():
        clear()

class ResetCommand(TurtleCommand):
    def __init__(self):
        pass
    def __repr__(self):
        return f"ResetCommand()"
    def __str__(self):
        return "reset()"
    def execute():
        reset()


class PositionCommand(TurnCommand):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"PositionCommand({self.x, self.y})"
    def __str__(self):
        return f"penup()\ngoto({self.x}, {self.y})\npendown()"
    def execute(self, x, y):
        penup()
        goto(self.x,self.y)
        pendown()
        
class LoopCommand(TurtleCommand):
    def __init__(self, iterations=1, commands=[]):
        self.iterations = iterations
        self.commands = commands
    def __str__(self):
        result = f"for _ in range({self.iterations}):\n"
        for command in self.commands:
            result += f"    {command}\n"
        return result
    def __repr__(self):
        return f"LoopCommand({self.iterations}, {self.commands!r})"
    def execute(self):
        for _ in range(self.iterations):
            for command in self.commands:
                command.execute()

if __name__ == "__main__":
    square = LoopCommand(4, [MoveCommand(100), TurnCommand(90)])
    triangle = LoopCommand(3, [MoveCommand(100), TurnCommand(120)])
    house = [square, TurnCommand(60, "L"), triangle]
    window = [TurnCommand(105, 'R'), MoveCommand(53), TurnCommand(45, 'R'), LoopCommand(4, [LoopCommand(4, [MoveCommand(20), TurnCommand(90)]), TurnCommand(90, "R")])]
    for command in house:
        command.execute()
    for command in window:
        command.execute()
        #ResetCommand.execute()
        ClearCommand.execute()

    PositionCommand(0,0)