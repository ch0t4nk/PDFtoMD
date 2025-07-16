#!/usr/bin/env python3
"""
Batch Monitor - Automatically check and retrieve batch results when ready
"""

import time
import subprocess
import sys

def monitor_batch(batch_id, check_interval=30):
    """Monitor batch and retrieve when completed"""
    print(f"🔍 Monitoring batch {batch_id}...")
    print(f"⏰ Checking every {check_interval} seconds")
    print("🛑 Press Ctrl+C to stop monitoring")

    try:
        while True:
            print(f"\n⏰ {time.strftime('%H:%M:%S')} - Checking batch status...")

            # Check status
            result = subprocess.run([
                sys.executable, "batch_api.py", "status", batch_id
            ], capture_output=True, text=True)

            if result.returncode == 0:
                output = result.stdout
                print(output.strip())

                # Check if completed
                if "Status: completed" in output:
                    print("\n🎉 Batch completed! Retrieving results...")

                    # Retrieve results
                    retrieve_result = subprocess.run([
                        sys.executable, "batch_api.py", "retrieve", batch_id
                    ], capture_output=True, text=True)

                    if retrieve_result.returncode == 0:
                        print("✅ Results retrieved successfully!")
                        print(retrieve_result.stdout)
                        break
                    else:
                        print("❌ Error retrieving results:")
                        print(retrieve_result.stderr)

                elif "Status: failed" in output:
                    print("❌ Batch failed!")
                    break

            else:
                print("❌ Error checking batch status")
                print(result.stderr)

            # Wait before next check
            print(f"⏳ Waiting {check_interval} seconds before next check...")
            time.sleep(check_interval)

    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monitor_batch.py <batch_id>")
        sys.exit(1)

    batch_id = sys.argv[1]
    monitor_batch(batch_id)
