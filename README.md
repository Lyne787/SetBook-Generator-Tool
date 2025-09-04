# SetBook Generator Tool

## Purpose
This tool generates SetBooks (PDFs) linking selected green patents to UN Sustainable Development Goals (SDGs). Each SetBook includes the chosen patent, SDG, audience, and type.

## Included Files
- setbook_generator.py  → Python script to generate SetBooks
- patents.json          → List of 20 patents
- sdgs.json             → List of 17 SDGs
- Sample PDFs           → Example SetBooks generated from different combinations

## How to Run
1. Make sure Python 3.13 is installed.
2. Install dependencies: 
   ```
   pip install fpdf2
   ```
3. Place all files in the same folder.
4. Run the script: 
   ```
   python setbook_generator.py
   ```
5. Follow prompts to select:
   - Patent (choose 1 of 20)
   - SDG (choose 1 of 17)
   - Audience (C = Children/Young, Y = Adult)
   - Type (A, Ba, Bb, C)
6. PDF will be automatically generated in the same folder.

## Features
- Select any of 20 patents.
- Select any of 17 SDGs.
- Choose audience and type.
- Automatic PDF generation with structured SetBook.
- Output saved in the same folder.

## URL
https://github.com/Lyne787/SetBook-Generator-Tool