import pandas as pd
import re

file_path = 'input-2.txt'

data = pd.DataFrame()

results_list = []
with open(file_path, 'r') as file:
     for line in file:
        game = line.strip().split(':')[0]
        results = line.strip().split(':')[1]
        game_number = int(game.split(' ')[-1])
        results = results.split(';')
        for r in results:
            green_match = re.search(r'(\d+)\s+green', r)
            red_match = re.search(r'(\d+)\s+red', r)
            blue_match = re.search(r'(\d+)\s+blue', r)
            res = {'game_number': game_number, 'green': 0, 'red': 0, 'blue': 0}
            if green_match:
                res['green'] = int(green_match.group(1))
            if red_match:
                res['red'] = int(red_match.group(1))
            if blue_match:
                res['blue'] = int(blue_match.group(1))
            
            results_list.append(res)
df = pd.DataFrame(results_list)
# 12 red cubes, 13 green cubes, and 14 blue cubes
df['passed_test'] = (df['red'] <= 12) & (df['green'] <= 13) & (df['blue'] <= 14)
df_pct = df.groupby('game_number')['passed_test'].mean().reset_index()

solution = df_pct.query('passed_test == 1')['game_number'].sum()
print(solution)
