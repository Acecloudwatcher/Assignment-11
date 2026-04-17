import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# --- Step 1: Read the CSV file, skipping the comment lines at the top ---
df = pd.read_csv("server_log.csv", comment="#")

# --- Step 2: Drop the Timestamp column, it is not needed for analysis ---
df = df.drop(columns=["Timestamp"])

# --- Step 3: Fill missing (NaN) values with the mean of each column ---
for col in df.columns:
    col_mean = df[col].mean()
    df[col] = df[col].fillna(col_mean)

# --- Step 4: Calculate the mean response time for each service ---
service_means = df.mean()

print("Average Response Times (ms):")
for service, avg in service_means.items():
    print(f"  {service}: {avg:.2f} ms")

# --- Step 5: Plot a pie chart of average response times ---
plt.figure(figsize=(7, 7))
plt.pie(
    service_means,
    labels=service_means.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["skyblue", "lightcoral", "lightgreen", "gold"]
)
plt.title("Distribution of Average Server Response Times")
plt.tight_layout()
plt.savefig("log_analysis_pie.png")
print("Chart saved as log_analysis_pie.png")
