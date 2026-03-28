const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

async function apiFetch<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...options?.headers },
    ...options,
  });
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(error.detail || `API error: ${res.status}`);
  }
  return res.json();
}

// Health
export const getHealth = () => apiFetch<{ status: string; version: string }>("/health");

// Leads
export interface Lead {
  id: number;
  business_name: string;
  owner_name: string | null;
  email: string | null;
  phone: string | null;
  website: string | null;
  town: string;
  source: string;
  score: number | null;
  status: string;
  created_at: string;
  updated_at: string;
  activity_log?: ActivityEntry[];
}

export interface ActivityEntry {
  action: string;
  details: string | null;
  timestamp: string;
}

export const getLeads = (params?: Record<string, string>) => {
  const query = params ? "?" + new URLSearchParams(params).toString() : "";
  return apiFetch<Lead[]>(`/api/v1/leads${query}`);
};

export const getLead = (id: number) =>
  apiFetch<Lead & { activity_log: ActivityEntry[] }>(`/api/v1/leads/${id}`);

export const createLead = (data: {
  business_name: string;
  town: string;
  source?: string;
  owner_name?: string;
  email?: string;
  phone?: string;
  website?: string;
}) => apiFetch<{ id: number }>("/api/v1/leads", { method: "POST", body: JSON.stringify(data) });

export const updateLead = (id: number, data: Record<string, string>) =>
  apiFetch<{ id: number; status: string }>(`/api/v1/leads/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });

export const deleteLead = (id: number) =>
  apiFetch<{ id: number }>(`/api/v1/leads/${id}`, { method: "DELETE" });

// Campaigns
export interface Campaign {
  id: number;
  name: string;
  status: string;
  template: string | null;
  target_criteria: Record<string, string>;
  created_at: string;
}

export interface CampaignStats {
  campaign: Campaign;
  stats: Record<string, number>;
}

export const getCampaigns = () => apiFetch<Campaign[]>("/api/v1/campaigns");

export const createCampaign = (data: {
  name: string;
  target_criteria: Record<string, string>;
  template?: string;
}) =>
  apiFetch<{ id: number }>("/api/v1/campaigns", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const getCampaignStats = (id: number) =>
  apiFetch<CampaignStats>(`/api/v1/campaigns/${id}/stats`);

// Compliance
export const unsubscribe = (email: string) =>
  apiFetch<{ status: string }>(`/api/v1/compliance/unsubscribe/${encodeURIComponent(email)}`, {
    method: "POST",
  });

export const requestErasure = (email: string) =>
  apiFetch<{ erased: boolean }>("/api/v1/compliance/erasure", {
    method: "POST",
    body: JSON.stringify({ email }),
  });

export const getAuditTrail = (email: string) =>
  apiFetch<{ email: string; action: string; details: string; timestamp: string }[]>(
    `/api/v1/compliance/audit/${encodeURIComponent(email)}`
  );
