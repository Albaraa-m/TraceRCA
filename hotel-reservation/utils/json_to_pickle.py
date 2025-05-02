import argparse
import json
import pickle
from pathlib import Path


def convert_json_to_pickle(json_file_path, output_pickle_path):
    """Convert Hotel Reservation JSON traces to TraceRCA pickle format."""
    
    # Read JSON file
    with open(json_file_path, 'r') as f:
        traces = json.load(f)
    
    converted_traces = []
    
    for trace in traces:
        # Convert the trace keeping the exact same structure
        # Convert list pairs to tuples for s_t
        s_t_tuples = [tuple(pair) for pair in trace['s_t']]
        
        converted_trace = {
            's_t': s_t_tuples,
            'timestamp': trace['timestamp'],  # Keep as regular list
            'endtime': trace['endtime'],      # Keep as regular list
            'latency': trace['latency'],      # Keep as regular list
            'http_status': [int(status) for status in trace['http_status']],  # Convert strings to ints
            'trace_id': trace['trace_id'],
            'label': bool(trace['label'])
        }
        
        converted_traces.append(converted_trace)

    # Create parent directories if they don't exist
    output_pickle_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save as pickle
    with open(output_pickle_path, 'wb') as f:
        pickle.dump(converted_traces, f)

def convert_directory(input_dir, output_dir):
    """Convert all JSON files in a directory to pickle format."""
    input_path = Path(input_dir).resolve()  # Get absolute path
    output_path = Path(output_dir).resolve()  # Get absolute path
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Reading files from: {input_path}")
    print(f"Writing pickles to: {output_path}")
    
    # Process each JSON file
    for json_file in input_path.glob('*.json'):
        # Create output filename: same name but .pkl extension in output directory
        output_file = output_path / json_file.with_suffix('.pkl').name
        
        print(f"Converting {json_file} to {output_file}")
        convert_json_to_pickle(json_file, output_file)
        print(f"Converted {json_file.name} -> {output_file.name}")

def main():
    parser = argparse.ArgumentParser(description='Convert Hotel Reservation JSON traces to TraceRCA pickle format')
    parser.add_argument('--input-dir', default='../normal', help='Directory containing JSON files')
    parser.add_argument('--output-dir', default='../normal/pkl', help='Directory to write pickle files')
    
    args = parser.parse_args()
    
    convert_directory(args.input_dir, args.output_dir)
    print("All files converted successfully!")

if __name__ == '__main__':
    main()
