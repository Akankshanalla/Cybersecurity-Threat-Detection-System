import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("network_traffic.csv")

# Drop non-numeric or identifier columns if needed
df = df.select_dtypes(include=['float64', 'int64'])

# Fill missing values
df.fillna(0, inplace=True)

# Create the Isolation Forest model
iso_forest = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)

# Fit model
iso_forest.fit(df)

# Predict anomalies (-1 = anomaly, 1 = normal)
df['anomaly'] = iso_forest.predict(df)

# Count anomalies
print("Anomaly counts:\n", df['anomaly'].value_counts())

# Visualize anomaly distribution (optional)
sns.histplot(df['anomaly'], kde=False)
plt.title("Anomaly vs Normal Traffic")
plt.xlabel("Anomaly Label (-1 = Anomaly, 1 = Normal)")
plt.ylabel("Count")
plt.show()
