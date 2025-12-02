import type { ContextDocument } from '../types';
import './ContextModal.css';

interface ContextModalProps {
  context: string;
  contextDocs: ContextDocument[];
  onClose: () => void;
}

export function ContextModal({ contextDocs, onClose }: ContextModalProps) {
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Source Context</h2>
          <button className="close-button" onClick={onClose}>
            &times;
          </button>
        </div>
        <div className="modal-body">
          <div className="context-section">
            <h3>Retrieved Documents ({contextDocs.length})</h3>
            {contextDocs.map((doc, index) => (
              <div key={index} className="context-doc">
                <div className="doc-metadata">
                  <span className="doc-page">
                    Page {doc.metadata.page || 'N/A'} / {doc.metadata.total_pages || 'N/A'}
                  </span>
                  <span className="doc-chars">
                    {doc.metadata.char_count || 0} chars
                  </span>
                </div>
                <div className="doc-content">{doc.content}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
