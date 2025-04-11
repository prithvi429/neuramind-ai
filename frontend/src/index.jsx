// filepath: c:\Users\DELL\OneDrive\Desktop\ai-agent\neuramind-ai-1\frontend\src\index.jsx
import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function App() {
    const [isSettingsOpen, setIsSettingsOpen] = useState(false);

    const toggleSettings = () => {
        setIsSettingsOpen(!isSettingsOpen);
    };

    const saveSettings = () => {
        alert('Settings saved successfully!');
        setIsSettingsOpen(false);
    };

    return (
        <div className="app">
            <div className="user-menu" onClick={toggleSettings} style={{ cursor: 'pointer' }}>
                <img src="user-logo.png" alt="User Logo" style={{ width: '40px', height: '40px', borderRadius: '50%' }} />
                <div className="user-menu-dropdown" style={{ display: isSettingsOpen ? 'block' : 'none' }}>
                    <a href="#" onClick={toggleSettings}>Settings</a>
                    <a href="#">Theme (Light/Dark)</a>
                    <a href="#">Sign Out</a>
                </div>
            </div>
            {isSettingsOpen && (
                <div id="settings-panel" style={{
                    position: 'fixed',
                    top: '20%',
                    left: '50%',
                    transform: 'translate(-50%, -20%)',
                    width: '450px',
                    background: 'var(--interface-gray)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    borderRadius: '12px',
                    padding: '1.5rem',
                    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
                    zIndex: 1000
                }}>
                    <h4 style={{ color: 'var(--neon-blue)', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <i className="fas fa-cogs"></i> Settings
                    </h4>
                    <div style={{ marginBottom: '1.5rem' }}>
                        <label htmlFor="custom-instructions" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
                            <i className="fas fa-edit" style={{ color: 'var(--neon-blue)' }}></i> Custom Instructions
                        </label>
                        <textarea id="custom-instructions" rows="3" style={{
                            width: '100%',
                            padding: '0.5rem',
                            borderRadius: '6px',
                            border: '1px solid var(--neon-blue)',
                            background: 'var(--interface-gray)',
                            color: 'white'
                        }}></textarea>
                    </div>
                    <div style={{ marginBottom: '1.5rem' }}>
                        <label htmlFor="language-tone" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
                            <i className="fas fa-language" style={{ color: 'var(--neon-blue)' }}></i> Language, Tone, and Style
                        </label>
                        <select id="language-tone" style={{
                            width: '100%',
                            padding: '0.5rem',
                            borderRadius: '6px',
                            border: '1px solid var(--neon-blue)',
                            background: 'var(--interface-gray)',
                            color: 'white'
                        }}>
                            <option value="default">Default</option>
                            <option value="formal">Formal</option>
                            <option value="casual">Casual</option>
                            <option value="creative">Creative</option>
                        </select>
                    </div>
                    <div style={{ marginBottom: '1.5rem' }}>
                        <label htmlFor="data-privacy" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
                            <i className="fas fa-shield-alt" style={{ color: 'var(--neon-blue)' }}></i> Data Privacy Controls
                        </label>
                        <select id="data-privacy" style={{
                            width: '100%',
                            padding: '0.5rem',
                            borderRadius: '6px',
                            border: '1px solid var(--neon-blue)',
                            background: 'var(--interface-gray)',
                            color: 'white'
                        }}>
                            <option value="default">Default</option>
                            <option value="strict">Strict</option>
                            <option value="relaxed">Relaxed</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <button onClick={saveSettings} style={{
                            background: 'var(--success-green)',
                            color: 'white',
                            border: 'none',
                            padding: '0.5rem 1rem',
                            borderRadius: '6px',
                            cursor: 'pointer'
                        }}>
                            <i className="fas fa-save"></i> Save
                        </button>
                        <button onClick={toggleSettings} style={{
                            background: 'var(--neon-blue)',
                            color: 'var(--deep-space)',
                            border: 'none',
                            padding: '0.5rem 1rem',
                            borderRadius: '6px',
                            cursor: 'pointer'
                        }}>
                            <i className="fas fa-times"></i> Close
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));