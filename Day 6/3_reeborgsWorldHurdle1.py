#put this function in Reeborg's World game
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def rep1():
    move()
    turn_left()
    move()
    
    turn_right()
    move()
    
    turn_right()
    move()
    
def rep(): 
    turn_left()
    move()
    
    turn_left()
    move()
    
    turn_right()
    move()
    
    turn_right()
    move()
    
    
rep1()
for step in range(5):
    rep()