# 🏨 Hotel Image Caption Filtering — AI Internship Case Study

This project was completed as part of the AI internship application at **oBilet**. It focuses on combining human-led image interpretation with programmatic filtering based on natural language descriptions.

---

## 🔍 Problem Overview

You are provided with a set of **15 hotel room images**, each needing to be:

1. Carefully analyzed  
2. Described with a clear and informative **caption**  
3. Filtered programmatically based on **user search queries** such as:
   - `"Double rooms with a sea view"`
   - `"Rooms with a balcony and air conditioning, with a city view"`
   - `"Triple rooms with a desk"`
   - `"Rooms with a maximum capacity of 4 people"`

The final goal is to identify which images satisfy which query, and export the results in a `.csv` format.

---

## 🧠 System Overview

The solution is broken into three core stages:

### 1. **Manual Caption Generation** (`captions.json`)

Each image is manually reviewed by a human (me), and its contents — such as bed types, view, room layout, and furniture — are written into a clear English caption.

Example entry from `captions.json`:

```json
{
  "13": "A charming triple room decorated in light tones, featuring one double bed and two single beds, making it suitable for families or small groups. The room includes a small round table with two chairs, a flat-screen TV, and a large window offering a clear sea view. A small desk with a chair is also available for work or study, enhancing the functionality of the space."
}
```

---

### 2. **Flexible Keyword-Based Filtering** (`main.py`)

The filtering system uses a Python script that:

- Loads all captions from `captions.json`
- Defines queries as **groups of keyword sets**  
  (e.g. `["balcony"]`, `["air conditioning", "ac"]`, `["city view"]`)
- Applies a smart filter that:
  - Uses **AND logic** between keyword groups
  - Uses **OR logic** within each group
  - Supports a **`min_match` threshold** to allow partial matches

#### Example for Query 2:

```python
query = [
  ["balcony"],
  ["air conditioning"],
  ["city view"]
]
min_match = 3
```

A caption will match if **any 3 of the 3 groups** are satisfied.

---

### 3. **Result Export to CSV** (`query_results.csv`)

For each query, the matching image IDs and their corresponding URLs are written into a structured CSV file.

Example output:

```
Query #,Query Description,Image #,URL
1,Double rooms with a sea view,2,https://.../2.jpg
3,Triple rooms with a desk,13,https://.../13.jpg
```

---

## 📁 Project Structure

```
hotel-caption-filtering-case/

   -├── captions.json         # Manually written image captions

   -├── main.py               # Core filtering logic + CSV export

   -├── query_results.csv     # Final output of matched results

   -├── create_json.py        # (Optional) Code to create captions.json

   -└── README.md             # This file
```

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then:

```bash
python main.py
```

This will:

- Load `captions.json`
- Run filtering logic for all 4 queries
- Save matching results to `query_results.csv`

> ✅ No external libraries are required — only `json` and `csv`.

---

## 💡 Key Highlights

- ✅ All image analysis was done **manually** — no AI model was used.
- ✅ Filtering logic is **modular, explainable, and easily adjustable**.
- ✅ Written in clean Python with zero dependencies.
- ✅ Result format is portable and easy to validate (CSV output).

---

## 👤 Author

This project was completed by [Muhammed Berk Bilgin]  
as part of the **oBilet AI Internship Case Study**.

If you have any questions or feedback, feel free to connect via GitHub.
