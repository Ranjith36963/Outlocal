"use client";

import { useEffect, useState } from "react";
import { getLeads, getCampaigns, type Lead, type Campaign } from "@/lib/api";
import StatsCard from "@/components/StatsCard";
import LeadCard from "@/components/LeadCard";
import CampaignCard from "@/components/CampaignCard";

export default function DashboardPage() {
  const [leads, setLeads] = useState<Lead[]>([]);
  const [campaigns, setCampaigns] = useState<Campaign[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      try {
        const [leadsData, campaignsData] = await Promise.all([getLeads(), getCampaigns()]);
        setLeads(leadsData);
        setCampaigns(campaignsData);
      } catch (e) {
        setError(e instanceof Error ? e.message : "Failed to load data");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <div className="text-zinc-500 p-8">Loading...</div>;
  if (error) {
    return (
      <div className="p-8">
        <div className="bg-red-950/50 border border-red-800 rounded-lg p-4">
          <p className="text-red-400 text-sm">Backend not reachable: {error}</p>
          <p className="text-red-500/70 text-xs mt-1">
            Start the FastAPI server: uvicorn src.outlocal.api.main:app --port 8000
          </p>
        </div>
      </div>
    );
  }

  const totalLeads = leads.length;
  const contacted = leads.filter((l) =>
    ["contacted", "replied", "interested", "converted"].includes(l.status)
  ).length;
  const replied = leads.filter((l) => ["replied", "interested"].includes(l.status)).length;
  const interested = leads.filter((l) => l.status === "interested").length;
  const hotLeads = leads.filter((l) => l.status === "interested");

  return (
    <div className="max-w-6xl">
      <h1 className="text-2xl font-semibold text-white mb-6">Dashboard</h1>

      <div className="grid grid-cols-4 gap-4 mb-8">
        <StatsCard label="Total Leads" value={totalLeads} />
        <StatsCard label="Emails Sent" value={contacted} />
        <StatsCard label="Replies" value={replied} accent="amber" />
        <StatsCard label="Interested" value={interested} accent="green" />
      </div>

      <div className="grid grid-cols-2 gap-6">
        <div>
          <h2 className="text-sm font-medium text-zinc-400 uppercase tracking-wider mb-3">
            People Who Want to Talk
          </h2>
          {hotLeads.length === 0 ? (
            <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6 text-center">
              <p className="text-zinc-500 text-sm">No interested leads yet</p>
              <p className="text-zinc-600 text-xs mt-1">Launch a campaign to get started</p>
            </div>
          ) : (
            <div className="space-y-2">
              {hotLeads.map((lead) => (
                <LeadCard key={lead.id} lead={lead} />
              ))}
            </div>
          )}
        </div>

        <div>
          <h2 className="text-sm font-medium text-zinc-400 uppercase tracking-wider mb-3">
            Active Campaigns
          </h2>
          {campaigns.length === 0 ? (
            <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6 text-center">
              <p className="text-zinc-500 text-sm">No campaigns yet</p>
              <p className="text-zinc-600 text-xs mt-1">Go to Campaigns to create one</p>
            </div>
          ) : (
            <div className="space-y-2">
              {campaigns.map((c) => (
                <CampaignCard key={c.id} campaign={c} />
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
