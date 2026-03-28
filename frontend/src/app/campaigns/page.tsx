"use client";

import { useEffect, useState } from "react";
import { getCampaigns, createCampaign, type Campaign } from "@/lib/api";
import CampaignCard from "@/components/CampaignCard";

export default function CampaignsPage() {
  const [campaigns, setCampaigns] = useState<Campaign[]>([]);
  const [loading, setLoading] = useState(true);
  const [creating, setCreating] = useState(false);

  // Form state
  const [query, setQuery] = useState("");
  const [location, setLocation] = useState("");
  const [minScore, setMinScore] = useState("50");
  const [maxEmails, setMaxEmails] = useState("20");

  useEffect(() => {
    getCampaigns()
      .then(setCampaigns)
      .finally(() => setLoading(false));
  }, []);

  async function handleCreate(e: React.FormEvent) {
    e.preventDefault();
    if (!query.trim() || !location.trim()) return;

    setCreating(true);
    try {
      await createCampaign({
        name: `${query} in ${location}`,
        target_criteria: {
          query: query.trim(),
          town: location.trim(),
          min_score: minScore,
          max_emails: maxEmails,
        },
      });
      const updated = await getCampaigns();
      setCampaigns(updated);
      setQuery("");
      setLocation("");
    } finally {
      setCreating(false);
    }
  }

  return (
    <div className="max-w-4xl">
      <h1 className="text-2xl font-semibold text-white mb-6">Campaigns</h1>

      {/* New Campaign Form */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 mb-8">
        <h2 className="text-sm font-medium text-zinc-300 mb-4">Launch New Campaign</h2>
        <form onSubmit={handleCreate} className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-xs text-zinc-500 mb-1">Business Type</label>
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="restaurants, plumbers, salons..."
                className="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-3 py-2.5 text-sm text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-500"
              />
            </div>
            <div>
              <label className="block text-xs text-zinc-500 mb-1">Location (UK)</label>
              <input
                type="text"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                placeholder="Bristol, Manchester, London..."
                className="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-3 py-2.5 text-sm text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-xs text-zinc-500 mb-1">Min Lead Score</label>
              <input
                type="number"
                value={minScore}
                onChange={(e) => setMinScore(e.target.value)}
                min="0"
                max="100"
                className="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-3 py-2.5 text-sm text-white focus:outline-none focus:border-zinc-500"
              />
            </div>
            <div>
              <label className="block text-xs text-zinc-500 mb-1">Max Emails</label>
              <input
                type="number"
                value={maxEmails}
                onChange={(e) => setMaxEmails(e.target.value)}
                min="1"
                max="100"
                className="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-3 py-2.5 text-sm text-white focus:outline-none focus:border-zinc-500"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={creating || !query.trim() || !location.trim()}
            className="bg-white text-zinc-900 px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-zinc-200 transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
          >
            {creating ? "Creating..." : "Start Campaign"}
          </button>
        </form>
      </div>

      {/* Campaign List */}
      <h2 className="text-sm font-medium text-zinc-400 uppercase tracking-wider mb-3">
        All Campaigns
      </h2>
      {loading ? (
        <p className="text-zinc-500 text-sm">Loading...</p>
      ) : campaigns.length === 0 ? (
        <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-8 text-center">
          <p className="text-zinc-500">No campaigns yet. Create one above.</p>
        </div>
      ) : (
        <div className="grid grid-cols-2 gap-3">
          {campaigns.map((c) => (
            <CampaignCard key={c.id} campaign={c} />
          ))}
        </div>
      )}
    </div>
  );
}
