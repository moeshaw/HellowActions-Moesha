import os 

# file to greet a student in GitHub Actions


name = os.getenv(" WHO_TO_GREET", "Grad Students")

print(" Hello GitHub Actions "+ name)
print("This program is running inside Github Actions ")
