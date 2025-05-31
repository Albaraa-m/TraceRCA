import json
from datetime import datetime


def analyze_timestamps(file_path):
    # Read the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Initialize variables to track first and last timestamps
    first_timestamp = float('inf')
    last_timestamp = float('-inf')
    
    # Iterate through all entries
    for entry in data:
        # Get all timestamps from the current entry
        timestamps = entry.get('timestamp', [])
        
        # Update first and last timestamps if needed
        if timestamps:
            first_timestamp = min(first_timestamp, min(timestamps))
            last_timestamp = max(last_timestamp, max(timestamps))
    
    # Calculate delta in minutes
    delta_seconds = last_timestamp - first_timestamp
    delta_minutes = delta_seconds / 60
    
    # Convert timestamps to readable format
    first_time = datetime.fromtimestamp(first_timestamp)
    last_time = datetime.fromtimestamp(last_timestamp)
    
    print(f"First timestamp: {first_time}")
    print(f"Last timestamp: {last_time}")
    print(f"Delta in minutes: {delta_minutes:.2f}")

if __name__ == "__main__":
    file_path = "hotel-reservation/abnormal/frontend.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1748393560.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1748448306.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1748448894.json"
    file_path = "hotel-reservation/normal/aggregated_traces_1748448894.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1744578448.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1744698212.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1744579974.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1748393051.json"
    file_path = "hotel-reservation/abnormal/search.json"

    ## OLD
    file_path = "hotel-reservation/normal/old/aggregated_traces_1744698212.json"
    # file_path = "hotel-reservation/normal/old/aggregated_traces_1744578448.json"
    # file_path = "hotel-reservation/normal/old/aggregated_traces_1744697651.json"
    # file_path = "hotel-reservation/normal/old/aggregated_traces_1744579974.json"


    # #NEW 
    # file_path = "hotel-reservation/normal/aggregated_traces_1748393051.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1748393560.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1748448306.json"
    # file_path = "hotel-reservation/normal/aggregated_traces_1748448894.json"
    
    # file_path = "hotel-reservation/normal/aggregated_traces_1748448894.json"
    file_path = "hotel-reservation/normal/two_mins.json"
    
    analyze_timestamps(file_path) 