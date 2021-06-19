team1=[]
for i in range(4):
    points1=int(input("Enter points for team1"))
    team1.append(points1)

team2=[]
for i in range(4):
    points2=int(input("Enter points for team2"))
    team1.append(points2)

if sum(team1)>sum(team2):
    print("1")
else:
    print("2")
