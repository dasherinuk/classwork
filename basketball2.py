lst_team1 = []
lst_team2 = []
for i in range(4):
    team1, team2 = [int(item) for item in input().split()]
    lst_team1.append(team1)
    lst_team2.append(team2)

if sum(lst_team1)>sum(lst_team2):
    print(sum(lst_team1),"team 1 is more")
else:
    print(sum(lst_team2),"team 2 is more")

