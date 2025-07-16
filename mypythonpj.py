# mypythonpj.py

# Define the HTML content as a string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>My Resume</title>
<style>
    body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4; }
    .container { max-width: 800px; margin: auto; background: #fff; padding: 20px; border-radius: 10px; }
    h1 { text-align: center; color: #333; }
    h2 { color: #555; border-bottom: 2px solid #eee; padding-bottom: 5px; }
    .section { margin-bottom: 20px; }
    .item { margin-bottom: 10px; }
    .title { font-weight: bold; }
    .subtitle { font-style: italic; color: #777; }
</style>
</head>
<body>
<div class="container">
    <h1>Your Name</h1>
    <div class="section">
        <h2>Contact</h2>
        <div class="item">Email: your.email@example.com</div>
        <div class="item">Phone: +123 456 7890</div>
        <div class="item">LinkedIn: linkedin.com/in/yourname</div>
    </div>
    <div class="section">
        <h2>Education</h2>
        <div class="item">
            <div class="title">Degree Name</div>
            <div class="subtitle">Institution, Year</div>
        </div>
    </div>
    <div class="section">
        <h2>Experience</h2>
        <div class="item">
            <div class="title">Job Title</div>
            <div class="subtitle">Company, Duration</div>
            <p>Describe your responsibilities and achievements here.</p>
        </div>
    </div>
    <!-- Add more sections as needed -->
</div>
</body>
</html>
"""

# Save the HTML content to a file
with open("resume.html", "w") as file:
    file.write(html_content)

print("Resume generated successfully! Open 'resume.html' in your browser.")