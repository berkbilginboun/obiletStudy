import json

captions = {
    "1": "A modern hotel room featuring two single beds with mustard-colored throws, a large window with sheer curtains, a wall-mounted flat-screen TV, a desk with a chair, and neutral-toned decor.",
    "2": "A spacious hotel room with a large double bed, white linens, a glass door opening to a balcony with chairs, offering a scenic sea view. The room includes a wall-mounted TV and minimalist decor.",
    "3": "A cozy hotel room featuring a queen-sized bed with white linens, a wooden headboard, a small bedside table with a lamp, a wall-mounted flat-screen TV, and a large window with city views. The room features a balcony, air conditioning unit above the bed, and a wide city view from the window.",
    "4": "A modern hotel room with one double bed, a corner L-shaped sofa, and a glass shower cabin located directly next to the bed. The room features wooden flooring, warm lighting, and a compact layout.",
    "5": "A small, budget-friendly hotel room with a single bed, simple white linens, a compact wardrobe, a wall-mounted mirror, and minimal decor. The room appears practical and designed for solo travelers.",
    "6": "A dormitory-style room with four single beds arranged symmetrically, each with white linens. The room includes two small desks with two chairs each, suitable for studying or working. The overall layout and simplicity suggest a budget-friendly, student-style accommodation.",
    "7": "A spacious, family-style hotel room featuring one double bed and two single beds. The room includes a balcony with outdoor seating, allowing natural light and fresh air. Its layout is ideal for families or groups of up to four people.",
    "8": "A hotel room designed for families or small groups, featuring one double bed and two single beds. The room includes a small table with chairs and a large window with a city view. Also includes a small balcony, air conditioning, and overlooks the city.",
    "9": "A family-style hotel room with two separate sleeping areas: one features a double bed suitable for two people, and the other contains two single beds. Equipped with a small French-style balcony, air conditioning, and city view from both sleeping areas.",
    "10": "A small, budget-friendly hotel room with two single beds, a compact work desk with a chair, a wall-mounted TV, and an air conditioner above the beds. The room is minimally decorated and optimized for two-person occupancy.",
    "11": "A simple hotel room with two single beds placed side by side, minimal decoration, and a small armchair. The room appears clean and practical, ideal for two people.",
    "12": "A small and cozy hotel room with a single bed, a wall-mounted TV, and a compact armchair. The room includes a small desk and chair placed under a mirror. Decor is minimal, and the space is designed for solo occupancy.",
    "13": "A charming triple room decorated in light tones, featuring one double bed and two single beds, making it suitable for families or small groups. The room includes a small round table with two chairs, a flat-screen TV, and a large window offering a clear sea view. A small desk with a chair is also available for work or study, enhancing the functionality of the space.",
    "14": "A cozy attic-style triple room with wooden interior decor, featuring one double bed and two single beds, suitable for up to three guests. The room includes a flat-screen TV, a compact desk with a chair near the window, and an armchair. A glass door leads to a small private balcony. The warm design and layout suggest a romantic or relaxing stay that also supports functionality with a dedicated workspace.",
    "15": "An elegant and romantic hotel room ideal for honeymooners, featuring a large double bed, a private in-room jacuzzi, and a wide glass wall with sliding doors offering a panoramic sea view. The room includes a work desk, a flat-screen TV, and stylish decor with a luxurious feel. Although there is no balcony, the full-height windows create an open and airy atmosphere, with an extra single bed for a third guest."
}


with open("captions.json", "w") as f:
    json.dump(captions, f, indent=4)