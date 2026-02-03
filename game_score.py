name = str(input("Enter Your Name : "))
games_played = int(input("Number of games played : "))
score_achived = int(input("Total score achieved : "))

avg_score = score_achived / games_played

print(f'''Player : {name}\nGames Played : {games_played}\nTotal Score : {score_achived}\nAverage Score : {avg_score}''')