import json
import sys
from collections import defaultdict
from typing import Dict, List


def analyze_traces(trace_file: str) -> Dict:
    """
    Analyze the trace file and count various metrics about the requests.
    
    Args:
        trace_file (str): Path to the trace JSON file
        
    Returns:
        Dict: Dictionary containing the analysis results
    """
    # Initialize counters
    total_requests = 0
    status_counts = defaultdict(int)
    service_counts = defaultdict(int)
    
    # Read and parse the JSON file
    with open(trace_file, 'r') as f:
        traces = json.load(f)
    
    # Process each trace
    for trace in traces:
        # Count HTTP status codes
        for status in trace['http_status']:
            status_counts[status] += 1
            total_requests += 1
        
        # Count service interactions
        for service_pair in trace['s_t']:
            source, target = service_pair
            service_counts[source] += 1
            service_counts[target] += 1
    
    # Prepare the results
    results = {
        "total_requests": total_requests,
        "requests_by_status": dict(status_counts),
        "requests_by_service": dict(service_counts),
        "success_rate": (status_counts.get("200", 0) / total_requests * 100) if total_requests > 0 else 0
    }
    
    return results

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_requests.py <trace_file>")
        sys.exit(1)
    
    trace_file = sys.argv[1]
    try:
        results = analyze_traces(trace_file)
        
        # Print results in a readable format
        print("\nTrace Analysis Results:")
        print("-" * 50)
        print(f"Total Requests: {results['total_requests']}")
        print("\nRequests by Status Code:")
        for status, count in results['requests_by_status'].items():
            print(f"  HTTP {status}: {count}")
        
        print("\nRequests by Service:")
        for service, count in results['requests_by_service'].items():
            print(f"  {service}: {count}")
        
        print(f"\nSuccess Rate: {results['success_rate']:.2f}%")
        
    except FileNotFoundError:
        print(f"Error: File {trace_file} not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: {trace_file} is not a valid JSON file")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()