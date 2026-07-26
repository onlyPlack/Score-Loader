import os
import csv

from datetime import timezone, datetime

class ScoreSaver:
    
    def __init__(self, score_file='scores.csv'):#init method
        self.score_file = score_file
        self.score = None

    def upload(self):#user type the score
        name = input('Enter the name: ')
        
        score = input('Enter the score: ')
        time = datetime.now(timezone.utc).strftime('%Y-%m-%d')       
        
        self.score = {'Name': name, 'Score': score, 'Time': time}

    def save_score(self):
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        score_dir = os.path.join(base_path, 'score_data')
        csv_file = os.path.join(score_dir, self.score_file)
        times = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        if not os.path.exists(score_dir):
        
        
            os.makedirs(score_dir)
         
        file_exists = os.path.exists(csv_file)
        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            choice = input('Is it in the same exam result? (yes/no): ').lower()
            
            
            if not file_exists or choice == 'no':  
            
                writer.writerow([times])    
            for name, score in self.score.items():
                writer.writerow([name, score])
            writer.writerow([])  # Add an empty line for separation
saver = ScoreSaver()
print('Here is the score saver program.')
print('What do you want')

print('1) Upload and save a score')

print('2) Exit')

while True:
    choice = input('Enter your choice: ')

    if choice == '1':
        saver.upload()

        saver.save_score()
        print('Score saved successfully.')
        print()

    elif choice == '2':
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please try again.')