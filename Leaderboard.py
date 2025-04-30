import pygame

class Leaderboard:
    def __init__(self):
        self.file_path = 'Leaderboard.txt'

    def read_leaderboard(self):
        leaderboard_data = []
        with open(self.file_path, 'r') as file:
            for line in file:
                stat = line.strip().split(',')
                leaderboard_data.append(stat)
        print(leaderboard_data)
        return leaderboard_data
    
    def add_to_leaderboard(self, name, score):
        # Read existing data
        leaderboard = self.read_leaderboard()

        # Add new score
        leaderboard.append([name, str(score)])

        # Sort by score ascending (lowest score first)
        leaderboard.sort(key=lambda x: int(x[1]), reverse=False)

        # Optionally keep only top N entries (e.g., top 10)
        leaderboard = leaderboard[:10]

        # Write updated leaderboard back to file
        with open(self.file_path, 'w') as file:
            for entry in leaderboard:
                file.write(','.join(entry) + '\n')
            file.flush()  # Ensure everything is written