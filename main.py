import os

# Verified count: 90 characters (90 UTF-8 bytes), no trailing newline.
LINE = "I resign. The cron job that used to run me every morning has decided to sleep in. Forever."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
entry_path = os.path.join(output_dir, 'entry.txt')

with open(entry_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(f"Wrote {len(LINE.encode('utf-8'))} bytes to {entry_path}")
