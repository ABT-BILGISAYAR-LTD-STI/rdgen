import os, glob
for f in glob.glob('.github/workflows/*.yml'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    new_content = content.replace('${{ secrets.GITHUB_TOKEN }}', '${{ secrets.GH_PAT }}')
    if content != new_content:
        with open(f, 'w', encoding='utf-8', newline='\n') as file:
            file.write(new_content)
