import os
import datetime
import random
import time

# Function to make a commit
def make_commit():
    file_path = "log.txt"

    # Modify the log file (creating a new line)
    with open(file_path, "a") as f:
        f.write(f"Commit on {datetime.datetime.now()}\n")

    # Run Git commands
    os.system("git add .")
    os.system(f'git commit -m "Automated commit at {datetime.datetime.now()}"')

# Number of commits per day (Change as needed)
commits_per_day = random.randint(3, 7)

for _ in range(commits_per_day):
    make_commit()
    
    # Wait for a random time (between 1 to 3 hours)
    wait_time = random.randint(3600, 10800)
    print(f"Waiting {wait_time // 60} minutes for next commit...")
    time.sleep(wait_time)

# Push changes once at the end of the day
os.system("git push origin main")
print("✅ All commits pushed successfully!")