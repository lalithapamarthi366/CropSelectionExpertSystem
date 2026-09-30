from rules import RULES


def get_recommendation(user_input):

    best_crop = None
    best_score = -1
    best_rule = None
    best_matches = []

    for rule in RULES:

        score = 0
        matches = []

        if user_input["soil"] == rule["soil"]:
            score += 2
            matches.append("Soil")

        if user_input["season"] == rule["season"]:
            score += 2
            matches.append("Season")

        if user_input["water"] == rule["water"]:
            score += 2
            matches.append("Water")

        if user_input["rainfall"] == rule["rainfall"]:
            score += 1
            matches.append("Rainfall")

        if user_input["temperature"] == rule["temperature"]:
            score += 1
            matches.append("Temperature")

        if user_input["irrigation"] == rule["irrigation"]:
            score += 1
            matches.append("Irrigation")

        if user_input["moisture"] == rule["moisture"]:
            score += 1
            matches.append("Soil Moisture")

        if user_input["farm_size"] == rule["farm_size"]:
            score += 1
            matches.append("Farm Size")

        if user_input["previous_crop"] == rule["previous_crop"]:
            score += 1
            matches.append("Previous Crop")

        if user_input["goal"] == rule["goal"]:
            score += 1
            matches.append("Goal")

        if score > best_score:
            best_score = score
            best_crop = rule["crop"]
            best_rule = rule
            best_matches = matches

    # Minimum matching requirement
    if best_score < 6:
        return {
            "crop": "No strong recommendation",
            "score": best_score,
            "rule": None,
            "matches": best_matches
        }

    return {
        "crop": best_crop,
        "score": best_score,
        "rule": best_rule,
        "matches": best_matches
    }