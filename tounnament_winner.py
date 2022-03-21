
HOME_TEAM_WON = 1

competitions = [['java', 'c#'], ['c#', 'python'], ['python', 'java']]
results = [0, 0, 1]

def identify_tournament_winner(competitions, results):
    current_best_team = ""
    scores = {current_best_team : 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winning_team = home_team if result == HOME_TEAM_WON else away_team

        update_team_scores(team=winning_team, scores=scores, points=3)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team
        
    print(current_best_team)


def update_team_scores(team, scores, points:int=3):
    if team not in scores:
        scores[team] = 0
    scores[team] += points



identify_tournament_winner(competitions=competitions, results=results)