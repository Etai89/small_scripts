import os.path
import winsound
import os
import shutil
import settings_file as sf

# Define input and output file paths
input_path = sf.TXT_FILE
output_path = sf.TXT_FILE

# Create output file if it does not exist
if not os.path.exists(output_path):
    open(output_path, 'w').close()

# Read input file, modify text, and write to temporary output file
with open(input_path, 'r') as f:
    text = f.read()
    lines = text.split('\n')
    strings = ['"' + line.strip()[3:].strip() + '",' for line in lines if line.strip()]

with open(output_path, 'w') as f:
    for string in strings:
        f.write(string + '\n')

# Move temporary output file to input file path
shutil.move(output_path, input_path)

# Play a Windows sound when the program finishes running
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
print("done!")
