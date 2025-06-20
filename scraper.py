from bs4 import BeautifulSoup

# Open the saved HTML file
with open("our_courses.html", "r", encoding="utf-8") as file:
    html = file.read()

doc = BeautifulSoup(html, 'lxml')


# Use the known selector
courses = doc.select('.heading-60-black.color-black.mb-20')

for course in courses:
    print(course.contents[0].strip())
