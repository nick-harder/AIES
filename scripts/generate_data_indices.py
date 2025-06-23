import os
from pathlib import Path

def main():
    # Base project directory
    base = Path(__file__).resolve().parent.parent

    # Lectures to process (7 through 13)
    for num in range(7, 14):
        data_dir = base / f'lecture{num}' / 'data'

        if not data_dir.is_dir():
            print(f"Warning: {data_dir} does not exist. Skipping.")
            continue

        try:
            # Gather all non-index files
            files = sorted(
                f.name for f in data_dir.iterdir()
                if f.is_file() and f.name.lower() != 'index.html'
            )
        except Exception as e:
            print(f"Error reading {data_dir}: {e}")
            continue

        # Build HTML list items
        items = '\n'.join(f'    <li><a href="{fn}">{fn}</a></li>' for fn in files)

        # Compose HTML content
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lecture {num} Data Folder</title>
</head>
<body>
  <h1>Lecture {num} Data Folder</h1>
  <ul>
{items}
  </ul>
</body>
</html>
"""

        # Write to index.html
        try:
            index_file = data_dir / 'index.html'
            index_file.write_text(html, encoding='utf-8')
            print(f'✔ Updated lecture{num}/data/index.html ({len(files)} items)')
        except Exception as e:
            print(f"Error writing to {index_file}: {e}")

if __name__ == '__main__':
    main()
