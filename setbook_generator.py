import json
from fpdf import FPDF

# -------------------------------
# Load patents and SDGs
# -------------------------------
with open("patents.json", "r", encoding="utf-8") as f:
    patents = json.load(f)

with open("sdgs.json", "r", encoding="utf-8") as f:
    sdgs = json.load(f)

# -------------------------------
# Step 1: Select Patent
# -------------------------------
print("Select a patent:")
for i, patent in enumerate(patents, 1):
    print(f"{i}. {patent['code']} - {patent['title']}")

patent_choice = int(input("\nEnter the number of your chosen patent: ")) - 1
selected_patent = patents[patent_choice]

# -------------------------------
# Step 2: Select SDG
# -------------------------------
print("\nSelect an SDG:")
for sdg in sdgs:
    print(f"{sdg['number']}. {sdg['title']}")

sdg_choice = int(input("\nEnter the SDG number: "))
selected_sdg = next(s for s in sdgs if s["number"] == sdg_choice)

# -------------------------------
# Step 3: Select Audience
# -------------------------------
audience = input("\nEnter audience (C=Children, A=Adult, M=Manager, G=General): ").upper()

# -------------------------------
# Step 4: Generate SetBook PDF
# -------------------------------
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)

# Title
pdf.cell(0, 10, f"{selected_patent['code']} - {selected_patent['title']}", ln=True)
pdf.ln(5)

# SDG Section
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 8, f"SDG {selected_sdg['number']}: {selected_sdg['title']}\n\nDescription: {selected_sdg['description']}")
pdf.ln(5)

# Tailor content per audience
intro_text = {
    "C": f"This SetBook explains the patent '{selected_patent['title']}' in a simple way for children, showing how it helps achieve {selected_sdg['title']}.",
    "A": f"This SetBook provides adults with detailed understanding of '{selected_patent['title']}' and its impact on {selected_sdg['title']}.",
    "M": f"This SetBook is designed for managers to understand strategic applications of '{selected_patent['title']}' for achieving {selected_sdg['title']}.",
    "G": f"This SetBook gives a general audience insight into '{selected_patent['title']}' and how it contributes to {selected_sdg['title']}."
}

pdf.multi_cell(0, 8, f"Introduction:\n{intro_text.get(audience, intro_text['G'])}\n\n")

# Chapters
pdf.multi_cell(0, 8, "Chapters:\n1. Overview\n2. Application\n3. Benefits\n\n")

# Detailed info
pdf.multi_cell(0, 8, f"Applications:\n{selected_patent.get('application','Application details not available.')}\n\n")
pdf.multi_cell(0, 8, f"Benefits:\n{selected_patent.get('benefits','Benefit details not available.')}\n\n")

# Conclusion
pdf.multi_cell(0, 8, f"Conclusion:\n'{selected_patent['title']}' is a significant contribution to the SDG '{selected_sdg['title']}' and has impactful applications for the audience '{audience}'.\n")

# Save PDF
pdf_filename = f"{selected_patent['code']}_{selected_sdg['number']}_{audience}_Virtuous Industry.pdf"
pdf.output(pdf_filename)
print(f"\nSetBook generated: {pdf_filename}")