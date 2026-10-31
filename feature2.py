import matplotlib.pyplot as plt
from data_loader import DataLoader


class Feature2Analysis:

    def __init__(self):
        self.data_collection = DataLoader().get_issues()

    def trend_analysis(self):
        monthly_counts = {}

        # Count issues by their creation month
        for issue in self.data_collection:
            if issue.created_date is not None:
                month = issue.created_date.strftime('%Y-%m')

                if month not in monthly_counts:
                    monthly_counts[month] = 0

                monthly_counts[month] += 1

        if not monthly_counts:
            print("No issue creation dates available.")
            return

        #TODO: arrange months chronologically
        months = sorted(monthly_counts.keys())
        counts = [monthly_counts[month] for month in months]

        #TODO: creates the trend chart
        plt.figure(figsize=(14, 6))
        plt.plot(months, counts, marker='o', linestyle='dotted')

        plt.title('Issue Creation Trend')
        plt.xlabel('Month')
        plt.ylabel('Number of Issues Created')
        plt.xticks(range(0, len(months), 6), months[::6], rotation=45)

        plt.tight_layout()
        plt.show()

    def run(self):
        self.trend_analysis()
