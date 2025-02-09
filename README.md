# To-Do List Application

A feature-rich task management application built with Streamlit that allows you to create, manage, and track tasks with different statuses.

## Features

- ✨ Clean and intuitive user interface
- 📱 Responsive grid layout
- 🔍 Filter tasks by status
- 📊 Task statistics dashboard
- 💾 Persistent storage using JSON
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- 🏷️ Multiple task statuses (To Do, In Progress, Completed, Aborted)

## Prerequisites

- Python 3.7 or higher

## Installation

1. Clone this repository or download the source code:
```sh
git clone <repository-url>
cd <project-directory>
```

2. Install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage

1. Start the application:
```sh
streamlit run ToDo.py
```

2. The application will open in your default web browser at `http://localhost:8501`

## Application Structure

- ToDo.py - Main application file
- tasks.json - JSON file for storing tasks
- requirements.txt - List of Python dependencies

## Task Features

Each task includes:
- Title
- Description
- Related URL
- Status (To Do, In Progress, Completed, Aborted)
- Creation timestamp
- Unique ID

## Project Structure

```
├── ToDo.py
├── tasks.json
└── requirements.txt
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

Feel free to use this project as you wish.
```
