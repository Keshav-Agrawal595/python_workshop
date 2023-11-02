score = 0 # global scope 

def increase_score(points):
    global score
    score+=points
    print(score)

increase_score(10)
print(f"Score : {score}")
