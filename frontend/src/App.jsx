import React, { useState } from 'react';
import './App.css'; // Import component-specific styles

const App = () => {
  const [theme, setTheme] = useState('dark');
  const [activityLog, setActivityLog] = useState(['Welcome to NeuraMind AI!']);
  const [feedback, setFeedback] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [message, setMessage] = useState('');

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'dark' ? 'light' : 'dark'));
    document.body.classList.toggle('light-mode');
  };

  const logActivity = (activity) => {
    setActivityLog((prevLog) => [...prevLog, activity]);
  };

  const submitFeedback = () => {
    if (feedback.trim()) {
      alert('Thank you for your feedback!');
      setFeedback('');
    } else {
      alert('Please enter your feedback before submitting.');
    }
  };

  const handleLogin = () => {
    if (email.includes('@') && password) {
      setIsAuthenticated(true);
      logActivity('User authenticated successfully.');
    } else {
      alert('Please enter a valid email and password.');
    }
  };

  const handleSendMessage = () => {
    if (message.trim()) {
      setChatHistory([...chatHistory, { sender: 'user', text: message }]);
      setMessage('');
      logActivity('User sent a message.');
      // Simulate AI response
      setTimeout(() => {
        setChatHistory((prev) => [
          ...prev,
          { sender: 'ai', text: 'This is a simulated AI response.' },
        ]);
        logActivity('AI responded to the user.');
      }, 1000);
    }
  };

  if (!isAuthenticated) {
    return (
      <div className="login-container">
        <div className="login-box">
          <h2>NeuraMind Access Portal</h2>
          <input
            type="email"
            className="login-input"
            placeholder="Email ID"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            className="login-input"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button className="send-button" onClick={handleLogin}>
            Authenticate
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className={`app ${theme}`}>
      <button className="theme-toggle" onClick={toggleTheme}>
        Toggle Theme
      </button>
      <div className="main-interface">
        <div className="sidebar">
          <div className="logo">
            <img src="logo.png" alt="NeuraMind Logo" />
            NeuraMind AI
          </div>
          <div className="chat-item" style={{ color: 'var(--neon-blue)' }}>
            <i className="fas fa-plus"></i> New Chat
          </div>
          <h4>Chat History</h4>
          <div className="chat-item">Market Analysis 2023</div>
          <div className="chat-item">Project Quantum</div>
          <div className="chat-item">Creative Writing Session</div>
          <div className="settings-panel">
            <h4>AI Mode</h4>
            <select>
              <option value="general">General</option>
              <option value="creative">Creative</option>
              <option value="analytical">Analytical</option>
            </select>
          </div>
          <div className="activity-tracker">
            <h4>Activity Tracker</h4>
            <ul>
              {activityLog.map((activity, index) => (
                <li key={index}>{activity}</li>
              ))}
            </ul>
          </div>
          <div className="feedback-section">
            <h4>Feedback</h4>
            <textarea
              rows="3"
              value={feedback}
              onChange={(e) => setFeedback(e.target.value)}
              placeholder="Share your thoughts..."
            ></textarea>
            <button onClick={submitFeedback}>Submit</button>
          </div>
        </div>
        <div className="chat-container">
          <div className="chat-history">
            {chatHistory.map((chat, index) => (
              <div
                key={index}
                className={`message ${chat.sender === 'ai' ? 'ai-message' : 'user-message'}`}
              >
                <strong>{chat.sender === 'ai' ? 'NeuraMind AI:' : 'You:'}</strong> {chat.text}
              </div>
            ))}
          </div>
          <div className="input-container">
            <input
              type="text"
              className="chat-input"
              placeholder="Enter cognitive query..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
            />
            <div className="toolbar">
              <label className="file-input-label">
                <i className="fas fa-paperclip"></i>
                <input type="file" multiple accept=".pdf,.docx,.xlsx,.jpg,.mp4" hidden />
              </label>
              <button className="send-button" onClick={handleSendMessage}>
                <i className="fas fa-arrow-up"></i>
              </button>
              <button className="send-button">
                <i className="fas fa-microphone"></i>
              </button>
              <button className="send-button">
                <i className="fas fa-map-marker-alt"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
