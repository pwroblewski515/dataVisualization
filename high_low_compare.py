import csv
from datetime import datetime

from matplotlib import pyplot as plt

# TODO: Figure out how to display these as different colors on the same plot

# Get the dates, low, and high temperatures from the file
filenames = ['death_valley_2014.csv', 'sitka_weather_2014.csv']

fig = plt.figure(dpi=128, figsize=(10, 6))

for filename in filenames:
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		dates, highs, lows = [], [], []
		for row in reader:
			try:
				current_date = datetime.strptime(row[0], "%Y-%m-%d")
				high = int(row[1])
				low = int(row[3])
			except ValueError:
				print(current_date, 'missing data')

			else:
				dates.append(current_date)
				lows.append(low)
				highs.append(high)

	# plot data
	plt.plot(dates, highs, c='red', alpha=0.5)
	plt.plot(dates, lows, c='blue', alpha=0.5)
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

	# Format plot
	title = "Daily High Temperatures - 2014\nDeath Valley, CA"
	plt.title(title, fontsize=20)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
