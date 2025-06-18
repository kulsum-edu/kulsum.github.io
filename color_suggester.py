def get_outfit_colors(skin_tone, event_type):
    skin_tone = skin_tone.strip().lower()
    event_type = event_type.strip().lower()

    color_rules = {
        ("fair porcelain", "wedding"): ["Silver"],
        ("fair porcelain", "party"): ["Emerald Green"],
        ("fair porcelain", "formal"): ["Plum"],
        ("fair porcelain", "casual"): ["Powder Blue"],
        ("tan cool", "wedding"): ["Merlot"],
        ("tan cool", "party"): ["Wine Purple"],
        ("tan cool", "formal"): ["Slate Gray"],
        ("tan cool", "casual"): ["Camel"],
        ("deep cool", "wedding"): ["Royal Blue"],
        ("deep cool", "party"): ["Deep Magenta"],
        ("deep cool", "formal"): ["Cool Silver"],
        ("deep cool", "casual"): ["Charcoal Black"]
    }

    return color_rules.get((skin_tone, event_type), ["No suggestion found"])
