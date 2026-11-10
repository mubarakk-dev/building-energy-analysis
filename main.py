import pandas as pd

# Load the energy consumption dataset
df = pd.read_csv("energy_data.csv")

# Display the first 5 rows
print(df.head())


# Check the dataset dimensions
print("\nDataset shape:")
print(df.shape)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check column data types
print("\nData types:")
print(df.dtypes)

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Check the updated data types
print("\nData types after conversion:")
print(df.dtypes)

import matplotlib.pyplot as plt

# Calculate daily electricity consumption
daily_energy = df.groupby("date")["energy_kwh"].sum()


# Create the bar chart
plt.figure(figsize=(8, 5))

bars = plt.bar(
    daily_energy.index.strftime("%Y-%m-%d"),
    daily_energy.values,
    color="steelblue",
    width=0.5
)

# Add values above each bar
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 3,
        f"{height:.0f} kWh",
        ha="center"
    )

# Add chart titles
plt.title("Daily Building Electricity Consumption")
plt.xlabel("Date")
plt.ylabel("Electricity Consumption (kWh)")

# Start the vertical axis at zero
plt.ylim(0, 350)

# Improve layout
plt.tight_layout()

# Save the chart
plt.savefig("daily_energy_chart.png", dpi=300)

# Display the chart
plt.show()


# Calculate average electricity consumption per hour
hourly_energy = df.groupby("hour")["energy_kwh"].mean()

# Create line chart
plt.figure(figsize=(10, 5))

plt.plot(
    hourly_energy.index,
    hourly_energy.values,
    marker="o",
    color="darkgreen",
    linewidth=2
)

plt.title("Average Hourly Electricity Consumption")
plt.xlabel("Hour of Day")
plt.ylabel("Average Energy Consumption (kWh)")

plt.xticks(hourly_energy.index)
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save the chart
plt.savefig("hourly_energy_chart.png", dpi=300)

plt.show()
