'''
Written 9/22/21 by Wyatt Homola

This program lists the winners of the following game: 

A group of people choose a number between 0 and 100.  The winning answer is the one closest to 2/3 of the average answer.  Assuming that everyone has received this same explanation and that you would like to win, which number will you choose?
'''

# students = {
    # 'Wyatt': 10,
    # 'Andrew': 7,
    # 'Aiden': 71,
    # 'Cal': 52
# }

# C day
# students = {
    # 'Lyza': 55,  
    # 'Tri': 33, 
    # 'Elijah': 33,
    # 'Aumrey': 44,
    # 'Brandis': 0,
    # 'Zoey': 23,
    # 'Benjamin': 51,
    # 'Wyatt': 56,
    # 'Xzavier': 2,
    # 'Zack': 55,
    # 'Ella': 61,
    # 'Noah': 12,
    # 'Samantha': 13,
    # 'Ashley': 72,
    # 'Scarlet': 50,
    # 'Abby':4
# }
# Zoey wins 10/5/21  -  she just wrote 23 cuz 2/3 is on the board

# B day 
students = {
    'Makenna':
    'Rory':
    'Matthew':
    'Celeste': 
    'Isobel':
    'Ella': 
    'Sean':
    'Wyatt':
    'Tristan':
    'Hannah':
    'Emmah':
    'Kamiryn':
    'Josephine':
    'Logan':
    'Sophia':
    'Greyson':
    'Eleanor':
}

def getavg(students):
    total = 0
    count = 0
    for i in students:
        if students[i] is not None:
            total += students[i]
            count += 1
    return total * 2 / (3 * count)

def getbest(students):
    avg = getavg(students)
    best = 1e6
    student = []
    for i in students:
        if students[i] is not None:
            diff = (students[i] - avg) ** 2
            if diff == best:
                student.append(i)
            if diff < best:
                student = [i]
                best = diff
    return student

print(getavg(students))
print(getbest(students))