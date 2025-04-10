# Installation Guide for NeuraMind AI

Follow these steps to set up and run NeuraMind AI on your local machine.

---

## Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **Node.js 14+**
- **npm** or **yarn**
- **Git**

---

## Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/prithvi429/neuramind-ai.git
   cd neuramind-ai/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   python main.py
   ```

---

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

---

## Access the Application

- Open your browser and navigate to:
  - **Frontend**: `http://localhost:3000`
  - **Backend**: `http://localhost:5000`

---

## Troubleshooting

- If you encounter issues with dependencies, ensure your Python and Node.js versions meet the prerequisites.
- For backend errors, check the logs in the terminal for detailed messages.
- For frontend issues, ensure all dependencies are installed and the development server is running.

---

**NeuraMind AI – A smarter way to work.**
