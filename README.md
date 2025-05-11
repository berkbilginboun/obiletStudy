# Hotel Image Caption Filtering Case Study

This project was completed as part of an AI internship application at **oBilet**. The task involved analyzing hotel room images, generating human-like captions for each, and programmatically filtering the rooms based on specific user queries.

---

## 🔍 Problem Definition

Given a set of 15 hotel room images, the goal was to:
1. Generate detailed and realistic text descriptions (captions) for each image
2. Filter rooms based on textual content according to 4 user queries:
   - Double rooms with a sea view
   - Rooms with a balcony and air conditioning, with a city view
   - Triple rooms with a desk
   - Rooms with a maximum capacity of 4 people
3. Export matching results into a structured CSV format

---

## 🧠 Solution Approach

- All captions were manually written by analyzing the images carefully.
- A JSON file (`captions.json`) stores these descriptions.
- A Python script (`main.py`) loads these captions, applies flexible keyword-based filtering logic, and outputs the matching image URLs per query.
- Matching results are saved in `query_results.csv`.

The filtering logic uses customizable keyword groups with `min_match` thresholds to handle fuzzy, natural-language descriptions effectively.

---

## 📁 File Structure

hotel_caption_filtering_case/
├── captions.json         # All manually written image captions
├── main.py               # Caption filtering logic + CSV output
├── query_results.csv     # Final output per query
├── create_json.py        # (Optional) Generates captions.json
└── README.md             # This file

---

## ▶️ How to Run

```bash
# Install dependencies (no external libraries required)
python main.py
