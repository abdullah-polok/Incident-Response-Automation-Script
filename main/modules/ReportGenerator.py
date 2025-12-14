"""
This module takes all the collected data and creates a final report.
It produces:

A JSON file (for machines or tools)

A simple HTML file (easy for humans to read)

Why it's useful:
After investigation, security teams need a summary to share with others.
This module puts everything together neatly.

Example real-world use:

Provide a summary of suspicious processes to your instructor

Save investigation results for later review

Share a clean formatted report with a cybersecurity team
"""
import json
from pathlib import Path

class ReportGenerator:
    # This module creates JSON and simple HTML reports.

    def save_json(self, data, out_folder):
        out_folder = Path(out_folder)
        out_folder.mkdir(parents=True, exist_ok=True)

        with open(out_folder / "report.json", "w") as f:
            json.dump(data, f, indent=4)

    def save_html(self, data, out_folder):
        html = "<h1>IRTA Report</h1>"
        for section, content in data.items():
            html += f"<h2>{section}</h2><pre>{content}</pre>"

        with open(Path(out_folder) / "report.html", "w") as f:
            f.write(html)

