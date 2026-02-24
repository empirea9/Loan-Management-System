<h1 align="center">Loan Management System – CSV based</h1>

<p align="center">
A **Loan Management System** is a simple Python console application that helps store and manage customer loan records for a bank/financial institution. It keeps borrower details in a **CSV file (`loan.csv`)**, making the data lightweight, portable, and easy to inspect/edit. 

This project supports:
- adding new customer loan records  
- viewing all records  
- searching by Customer ID  
- modifying existing records  
- deleting one record (or all records)  
- calculating loan interest & total repayment (simple interest)

---

## Features (Menu Options)

### 1) Input Record
Add one or more customers to the system. For each customer, the program captures:

- **Customer ID** (unique numeric identifier)
- **Name** (alphabetic words)
- **Loan Amount** (principal)
- **Loan Time** (duration in months)
- **Interest Rate** (percentage)

Records are appended to `loan.csv`.

### 2) Display Records
Prints all stored customer records in a readable format.

If the file contains only headers (no data), it shows:
> `No records found. Please add customer records first.`

### 3) Search Record
Searches for a single customer record by **Customer ID** and displays all details.
If not found:
> `Record Not Found!`

### 4) Modify Record
Updates an existing customer record by **Customer ID**.  
All fields can be changed after validation, and the CSV is rewritten with updated values.

### 5) Delete Record
Deletes:
- a specific record by **Customer ID**, or
- **all records** by entering `all` (case-insensitive)

### 6) Calculate Loan
Calculates **interest amount** and **total repayment** for a given Customer ID using *simple interest*.

The program computes interest using months as time:

- `interest = (principal * rate * time/12) / 100`
- `total_amount = principal + interest`

### 7) Exit
Closes the program gracefully.

---

## Data Storage (CSV Backend)

All records are stored in `loan.csv` with the following header:

- `CUSTOMER ID`
- `NAME`
- `LOAN AMOUNT`
- `LOAN TIME`
- `INTEREST`

---

## Input Validation & Error Handling

The system is designed to fail safely and avoid crashing on invalid input.

### Common validations
- Menu choice must be numeric and within **1–7**
- Customer ID must be numeric (`isdigit()`)
- Name must contain only alphabetic words (`split()` + `isalpha()`)
- Loan Amount & Interest must be valid decimal numbers (`float()` via `is_float()`)
- Loan Time must be numeric (months)

### Empty file protection
Most operations first check whether records exist (beyond the header) before continuing.

---

## Functions Overview

### Built-in / Library Modules Used
- `os`
  - `os.path.exists()` → checks if `loan.csv` exists
  - `os.path.getsize()` → checks if file is empty
- `csv`
  - `csv.reader()` → reads CSV rows
  - `csv.writer()` → writes rows back into CSV

### User-Defined Functions
- `no_records_check()`  
  Detects whether the CSV file has records beyond the header; prevents operations on empty datasets.

- `heading()`  
  Ensures `loan.csv` exists and contains column headers.

- `is_float(value)`  
  Returns `True` if `value` can be converted to float; else `False`.

- `wrong_input()`  
  Standardized invalid input message + pause.

- `data()`  
  Adds customer records after validating all fields.

- `display()`  
  Displays all records.

- `search()`  
  Finds and prints a record by Customer ID.

- `modify()`  
  Updates a record by Customer ID and rewrites the CSV.

- `delete()`  
  Removes a record by Customer ID or clears all records using `all`.

- `calculate_interest()`  
  Retrieves a record and calculates interest + total repayment.

---

## How to Run

### Requirements
- Python 3.x

### Run the program
```bash
python loan_management_system.py
```

> the program will create `loan.csv` if missing

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/empirea9">empirea9</a>
</p>
