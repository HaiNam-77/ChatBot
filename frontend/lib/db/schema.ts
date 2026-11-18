export interface Vote {
  chatId: string;
  messageId: string;
  isUpvoted: boolean;
}

export interface Chat {
  id: string;
  createdAt: Date;
  title: string;
  userId?: string;
  visibility: "public" | "private";
}

export interface DBMessage {
  id: string;
  role: "user" | "assistant" | "system";
  parts: any[];
  createdAt: Date | string;
}

export interface Document {
  id: string;
  createdAt: Date;
  title: string;
  content: string;
  kind: string;
}

export interface Suggestion {
  id: string;
  documentId: string;
  description: string;
}
