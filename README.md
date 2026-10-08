# Memo App

A simple web-based memo application built with Flask.

## Features

- ✏️ Create and save memos
- 📝 View all saved memos
- ⏰ Automatic timestamps for each memo
- 🎨 Simple and clean web interface

## Technologies

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Data Storage**: Plain text file

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kknxk/memo.git
cd memo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask
```

### Running the Application

```bash
python app2.py
```

Then open your browser and navigate to `http://localhost:5000`

## File Structure

```
memo/
├── app2.py          # Main Flask application (recommended version)
├── app.py           # Initial version
├── templates/       # HTML templates
├── static/          # Static files (CSS, JS)
├── memo.txt         # Memo storage (auto-generated)
└── README.md        # This file
```

## Usage

1. Open the application in your browser
2. Type your memo in the text area
3. Click "Save" to save the memo
4. Your memo will appear in the list with a timestamp

## Future Improvements

- Add edit/delete functionality
- Use a database instead of text files
- Add categories or tags
- Implement user authentication
- Add search functionality

## License

MIT
