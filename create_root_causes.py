import pickle
from pathlib import Path

# Define test cases and their root causes with full service names
test_cases = {
    'basic_abort_1011': ['ts-basic-service'],
    'basic_abort_1015': ['ts-basic-service'],
    'basic_abort_1023': ['ts-basic-service'],
    'basic_cpu_1012': ['ts-basic-service'],
    'basic_cpu_1016': ['ts-basic-service'],
    'basic_delay_1025': ['ts-basic-service']
}

# Create root causes directory
root_causes_dir = Path('tracerca-exp/data/root_causes')
root_causes_dir.mkdir(exist_ok=True)

# Create root cause files
for test_case, service in test_cases.items():
    filepath = root_causes_dir / f'{test_case}.pkl'
    root_cause = [service]  # Single list with full service name
    print(f"Creating {filepath} with root cause {root_cause}")
    with open(filepath, 'wb') as f:
        pickle.dump(root_cause, f)

print("\nCreated root cause files:")
for file in root_causes_dir.glob('*.pkl'):
    print(f"- {file.name}")