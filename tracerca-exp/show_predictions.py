import pickle
from pathlib import Path
import pandas as pd

def load_prediction(file_path):
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except:
        return None

def load_ground_truth(file_path):
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except:
        return None

def main():
    # Directories
    output_dir = Path('output')
    rc_dir = output_dir / 'trainticket_root_cause_localization'
    ground_truth_dir = Path('data/root_causes')
    
    # Get all result files
    result_files = list(rc_dir.glob('basic_*.result.pkl'))
    
    print("\nRoot Cause Analysis Results:")
    print("-" * 80)
    print(f"{'Test Case':<20} {'Predicted Root Causes':<40} {'Ground Truth':<20}")
    print("-" * 80)
    
    for result_file in sorted(result_files):
        test_case = result_file.stem.replace('.result', '')
        
        # Load prediction
        pred = load_prediction(result_file)
        if pred is None:
            continue
            
        # Load ground truth
        gt_file = ground_truth_dir / f"{test_case}.pkl"
        ground_truth = load_ground_truth(gt_file)
        
        # Get top 3 predictions (assuming predictions are sorted by confidence)
        top_preds = pred[:3] if isinstance(pred, list) else [str(pred)]
        pred_str = ', '.join(str(p) for p in top_preds)
        
        gt_str = ', '.join(ground_truth) if isinstance(ground_truth, list) else str(ground_truth)
        
        print(f"{test_case:<20} {pred_str:<40} {gt_str:<20}")
    
    # Also show anomaly detection results
    print("\nAnomaly Detection Results:")
    print("-" * 80)
    
    ad_results = pd.read_csv('output/trainticket.anomaly_detection.result.csv.0.0.1.3')
    
    # Filter for 'Ours' method and group by test case
    ours_results = ad_results[ad_results['method'] == 'Ours'].groupby('name').first()
    
    print(f"{'Test Case':<20} {'F1-Score':<10} {'Precision':<10} {'Recall':<10}")
    print("-" * 80)
    
    for name, row in ours_results.iterrows():
        print(f"{name:<20} {row['F1-score']:<10.2f} {row['Precision']:<10.2f} {row['Recall']:<10.2f}")

if __name__ == "__main__":
    main()