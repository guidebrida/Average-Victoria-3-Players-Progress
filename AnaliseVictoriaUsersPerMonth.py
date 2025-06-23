import matplotlib.pyplot as plt

meses = [
    "Jan 2023", "Feb 2023", "Mar 2023", "Apr 2023", "May 2023", "Jun 2023",
    "Jul 2023", "Aug 2023", "Sep 2023", "Oct 2023", "Nov 2023", "Dec 2023",
    "Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024", "May 2024", "Jun 2024",
    "Jul 2024", "Aug 2024", "Sep 2024", "Oct 2024", "Nov 2024", "Dec 2024",
    "Jan 2025", "Feb 2025", "Mar 2025", "Apr 2025", "May 2025", "Last 30 Days"
]

jogadores_medios = [
    6951.3, 5202.9, 6121.1, 5427.8, 4875.4, 4615.8,
    4807.1, 4414.7, 4627.6, 4778.5, 8530.6, 7986.7,
    6641.4, 5697.8, 6390.9, 5872.7, 6067.9, 7497.4,
    10550.4, 7700.0, 6592.1, 5747.9, 6858.6, 6998.6,
    6438.0, 5477.2, 5234.3, 5649.1, 5577.9, 7576.1
]

plt.figure(figsize=(12, 6))
plt.plot(meses, jogadores_medios, marker='o', color='blue', linewidth=2)
plt.title('Average Victoria 3 Players Progress (From Jan 2023 Onwards)')
plt.xlabel('Month')
plt.ylabel('Average Players')
plt.xticks(rotation=90)
plt.grid(True)

annotations = {
    "May 2023": "1.3 + DLC Voice of the People",
    "Nov 2023": "1.5 Update + DLC Colossus of the South",
    "Jun 2024": "1.7 Update + Sphere of Influence",
    "Nov 2024": "1.8 Update + DLC Pivot of Empire",
    "Last 30 Days": "1.9 Update + Charters of Commerce"

}

for month, text in annotations.items():
    if month in meses:
        idx = meses.index(month)
        plt.annotate(text,
                     xy=(idx, jogadores_medios[idx]),
                     xytext=(idx, jogadores_medios[idx] + 3000),
                     arrowprops=dict(facecolor='red', shrink=0.05),
                     fontsize=9,
                     color='red',
                     ha='center')

plt.tight_layout()

# Save the plot automatically
output_path = r"C:\Users\guilh\Documents\Projetos pessoais\Estudos\PYTHON ANALISE VIC 3\Resultados\average_players_progress.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')


plt.show()
