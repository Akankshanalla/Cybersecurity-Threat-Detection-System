# 🛡️ AI-Powered Cybersecurity Threat Detection System

This project uses an unsupervised machine learning approach (Isolation Forest) to detect anomalous network behavior, helping organizations identify potential cyber threats in real-time.

---

## 📌 Features

- Detects network anomalies using the **Isolation Forest algorithm**
- Handles large datasets such as **CICIDS** or **NSL-KDD**
- Visualizes anomaly distribution using **Matplotlib & Seaborn**
- Outputs flagged anomalies into a CSV file
- Easily extendable for real-time log ingestion or web dashboards

---

## 🧠 How It Works

1. Loads and preprocesses network traffic data
2. Trains an Isolation Forest model on normal + anomalous traffic
3. Flags network events with an **anomaly score**
4. Saves results and alerts if suspicious patterns are found

---

## 🛠️ Requirements

```bash
pip install pandas scikit-learn matplotlib seaborn


##vaj
