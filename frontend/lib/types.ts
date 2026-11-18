import type { UIMessage } from "ai";
import { z } from "zod";
import type { Suggestion } from "./db/schema";

export const messageMetadataSchema = z.object({
  createdAt: z.string().optional(),
});

export type MessageMetadata = z.infer<typeof messageMetadataSchema>;

export type ArtifactKind = "text" | "code" | "image" | "sheet";

export type ChatTools = Record<string, any>;

export type WaitingStatusData = {
  phase: "waiting" | "still-waiting" | "health" | "thinking";
  message: string;
  modelId?: string;
  modelName?: string;
};

export type CustomUIDataTypes = {
  textDelta?: string;
  imageDelta?: string;
  sheetDelta?: string;
  codeDelta?: string;
  suggestion?: Suggestion;
  appendMessage?: string;
  id?: string;
  title?: string;
  kind?: ArtifactKind;
  clear?: null;
  finish?: null;
  "chat-title"?: string;
  "waiting-status"?: WaitingStatusData;
  [key: string]: any;
};

export type ChatMessage = UIMessage<
  MessageMetadata,
  CustomUIDataTypes,
  ChatTools
>;

export type Attachment = {
  name: string;
  url: string;
  contentType: string;
};
