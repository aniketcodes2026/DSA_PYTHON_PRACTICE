# Problem: Finding the Percentage
# Concept: Dictionaries / Hash Maps
# Platform: HackerRank

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() # read the name and the scores of the student, the *line syntax allows us to capture all remaining inputs as a list
        scores = list(map(float, line)) # convert the scores from strings to floats and store them in a list called scores
        student_marks[name] = scores # store the scores in the dictionary with the student's name as the key and the list of scores as the value
    query_name = input()
    scores=student_marks[query_name]
    avg=sum(scores)/len(scores) 
    print(f"{avg:.2f}") #prints the average of the scores with 2 decimal places
