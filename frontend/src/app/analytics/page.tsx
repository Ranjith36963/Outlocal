"use client";

import { useEffect, useState } from "react";
import { getCampaigns, getCampaignStats, type Campaign, type CampaignStats } from "@/lib/api";
import StatsCard from "@/components/StatsCard";

export default function AnalyticsPage() {
  const [campaigns, setCampaigns] = useState<Campaign[]>([]);
  const [stats, setStats] = useState<Record<number, CampaignStats>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const camps = await getCampaigns();
        setCampaigns(camps);

        const statsMap: Record<number, CampaignStats> = {};
        for (const c of camps) {
          try {
            statsMap[c.id] = await getCampaignStats(c.id);
          } catch {
            // Campaign might not have stats yet
          }
        }
        setStats(statsMap);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  // Aggregate stats across all campaigns
  const totalSent = Object.values(stats).reduce((sum, s) => sum + (s.stats?.sent || 0), 0);
  const totalOpened = Object.values(stats).reduce((sum, s) => sum + (s.stats?.opened || 0), 0);
  const totalReplied = Object.values(stats).reduce(
    (sum, s) => sum + (s.stats?.reply_interested || 0) + (s.stats?.reply_not_interested || 0),
    0
  );
  const totalInterested = Object.values(stats).reduce(
    (sum, s) => sum + (s.stats?.reply_interested || 0),
    0
  );

  const openRate = totalSent > 0 ? ((totalOpened / totalSent) * 100).toFixed(1) : "0";
  const replyRate = totalSent > 0 ? ((totalReplied / totalSent) * 100).toFixed(1) : "0";
  const convRate = totalSent > 0 ? ((totalInterested / totalSent) * 100).toFixed(1) : "0";

  if (loading) return <div className="text-zinc-500 p-8">Loading...</div>;

  return (
    <div className="max-w-5xl">
      <h1 className="text-2xl font-semibold text-white mb-6">Analytics</h1>

      {/* Overview Stats */}
      <div className="grid grid-cols-4 gap-4 mb-8">
        <StatsCard label="Total Sent" value={totalSent} />
        <StatsCard label="Open Rate" value={`${openRate}%`} accent="amber" />
        <StatsCard label="Reply Rate" value={`${replyRate}%`} accent="amber" />
        <StatsCard label="Conversion" value={`${convRate}%`} accent="green" />
      </div>

      {/* Per-Campaign Breakdown */}
      <h2 className="text-sm font-medium text-zinc-400 uppercase tracking-wider mb-3">
        Campaign Breakdown
      </h2>

      {campaigns.length === 0 ? (
        <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-8 text-center">
          <p className="text-zinc-500">No campaigns to analyse yet</p>
        </div>
      ) : (
        <div className="bg-zinc-900 border border-zinc-800 rounded-xl overflow-hidden">
          <table className="w-full">
            <thead>
              <tr className="border-b border-zinc-800">
                <th className="text-left text-xs text-zinc-500 font-medium px-4 py-3">Campaign</th>
                <th className="text-right text-xs text-zinc-500 font-medium px-4 py-3">Sent</th>
                <th className="text-right text-xs text-zinc-500 font-medium px-4 py-3">Opened</th>
                <th className="text-right text-xs text-zinc-500 font-medium px-4 py-3">Replied</th>
                <th className="text-right text-xs text-zinc-500 font-medium px-4 py-3">Interested</th>
                <th className="text-right text-xs text-zinc-500 font-medium px-4 py-3">Status</th>
              </tr>
            </thead>
            <tbody>
              {campaigns.map((c) => {
                const s = stats[c.id]?.stats || {};
                return (
                  <tr key={c.id} className="border-b border-zinc-800/50 hover:bg-zinc-800/30">
                    <td className="px-4 py-3 text-sm text-white">{c.name}</td>
                    <td className="px-4 py-3 text-sm text-zinc-300 text-right">{s.sent || 0}</td>
                    <td className="px-4 py-3 text-sm text-zinc-300 text-right">{s.opened || 0}</td>
                    <td className="px-4 py-3 text-sm text-zinc-300 text-right">
                      {(s.reply_interested || 0) + (s.reply_not_interested || 0)}
                    </td>
                    <td className="px-4 py-3 text-sm text-emerald-400 text-right font-medium">
                      {s.reply_interested || 0}
                    </td>
                    <td className="px-4 py-3 text-right">
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-zinc-800 text-zinc-400">
                        {c.status}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
