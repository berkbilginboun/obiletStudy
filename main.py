import json
import csv

# Load captions from JSON
with open("captions.json", "r") as f:
    captions = json.load(f)


# Generate image URL from ID
def image_url(img_id):
    return f"https://s3.eu-central-1.amazonaws.com/static.obilet.com/CaseStudy/HotelImages/{img_id}.jpg"


# Flexible keyword matching (AND between groups, OR within a group), with min required matches
def contains_keywords(caption, keyword_groups, min_match=2):
    caption_lower = caption.lower()
    match_count = 0
    for group in keyword_groups:
        if any(keyword.lower() in caption_lower for keyword in group):
            match_count += 1
    return match_count >= min_match


# Filter captions with given threshold
def filter_by_query(keyword_groups, min_match=2):
    matched_images = []
    for img_id, caption in captions.items():
        if contains_keywords(caption, keyword_groups, min_match):
            matched_images.append({
                "image_id": img_id,
                "url": image_url(img_id),
                "caption": caption
            })
    return matched_images


# Define flexible keyword groups and required match count for each query
queries = {
    1: ([["double"], ["sea view"]], 2),
    2: ([["balcony"], ["air conditioning"], ["city view"]], 3),
    3: ([["triple", "three beds", "3 beds","three guests", "up to three"],["desk", "work desk"]], 2),
    4: ([["4 people", "four people", "family", "group of 4"]], 1)
}

# Descriptions for CSV output
query_descriptions = {
    1: "Double rooms with a sea view",
    2: "Rooms with a balcony and air conditioning, with a city view",
    3: "Triple rooms with a desk",
    4: "Rooms with a maximum capacity of 4 people"
}

# Run filters and collect results
results = {}
for query_id, (keyword_groups, min_match) in queries.items():
    results[query_id] = filter_by_query(keyword_groups, min_match)

# Export results to CSV
with open("query_results.csv", "w", newline="") as csvfile:
    fieldnames = ["Query #", "Query Description", "Image #", "URL"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for query_num, matches in results.items():
        for match in matches:
            writer.writerow({
                "Query #": query_num,
                "Query Description": query_descriptions[query_num],
                "Image #": match["image_id"],
                "URL": match["url"]
            })

print("CSV file 'query_results.csv' created successfully.")