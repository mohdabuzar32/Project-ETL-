"""
run_pipeline.py
Master execution script for Bluestock Mutual Fund ETL Pipeline.
Usage: python run_pipeline.py
"""

import subprocess
import sys
import time

def run_step(script_name, step_num, description):
    """Run a single pipeline step."""
    print(f"\n{'='*50}")
    print(f"  STEP {step_num}: {description}")
    print(f"{'='*50}")
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f" Step {step_num} completed!")
        if result.stdout:
            print(result.stdout)
    else:
        print(f" Step {step_num} failed!")
        print(result.stderr)
        return False
    return True

def main():
    """Main pipeline orchestrator."""
    print("\n Bluestock MF Analytics Pipeline Starting...")
    print(f"   Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    steps = [
        ("data_ingestion.py", 1, "Data Ingestion — Fetching NAV data"),
        ("clean_data.py",     2, "Data Cleaning — Transform & merge"),
        ("recommender.py",    3, "Recommendation Engine — Fund scores"),
    ]
    for script, num, desc in steps:
        success = run_step(script, num, desc)
        if not success:
            print(f"\n Pipeline stopped at Step {num}.")
            sys.exit(1)
    print("\n PIPELINE COMPLETE!")

if __name__ == "__main__":
    main()