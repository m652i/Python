scores = list()
score = int(input('please enter score: '))
while score != 999:
 

    if score > 0 and score <= 100:
        scores.append(score)
    elif score < 0:
        print('enter above 0')
    elif score > 100:
        print('enter below 101')
    score = int(input('please enter score: '))

print('Total scores entered : ', len(scores))
print('Max : ',max(scores))
print('Min : ',min(scores))
print('Average : ',sum(scores)/len(scores))
