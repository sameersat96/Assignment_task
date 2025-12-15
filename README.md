# Assignment_task

# Task Board

A beautiful full-stack Task Board application built with FastAPI and React featuring a stunning dark theme with glassmorphism effects.

## Features

- Add, complete, and delete tasks
- Live progress indicator with percentage
- Beautiful dark theme with glassmorphism UI
- Smooth animations and transitions

### Unique Features

- **Confetti Celebration** - Completing a task triggers a colorful confetti animation
- **Motivational Quotes** - Random productivity quotes to keep you inspired

## Tech Stack

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: React (CDN), Tailwind CSS (CDN)
- **Storage**: In-memory (no database required)

## Installation

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/task-board.git
cd task-board

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
uvicorn main:app --host 0.0.0.0 --port 8000

4. Open your browser and navigate to http://localhost:8000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | List all tasks |
| POST | /api/tasks | Add a new task |
| PATCH | /api/tasks/{task_id} | Mark task complete/incomplete |
| DELETE | /api/tasks/{task_id} | Delete a task |

## License

MIT License
