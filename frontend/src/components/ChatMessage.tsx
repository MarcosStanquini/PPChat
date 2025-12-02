import type { Message } from '../types';
import './ChatMessage.css';

interface ChatMessageProps {
  message: Message;
  onShowContext?: () => void;
}

export function ChatMessage({ message, onShowContext }: ChatMessageProps) {
  return (
    <div className={`chat-message ${message.type}`}>
      <div className="message-header">
        <span className="message-type">
          {message.type === 'user' ? 'You' : 'PPChat'}
        </span>
        <span className="message-time">
          {message.timestamp.toLocaleTimeString()}
        </span>
      </div>
      <div className="message-content">{message.content}</div>
      {message.type === 'assistant' && message.context && (
        <button className="context-button" onClick={onShowContext}>
          View Source Context
        </button>
      )}
    </div>
  );
}
