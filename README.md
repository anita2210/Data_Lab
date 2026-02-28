# Data Lab - DVC Data Versioning

This repository demonstrates data versioning using **DVC (Data Version Control)** with **Google Cloud Storage (GCS)** as the remote backend, as part of the MLOps course at Northeastern University.

---

## 📌 Objective

Track and version a real-world dataset through multiple preprocessing stages using DVC, while storing large data files remotely on GCS and keeping only lightweight metadata in GitHub.

---

## 📂 Repository Structure

```
Data-Lab/
│   README.md
│   preprocess.py
│   .dvcignore
│
├── .dvc/
│   └── config          # DVC remote configuration
│
└── data/
    └── adult_income.csv.dvc   # DVC metadata file (tracks the dataset)
```

---

## 📊 Dataset

| Property | Detail |
|---|---|
| Name | Adult Income (Census Income) |
| Source | UCI Machine Learning Repository |
| URL | https://archive.ics.uci.edu/dataset/2/adult |
| File | `adult_income.csv` |
| Task | Binary classification — predict if income >50K or ≤50K |

---

## 🔄 Data Versions

### V1 — Raw Dataset
- **Shape:** (32,561 rows × 15 columns)
- **Description:** Original unmodified dataset downloaded from UCI
- **Commit:** `3486882`

### V2 — Cleaned Dataset
- **Shape:** (30,162 rows × 15 columns)
- **Description:** Removed rows with unknown values (`?`) in `workclass`, `occupation`, and `native_country` columns
- **Rows removed:** 2,399

---

## ⚙️ Tools & Technologies

- **DVC** — Data version control
- **Google Cloud Storage** — Remote data storage
- **Git & GitHub** — Code and metadata versioning
- **Python / Pandas** — Data preprocessing

---

## 🚀 How to Reproduce

### 1. Clone the repository
```bash
git clone https://github.com/anita2210/Data_Lab.git
cd Data_Lab
```

### 2. Install dependencies
```bash
pip install dvc[gs] pandas
```

### 3. Configure GCS credentials
```bash
dvc remote modify myremote credentialpath /path/to/your-credentials.json
```

### 4. Pull the dataset
```bash
dvc pull
```

### 5. Run preprocessing
```bash
python preprocess.py
```

---

## 🔁 Switching Between Versions

**Revert to V1 (raw data):**
```bash
git checkout 3486882
dvc checkout
```

**Return to V2 (cleaned data):**
```bash
git checkout main
dvc checkout
```

---

## ⚠️ Notes

- The actual dataset (`adult_income.csv`) is **not stored in GitHub** — it is tracked by DVC and stored in Google Cloud Storage
- The GCS credentials JSON file is excluded via `.gitignore` and should **never** be committed to GitHub