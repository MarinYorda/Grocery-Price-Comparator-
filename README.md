# Grocery Price Comparator

This project is a grocery price comparator that shows where the most price-friendly products are located.

The goal is to fetch item prices directly from local grocery stores  
(e.g. Maxi, Provigo, Metro) and present them in a clean, comparable format.

---

## Phase 1 — Demo (JSON-based)

**Features**
- Load product data from JSON files
- Validate and normalize data using Pydantic
- Compare store prices per product
- Print a readable comparison report
- Export results to a CSV file

### How to Run Phase 1 (Demo mode)
pip install -r requirements.txt
py main.py --demo-json

## How to Run Phase 2
pip install -r requirements.txt
py main.py --demo-json
# or
py main.py --postal-code "H4E 4N5"



