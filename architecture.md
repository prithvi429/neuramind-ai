# NeuraMind AI Architecture

This document outlines the architecture of the NeuraMind AI system, detailing its components and how they interact.

---

## 🏗️ System Overview

NeuraMind AI is a multi-agent system designed to handle various tasks such as navigation, content generation, image processing, and financial analysis. The architecture is modular, allowing each agent to function independently while collaborating through a central backend.

---

## 📊 Multi-Agent Flow Diagram

Below is the visual representation of the multi-agent flow:

![Multi-Agent Flow](./architecture/multi_agent_flow.png)

---

## 📂 Folder Structure

```
neuramind-ai/
├── backend/                # Backend logic and APIs
│   ├── main.py             # Entry point for the backend
│   ├── nav_agent.py        # Navigation agent logic
│   ├── image_agent.py      # Image processing agent
│   └── utils/              # Utility functions
├── frontend/               # Frontend code
│   ├── public/             # Static files
│   ├── src/                # React components
│   └── styles/             # CSS styles
├── agents/                 # Individual AI agents
│   ├── mapping_agent.py    # Mapping agent
│   ├── voice_agent.py      # Voice processing agent
│   ├── writing_agent.py    # Content generation agent
│   ├── image_agent.py      # Image generation agent
│   └── finance_agent.py    # Financial analysis agent
├── data/                   # Data files and examples
│   └── prompts_examples.json
└── architecture.md         # System architecture documentation
```

---

## 🧩 Components

### 1. **Backend**
- **Framework**: Flask
- **Purpose**: Acts as the central hub, handling API requests and coordinating between agents.
- **Key Files**:
  - `main.py`: Entry point for the backend.
  - `nav_agent.py`: Handles route calculations.
  - `image_agent.py`: Manages image generation tasks.

### 2. **Frontend**
- **Framework**: React.js
- **Purpose**: Provides a user-friendly interface for interacting with the system.
- **Key Files**:
  - `App.jsx`: Main React component.
  - `Header.jsx`, `Footer.jsx`: UI components.
  - `AgentCard.jsx`: Displays agent details.

### 3. **Agents**
- **Purpose**: Specialized modules for handling specific tasks.
- **Examples**:
  - `mapping_agent.py`: Handles spatial mapping.
  - `writing_agent.py`: Generates content or code.
  - `finance_agent.py`: Analyzes financial data.

### 4. **Data**
- **Purpose**: Stores example prompts and other data files.
- **Key File**: `prompts_examples.json`

---

## 🔄 Workflow

1. **Frontend**: Users interact with the system via the React-based UI.
2. **Backend**: The Flask server processes requests and routes them to the appropriate agent.
3. **Agents**: Perform specific tasks and return results to the backend.
4. **Frontend**: Displays the results to the user.

---

## 🚀 Future Enhancements

- Add a database for user data and logs.
- Implement real-time collaboration between agents.
- Enhance the UI with more interactive features.

---

**NeuraMind AI – A smarter way to work.**
