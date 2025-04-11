![NeuraMind AI Banner] (https://github.com/prithvi429/neuramind-ai/blob/main/assets/logo.png?raw=true)

# 🧠 NeuraMind AI

**India’s First Free, Human-like Multi-Agent AI Assistant**  
🚀 Built solo by [Pruthviraj Rathod](https://www.linkedin.com/in/rathod-pruthviraj/) with a mission to make AI accessible, useful, and personal.

---

## 📌 About the Project

NeuraMind AI is a modular multi-agent system designed to solve real-world problems like navigation, content generation, image processing, and financial analysis. Each agent operates independently but collaborates through a central backend.

---

## 📂 Project Structure

```
neuramind-ai/
├── agents/                 # Individual AI agents
│   ├── config.json         # Agent configuration
│   ├── prompts.txt         # Example prompts for agents
│   ├── mapping_agent.py    # Mapping agent
│   ├── voice_agent.py      # Voice processing agent
│   ├── writing_agent.py    # Content generation agent
│   ├── image_agent.py      # Image generation agent
│   └── finance_agent.py    # Financial analysis agent
├── api_docs/               # API documentation
│   ├── openapi.yaml        # OpenAPI specification
│   └── README.md           # API usage guide
├── backend/                # Backend logic and APIs
│   ├── main.py             # Entry point for the backend
│   ├── nav_agent.py        # Navigation agent logic
│   ├── image_agent.py      # Image processing agent
│   └── utils/              # Utility functions
├── data/                   # Data files and examples
│   ├── prompts/            # Prompts for agents
│   ├── training_data.csv   # Training data for AI models
│   ├── responses.json      # Example responses
│   └── README.md           # Data folder documentation
├── docs/                   # Documentation
│   ├── architecture.md     # System architecture
│   ├── roadmap.md          # Development roadmap
│   ├── production_plan.md  # Production plan
│   ├── inspiration.md      # Project inspiration
│   └── installation_guide.md # Installation guide
├── frontend/               # Frontend code
│   ├── public/             # Static files
│   ├── src/                # React components
│   ├── styles/             # CSS styles
│   └── README.md           # Frontend folder documentation
├── notebooks/              # Jupyter notebooks
│   ├── nav_agent_flow.ipynb # Navigation agent flow
│   └── text_generation_prompts.ipynb # Writing agent prompts
├── prompts/                # Prompts for agents
│   ├── writing_agent_prompts.txt
│   ├── image_agent_prompts.txt
│   └── finance_prompts.txt
├── test/                   # Test scripts
│   ├── test_nav_agent.py   # Tests for navigation agent
│   ├── test_frontend_render.py # Tests for frontend rendering
│   └── test_endpoints.py   # Tests for backend endpoints
├── weights/                # Pre-trained model weights
│   └── mapping_model.pt    # Mapping agent model
└── README.md               # Main project documentation
```

---

## 🚀 Features

- **Writing & Coding**: Generate content or code based on user prompts.
- **Mapping & Navigation**: Plan routes and provide navigation assistance.
- **Image Generation & Editing**: Create and edit images using AI.
- **Finance & Business Insights**: Analyze financial data and generate reports.
- **Voice Interaction**: Communicate with the system using natural language.
- **Customizable Settings Panel**:
  - **Custom Instructions**: Provide specific instructions for the AI to follow.
  - **Language, Tone, and Style**: Choose between default, formal, casual, or creative response styles.
  - **Data Privacy Controls**: Manage how your data is handled with options like default, strict, or relaxed.
- **Chat History Management**:
  - Rename or delete chat sessions.
  - Organized by time periods (Today, Previous 7 Days, Previous 30 Days).
- **Persona Store**:
  - Access pre-configured AI personas for specific tasks.
- **Explore Neura**:
  - Discover additional tools and plugins.
- **Upgrade Plan**:
  - Subscribe to NeuraMind Plus for faster responses, advanced features, and more.

---

## 🛠️ Installation

Refer to the [Installation Guide](docs/installation_guide.md) for detailed setup instructions.

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/neuramind-ai.git
   ```
2. Navigate to the project directory:
   ```bash
   cd neuramind-ai
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the development server:
   ```bash
   npm start
   ```

---

## 📖 Usage

- Open the application in your browser.
- Use the **Settings Panel** to customize your experience.
- Start new chats, explore personas, or upgrade your plan for additional features.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📢 Contact

👨‍💻 **Founder**: Pruthviraj Rathod  
📧 **Email**: prithvirathod29884@gmail.com  
🌐 **Socials**:  
- [LinkedIn](https://www.linkedin.com/in/rathod-pruthviraj/)  
- [GitHub](https://github.com/prithvi429)  
- [Twitter/X](https://x.com/PrithviRathod19)

---

## 📜 License

This project is licensed under the MIT License.

---

**NeuraMind AI – A smarter way to work.**
