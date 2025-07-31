import pandas as pd
import matplotlib.pyplot as plt

# Example data structure (Replace with real data when running locally)
data = {
    'Player': ['Emma Ward', 'Meaghan Tyrrell', 'Emma Tyrrell'],
    'Goals': [45, 40, 30],
    'Assists': [20, 25, 18],
    'Games': [18, 18, 18]
}

df = pd.DataFrame(data)

# Basic stats
print("Summary Statistics:\n", df.describe())

# Top scorer
top_scorer = df.loc[df['Goals'].idxmax(), 'Player']
print(f"Top Scorer: {top_scorer}")

# Visualization
plt.figure(figsize=(6, 4))
plt.bar(df['Player'], df['Goals'])
plt.title('Goals by Player')
plt.xlabel('Player')
plt.ylabel('Goals')
plt.tight_layout()
plt.savefig('images/goals_chart.png')
