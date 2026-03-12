import subprocess

print("Starting trend data collection...")

subprocess.run(["python", "scrapers/reddit_scraper.py"])
subprocess.run(["python", "scrapers/hackernews_scraper.py"])
subprocess.run(["python", "scrapers/google_trends_scraper.py"])

print("All scrapers finished.")
