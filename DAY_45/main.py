from bs4 import BeautifulSoup


contents = None
with open('./website.html') as file:
    contents = file.read()

# Parse contents of an html page
soup = BeautifulSoup(contents, "html.parser")

# Access Title tag
print(soup.title)

# Access title tag name
print(soup.title.name)

# Access title tag contents
print(soup.title.string)

# Access the FIRST anchor tag
print(soup.a)

# Find all anchor tags
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag_a in all_anchor_tags:
    # Get text of an anchor tag
    print(tag_a.getText())

    # Get an attribute (href) of an anchor tag
    print(tag_a.get("href"))

# Find an element by its attributes
# In this example, we are searching for an H1 tag with id="name"
heading = soup.find(name="h1", id="name")
print(heading)

# In this example, we are searching for an H3 tag with class="heading"
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# Using CSS selectors to find elements
# In this example, we are searching for a specific A tag using a css selector "body p em strong a"
company_url = soup.select_one(selector="body p em strong a")
print(company_url)

# In this example, we are searching for a specific H1 tag with ID="name" using a css selector "#name"
heading_tag = soup.select_one(selector="#name")
print(heading_tag)

# In this example, we are searching for tags that have a class "heading" using a css selector ".heading"
heading_tags = soup.select(selector=".heading")
print(heading_tags)
