
# Placeholder for advanced health recommendation engine
def get_recommendations(sleep, screen, stress, water):
    tips = []
    if sleep < 6:
        tips.append("Try to increase sleep to at least 7 hours for optimal rest.")
    if screen > 6:
        tips.append("Reduce screen time to avoid eye strain and fatigue.")
    if stress > 7:
        tips.append("Practice breathing exercises or mindfulness to reduce stress.")
    if water < 1.5:
        tips.append("Drink more water — aim for 2L per day.")
    return tips
