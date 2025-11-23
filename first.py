import subprocess

commands = [
    "git add .",
    "git commit -m \"update from python script\"",
    "git push origin main"
]

for cmd in commands:
    subprocess.run(cmd, shell=True)
