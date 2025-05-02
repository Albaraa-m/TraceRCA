import pickle
import re
from pathlib import Path


def extract_service_from_filename(filename):
    # Handle special cases with '+'
    # if '+' in filename:
    #     # For files like 'user+verification-code_cpu_1021.pkl'
    #     # Take all services before the underscore
    #     service = filename.split('_')[0]
    #     return service.split('+')
    
    # # Regular case: service name is everything before first underscore
    # service = filename.split('_')[0]
    # return [service]
    service = filename.split('_')[0]
    return [service]

# Create root causes directory
root_causes_dir = Path('tracerca-exp/data/root_causes')
root_causes_dir.mkdir(exist_ok=True)

# Get all test files
test_dir = Path('tracerca-exp/data/test')
test_files = list(test_dir.glob('*.pkl'))

# Create root cause files for each test case
created_files = {}
for test_file in test_files:
    # Get filename without .pkl
    filename = test_file.stem
    # Extract service name(s)
    services = extract_service_from_filename(filename)
    
    # Create root cause file
    root_cause_path = root_causes_dir / f'{filename}.pkl'
    with open(root_cause_path, 'wb') as f:
        pickle.dump(services, f)
    created_files[filename] = services

# Print summary
print("\nCreated root cause files:")
print("-" * 70)
print(f"{'Test Case':<40} {'Root Cause Service(s)':<30}")
print("-" * 70)
for test_case, services in sorted(created_files.items()):
    print(f"{test_case:<40} {', '.join(services):<30}")

print(f"\nTotal files created: {len(created_files)}")