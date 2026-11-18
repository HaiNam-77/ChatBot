export const DEFAULT_CHAT_MODEL = "default-model";

export interface ModelCapabilities {
  reasoning?: boolean;
  vision?: boolean;
  tools?: boolean;
}

export interface ChatModel {
  id: string;
  name: string;
  description: string;
  provider?: string;
  capabilities?: ModelCapabilities;
  gatewayOrder?: any;
  reasoningEffort?: any;
}

export const chatModels: ChatModel[] = [
  {
    id: "default-model",
    name: "RAG Assistant",
    description: "Trợ lý tra cứu giáo trình Lý thuyết thông tin",
    provider: "FastAPI RAG",
    capabilities: {
      reasoning: false,
      vision: false,
      tools: false,
    },
  },
];

export const allowedModelIds = ["default-model"];

export const getCapabilities = async (): Promise<Record<string, ModelCapabilities>> => ({
  "default-model": {
    reasoning: false,
    vision: false,
    tools: false,
  },
});

export const getModelAvailability = async (_modelId: string) => "available";
