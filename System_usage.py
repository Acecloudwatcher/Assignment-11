import matplotlib.pyplot as plt
import pandas as pd

# CPU usage data over an 8-hour shift
hours = [1, 2, 3, 4, 5, 6, 7, 8]
usage = [25, 30, 83, 85, 40, 38, 73, 30]

# Create a pandas DataFrame
df = pd.DataFrame({"Hour": hours, "Usage (%)": usage})

# Print statistical breakdown
print("CPU Usage Statistical Breakdown")
print("--------------------------------")
print("Mean Usage   :", df["Usage (%)"].mean())
print("Median Usage :", df["Usage (%)"].median())
print("Std Deviation:", round(df["Usage (%)"].std(), 2))
print("Min Usage    :", df["Usage (%)"].min())
print("Max Usage    :", df["Usage (%)"].max())
print("--------------------------------")

# --- Bar Chart ---
plt.figure(figsize=(6, 5))
plt.bar(df["Hour"], df["Usage (%)"], color="skyblue")
plt.title("Hourly CPU Usage Report")
plt.xlabel("Hour")
plt.ylabel("Usage (%)")
plt.xticks(df["Hour"])
plt.tight_layout()
plt.savefig("system_usage_bar.png")
plt.show()

# --- Line Graph ---
plt.figure(figsize=(6, 5))
plt.plot(df["Hour"], df["Usage (%)"], color="skyblue")
plt.title("Hourly CPU Usage Report")
plt.xlabel("Hour")
plt.ylabel("Usage (%)")
plt.xticks(df["Hour"])
plt.tight_layout()
plt.savefig("system_usage_line.png")
plt.show()
