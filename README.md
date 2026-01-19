This project is a grocery price comparator that will show where the most price friendly products are located
The goal is to develop it to fetch item prices directly from stores in your area local stores (ex. as maxi, provigo, metro)
It would fetch the information from the websites and display them to be readily available for the users

Phase 1:
Load product data from JSON files 
Validate and normalize using Pydantic
Compare store prices per product
Print a readable report and results exported to a CSV file

To run phase 1:
Run:
py requirements.txt
py main.py --demo-json
------------------
Phase 2: 
Replace JSON files with real store APIs
Store location (postal code -> shows nearby store branches)
PostgreSQL to persist prices 

To run phase 2:
Run:
py requirements.txt
py main.py --postal-code "H4E 4N5"


Phase 3:
WEB UI

