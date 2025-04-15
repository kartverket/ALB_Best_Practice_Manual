import requests
import json

# Fetch the data from the API
url = "https://hoydedata.no/laserservices/rest/projectMetadata.ashx?request={Filter:%22Type=%274%27%22,ReturnMetadata:true}"
response = requests.get(url)
data = response.json()

# Prepare Markdown table header
md_lines = [
    "| LAS_PROJECT_NAME | AARSTALL | LEVERANDOR | OPPDRAGSGIVER |",
    "|------------------|----------|-------------|----------------|"
]

# Loop through the features and extract required fields
for feature in data.get("ProjectMetadata", []):
    props = feature["properties"]
    name = props.get("LAS_PROJECT_NAME", "").replace("|", "&#124;")  # Escape pipes if any
    year = props.get("AARSTALL", "")
    provider = props.get("LEVERANDOR", "")
    client = props.get("OPPDRAGSGIVER", "")
    project_id = props.get("LAS_PROJECT_ID", "")

    link = f"[{name}](https://hoydedata.no/laserinnsyn2?id={project_id})"
    md_lines.append(f"| {link} | {year} | {provider} | {client} |")

# Save to markdown file
with open("laser_projects.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("Markdown file 'laser_projects.md' has been created.")
