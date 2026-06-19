"""
Labeled training data for the note classifier.

Each entry is (text, tag). The text combines title + content since that's
how we'll feed real notes to the model later (more text = more signal for
a model this simple).

Feel free to add more examples — for a TF-IDF + LogisticRegression model,
more examples per category (even just 10-20 more) noticeably improves it.
"""

TRAINING_DATA = [
    # work
    ("Code new UI Code new UI for Dashboard application", "work"),
    ("Review PR Review pull request from teammate for the auth module", "work"),
    ("Sprint planning Prepare backlog items for next sprint planning meeting", "work"),
    ("Fix bug Investigate and fix the null pointer exception in the payment service", "work"),
    ("Write docs Write API documentation for the new notes endpoint", "work"),
    ("Standup notes Update team on yesterday's progress during daily standup", "work"),

    # personal
    ("Buy groceries Buy milk, eggs, bread, and coffee from the supermarket", "personal"),
    ("Gym session Leg day workout at the gym, focus on squats", "personal"),
    ("Call mom Call mom to check in and plan weekend visit", "personal"),
    ("Book dentist Schedule a dentist appointment for next month", "personal"),
    ("Clean apartment Vacuum living room and do the laundry this weekend", "personal"),
    ("Plan trip Look up flights and hotels for the trip to Japan", "personal"),

    # idea
    ("App idea Build an app that tracks reading habits and suggests books", "idea"),
    ("Blog post idea Write a blog post about deploying FastAPI without Docker", "idea"),
    ("Side project Idea: a tool that auto-tags notes using a small ML model", "idea"),
    ("Startup concept What if there was a marketplace for unused gym memberships", "idea"),
    ("Feature idea Maybe add dark mode toggle to the dashboard app", "idea"),

    # urgent
    ("Server down Production server is down, needs immediate attention", "urgent"),
    ("Client deadline Client needs the report by end of day, top priority", "urgent"),
    ("Security issue Critical security vulnerability found, patch immediately", "urgent"),
    ("Payment failing Payment gateway is failing for all users right now", "urgent"),
    ("Urgent fix Database connection pool exhausted, fix before it crashes again", "urgent"),
]
