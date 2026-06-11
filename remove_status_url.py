import os, glob
for f in glob.glob('.github/workflows/*.yml'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    new_content = "\n".join([line for line in content.split("\n") if 'STATUS_URL: "${{ env.genurl }}/updategh"' not in line])
    if content != new_content:
        with open(f, 'w', encoding='utf-8', newline='\n') as file:
            file.write(new_content)
