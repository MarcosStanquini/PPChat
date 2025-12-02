export interface QuestionRequest {
  question: string;
}

export interface DocumentMetadata {
  page: number;
  total_pages: number;
  chunk_method: string;
  char_count: number;
  source: string;
}

export interface ContextDocument {
  content: string;
  metadata: Record<string, any>;
}

export interface QuestionResponse {
  question: string;
  answer: string;
  context: string;
  context_docs: ContextDocument[];
}

export interface Message {
  id: string;
  type: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  context?: string;
  context_docs?: ContextDocument[];
}
