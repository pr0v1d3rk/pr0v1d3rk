import json, random, datetime, re, pathlib

# Load README
readme_path = pathlib.Path("README.md")
readme = readme_path.read_text()

# Load topics & quotes
topics = json.loads(pathlib.Path("learning.json").read_text())["topics"]
quotes = json.loads(pathlib.Path("quotes.json").read_text())["quotes"]

# Pick one
chosen_topic = random.choice(topics)
chosen_quote = random.choice(quotes)

# Replace LEARNING section
readme = re.sub(
    r"<!--LEARNING-->.*?<!--END_LEARNING-->",
    f"<!--LEARNING-->{chosen_topic}<!--END_LEARNING-->",
    readme,
    flags=re.S,
)

# Replace QUOTE section
readme = re.sub(
    r"<!--QUOTE-->.*?<!--END_QUOTE-->",
    f"<!--QUOTE-->{chosen_quote}<!--END_QUOTE-->",
    readme,
    flags=re.S,
)

# Replace DATE section
today = datetime.date.today().isoformat()
readme = re.sub(
    r"<!--DATE-->.*?<!--END_DATE-->",
    f"<!--DATE-->{today}<!--END_DATE-->",
    readme,
    flags=re.S,
)

# Save README
readme_path.write_text(readme)
