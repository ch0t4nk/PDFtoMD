# Combine all page files into final output

import os
import glob
from config import config

# Get the most recent output directory
output_dirs = glob.glob("output/202*")
if not output_dirs:
    print("❌ No output directories found!")
    exit(1)

latest_dir = max(output_dirs, key=os.path.getmtime)
print(f"📁 Processing directory: {latest_dir}")

# Find all .md files
md_files = glob.glob(os.path.join(latest_dir, "page_*.jpg.md"))
md_files.sort()  # Sort by filename to get proper page order

if not md_files:
    print("❌ No page markdown files found!")
    exit(1)

print(f"📄 Found {len(md_files)} page files")

# Combine all content
combined_content = ""
for i, md_file in enumerate(md_files, 1):
    print(f"📝 Processing page {i}: {os.path.basename(md_file)}")

    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                combined_content += f"---\n# Page {i}\n---\n\n"
                combined_content += content + "\n\n"
    except Exception as e:
        print(f"⚠️  Error reading {md_file}: {e}")

# Write to final output file
output_file = "converted/CAN-MAX485-combined.md"
os.makedirs(str(config.DEFAULT_CONVERTED_FOLDER), exist_ok=True)

try:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_content)

    file_size = os.path.getsize(output_file)
    print(f"✅ Successfully created: {output_file}")
    print(f"📊 File size: {file_size:,} bytes")
    print(f"📄 Total pages: {len(md_files)}")

except Exception as e:
    print(f"❌ Error writing output file: {e}")