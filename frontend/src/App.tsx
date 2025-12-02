import { useState, useEffect, useRef } from 'react';
import { ChatMessage } from './components/ChatMessage';
import { ChatInput } from './components/ChatInput';
import { ContextModal } from './components/ContextModal';
import { ragApi } from './api/ragApi';
import type { Message } from './types';
import './App.css';

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [selectedContext, setSelectedContext] = useState<Message | null>(null);
  const [healthStatus, setHealthStatus] = useState<string>('checking...');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    checkHealth();
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const checkHealth = async () => {
    try {
      const health = await ragApi.checkHealth();
      setHealthStatus(health.rag_service);
    } catch {
      setHealthStatus('error');
    }
  };

  const handleSendMessage = async (content: string) => {
    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      const response = await ragApi.askQuestion(content);

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'assistant',
        content: response.answer,
        timestamp: new Date(),
        context: response.context,
        context_docs: response.context_docs,
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to get response');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1>PPChat</h1>
          <p>RAG-powered Document Q&A</p>
        </div>
        <div className={`health-indicator ${healthStatus}`}>
          <span className="health-dot"></span>
          {healthStatus === 'initialized' ? 'Online' : 'Offline'}
        </div>
      </header>

      <main className="chat-container">
        <div className="messages-list">
          {messages.length === 0 && (
            <div className="welcome-message">
              <h2>Welcome to PPChat!</h2>
              <p>Ask questions about your documents and get intelligent answers.</p>
              <div className="example-questions">
                <p className="example-label">Try asking:</p>
                <ul>
                  <li>What is this document about?</li>
                  <li>Summarize the main points</li>
                  <li>What does it say about [topic]?</li>
                </ul>
              </div>
            </div>
          )}

          {messages.map((message) => (
            <ChatMessage
              key={message.id}
              message={message}
              onShowContext={
                message.context
                  ? () => setSelectedContext(message)
                  : undefined
              }
            />
          ))}

          {isLoading && (
            <div className="loading-indicator">
              <div className="loading-dots">
                <span></span>
                <span></span>
                <span></span>
              </div>
              <p>Thinking...</p>
            </div>
          )}

          {error && (
            <div className="error-message">
              <strong>Error:</strong> {error}
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        <ChatInput onSend={handleSendMessage} disabled={isLoading} />
      </main>

      {selectedContext && (
        <ContextModal
          context={selectedContext.context!}
          contextDocs={selectedContext.context_docs!}
          onClose={() => setSelectedContext(null)}
        />
      )}
    </div>
  );
}

export default App;
