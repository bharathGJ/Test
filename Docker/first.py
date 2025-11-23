import subprocess

commands = [
    "git add .",
    "git commit -m \"\"",
    "git push origin main"
]

for cmd in commands:
    subprocess.run(cmd, shell=True)
