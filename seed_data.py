"""
Seeds the running API with sample notes across 4 categories:
work, personal, idea, urgent.

This isn't just filler data — these notes (plus their category, which
you'll add manually as the `tag`) become your training set in Phase 2.

Usage:
    1. Make sure the API is running: uvicorn app.main:app --reload
    2. In another terminal: python seed_data.py
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

notes = [
    # work
    {"title": "Code new UI", "content": "Code new UI for Dashboard application"},
    {"title": "Review PR", "content": "Review pull request from teammate for the auth module"},
    {"title": "Sprint planning", "content": "Prepare backlog items for next sprint planning meeting"},
    {"title": "Fix bug", "content": "Investigate and fix the null pointer exception in the payment service"},
    {"title": "Write docs", "content": "Write API documentation for the new notes endpoint"},
    {"title": "Standup notes", "content": "Update team on yesterday's progress during daily standup"},

    # personal
    {"title": "Buy groceries", "content": "Buy milk, eggs, bread, and coffee from the supermarket"},
    {"title": "Gym session", "content": "Leg day workout at the gym, focus on squats"},
    {"title": "Call mom", "content": "Call mom to check in and plan weekend visit"},
    {"title": "Book dentist", "content": "Schedule a dentist appointment for next month"},
    {"title": "Clean apartment", "content": "Vacuum living room and do the laundry this weekend"},
    {"title": "Plan trip", "content": "Look up flights and hotels for the trip to Japan"},

    # idea
    {"title": "App idea", "content": "Build an app that tracks reading habits and suggests books"},
    {"title": "Blog post idea", "content": "Write a blog post about deploying FastAPI without Docker"},
    {"title": "Side project", "content": "Idea: a tool that auto-tags notes using a small ML model"},
    {"title": "Startup concept", "content": "What if there was a marketplace for unused gym memberships"},
    {"title": "Feature idea", "content": "Maybe add dark mode toggle to the dashboard app"},

    # urgent
    {"title": "Server down", "content": "Production server is down, needs immediate attention"},
    {"title": "Client deadline", "content": "Client needs the report by end of day, top priority"},
    {"title": "Security issue", "content": "Critical security vulnerability found, patch immediately"},
    {"title": "Payment failing", "content": "Payment gateway is failing for all users right now"},
    {"title": "Urgent fix", "content": "Database connection pool exhausted, fix before it crashes again"},
]

for note in notes:
    response = requests.post(f"{BASE_URL}/notes", json=note)
    if response.status_code == 201:
        print(f"Created: {note['title']}")
    else:
        print(f"Failed: {note['title']} -> {response.status_code} {response.text}")