# NOTES

## AI Usage

- **Tool Used**: ChatGPT
- **Purpose**:
  - Took general help with Flask structure and debugging
  - Used it for resolving errors and getting unstuck
  - Verified test coverage and output formatting

## Implementation Notes

- Python 3.11 with Flask
- In-memory store using a dictionary
- Short codes are randomly generated 6-character alphanumeric strings
- URLs are validated
- Full support for:
  - POST /api/shorten
  - GET /<short_code> redirect
  - GET /api/stats/<short_code>
- 5+ test cases included for functional and error scenarios
