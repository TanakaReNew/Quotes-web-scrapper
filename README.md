# Web Scraping Project: Quotes to Scrape

## Overview

This project involves scraping quotes from the website *Quotes to Scrape* using Python. The objective was to extract structured data (quotes, authors, and tags) across multiple pages and store it in a clean, usable format.

---

## Tools and Libraries Used

* **Python**
* **requests** – for sending HTTP requests
* **BeautifulSoup (bs4)** – for parsing HTML
* **csv** – for storing extracted data

---

## Data Extraction Process

1. **Accessing the Website**
   The website uses a predictable URL structure for pagination:

   ```
   https://quotes.toscrape.com/page/{}/
   ```

   A loop was implemented to iterate through multiple pages (1–10).

2. **Fetching HTML Content**
   Each page was requested using the `requests` library with  headers to simulate a browser.

3. **Parsing the HTML**
   BeautifulSoup was used to parse the HTML and locate all quote elements:

   ```python
   soup.find_all('div', class_='quote')
   ```

4. **Extracting Data Fields**
   For each quote block, the following data was extracted:

   * Quote text
   * Author name
   * Tags associated with the quote

5. **Data Cleaning**

   * Removed extra whitespace using `.strip()`
   * Replaced non-standard quotation marks with standard ones
   * Converted tag lists into comma-separated strings

---

## Data Storage

The extracted data was saved into a CSV file with the following structure:

| Quote | Author | Tags |
| ----- | ------ | ---- |

To ensure compatibility and proper formatting:

* UTF-8 encoding with BOM (`utf-8-sig`) was used
* All fields were enclosed in quotes to handle commas within text
* Tags were stored as a single comma-separated string

---

## Challenges Encountered

### CSV Formatting in Excel

When opening the CSV file directly in Excel, the data initially appeared incorrectly formatted (e.g., all content in a single column).

**Cause:**
Excel misinterpreted the delimiter due to regional settings.

**Solution:**
The file was imported using Excel’s *“From CSV”* feature, where the correct delimiter (comma) and encoding (UTF-8) were specified. This ensured the data displayed in properly aligned columns.

---

## Outcome

* Successfully scraped quotes from multiple pages
* Structured the data into a clean tabular format
* Resolved formatting and encoding issues for compatibility with Excel
* Produced a dataset suitable for further analysis or use

---

## Conclusion

This project demonstrates practical skills in:

* Web scraping
* HTML parsing
* Data cleaning
* Handling real-world formatting and encoding issues

