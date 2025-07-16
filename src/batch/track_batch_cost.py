#!/usr/bin/env python3
"""
Batch Cost Tracker - Monitor batch progress and calculate exact costs
"""
import time
import json
from .master import PDFBatchMaster

def track_batch_cost():
    master = PDFBatchMaster()
    batch_id = "batch_6876ed3311c88190a4f47b8109ca9cbd"

    print("🔍 BATCH COST TRACKING")
    print("=" * 50)
    print(f"Batch ID: {batch_id}")
    print(f"Baseline Cost (previous batch): $0.4528")
    print(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    while True:
        try:
            # Check status
            batches = master.find_active_batches()
            current_batch = None

            for batch in batches:
                if batch['id'] == batch_id:
                    current_batch = batch
                    break

            if not current_batch:
                print("❌ Batch not found!")
                break

            status = current_batch['status']
            completed = current_batch['completed']
            total = current_batch['total']

            print(f"\n⏰ {time.strftime('%H:%M:%S')} - Status: {status} ({completed}/{total})")

            if status == "completed":
                print("\n🎉 BATCH COMPLETED! Analyzing costs...")

                # Analyze usage
                usage_stats = master.analyze_batch_usage(batch_id)
                if usage_stats:
                    master.print_usage_summary(usage_stats)

                    # Calculate cost difference
                    new_cost = usage_stats['total_cost']
                    old_cost = 0.4528
                    difference = new_cost - old_cost

                    print(f"\n💰 COST COMPARISON")
                    print(f"Previous batch: ${old_cost:.4f}")
                    print(f"New batch: ${new_cost:.4f}")
                    print(f"Difference: ${difference:+.4f} ({difference/old_cost*100:+.1f}%)")

                    if new_cost > old_cost:
                        print(f"📈 Higher cost due to increased max_tokens (8192 vs 4096)")
                    else:
                        print(f"📉 Lower cost - impressive optimization!")

                break
            elif status == "failed":
                print("❌ Batch failed!")
                break
            else:
                # Wait before next check
                time.sleep(30)

        except KeyboardInterrupt:
            print("\n⏹️  Monitoring stopped by user")
            break
        except (RuntimeError, OSError, ValueError) as e:
            print(f"❌ Error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    track_batch_cost()
