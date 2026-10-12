import json
import pandas as pd

events_json = '''
[
    {"session_id": "S1", "user_id": "U001", "event_type": "page_view", "page": "/home", "timestamp": "2024-01-10 10:00:00"},
    {"session_id": "S1", "user_id": "U001", "event_type": "page_view", "page": "/products", "timestamp": "2024-01-10 10:01:30"},
    {"session_id": "S1", "user_id": "U001", "event_type": "add_to_cart", "page": "/products", "timestamp": "2024-01-10 10:03:00"},
    {"session_id": "S1", "user_id": "U001", "event_type": "page_view", "page": "/checkout", "timestamp": "2024-01-10 10:05:00"},
    {"session_id": "S2", "user_id": "U002", "event_type": "page_view", "page": "/home", "timestamp": "2024-01-10 11:00:00"},
    {"session_id": "S2", "user_id": "U002", "event_type": "page_view", "page": "/about", "timestamp": "2024-01-10 11:00:45"},
    {"session_id": "S3", "user_id": "U003", "event_type": "page_view", "page": "/products", "timestamp": "2024-01-10 12:00:00"},
    {"session_id": "S3", "user_id": "U003", "event_type": "add_to_cart", "page": "/products", "timestamp": "2024-01-10 12:02:00"},
    {"session_id": "S3", "user_id": "U003", "event_type": "purchase", "page": "/checkout", "timestamp": "2024-01-10 12:05:00"}
]
'''

df = pd.DataFrame(json.loads(events_json))
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Events per session
print("Events per session:")
print(df.groupby('session_id').size())

# Session duration
session_duration = df.groupby('session_id')['timestamp'].agg(['min', 'max'])
session_duration['duration_minutes'] = (session_duration['max'] - session_duration['min']).dt.total_seconds() / 60
print("\nSession durations:")
print(session_duration)

# Most viewed pages
print("\nPage popularity:")
print(df[df['event_type'] == 'page_view']['page'].value_counts())

# Conversion rate
converted_sessions = df[df['event_type'] == 'purchase']['session_id'].unique()
total_sessions = df['session_id'].nunique()
conversion_rate = len(converted_sessions) / total_sessions
print(f"\nConversion rate: {conversion_rate:.1%}")