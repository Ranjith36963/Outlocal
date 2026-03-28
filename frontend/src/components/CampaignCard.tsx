import type { Campaign } from "@/lib/api";

const STATUS_BADGE: Record<string, string> = {
  draft: "bg-zinc-700 text-zinc-300",
  active: "bg-emerald-900/50 text-emerald-300",
  paused: "bg-amber-900/50 text-amber-300",
  completed: "bg-blue-900/50 text-blue-300",
};

interface CampaignCardProps {
  campaign: Campaign;
  stats?: Record<string, number>;
}

export default function CampaignCard({ campaign, stats }: CampaignCardProps) {
  const badgeColor = STATUS_BADGE[campaign.status] || STATUS_BADGE.draft;
  const sent = stats?.sent || 0;
  const replied = stats?.reply_interested ? Object.values(stats).reduce((a, b) => a + b, 0) : 0;

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-4">
      <div className="flex items-start justify-between">
        <div>
          <h3 className="text-sm font-medium text-white">{campaign.name}</h3>
          <p className="text-xs text-zinc-500 mt-0.5">
            {campaign.target_criteria?.town && `${campaign.target_criteria.town}`}
            {campaign.target_criteria?.type && ` · ${campaign.target_criteria.type}`}
          </p>
        </div>
        <span className={`text-[10px] px-2 py-0.5 rounded-full font-medium ${badgeColor}`}>
          {campaign.status}
        </span>
      </div>

      {stats && (
        <div className="flex gap-4 mt-3 pt-3 border-t border-zinc-800">
          <div>
            <p className="text-lg font-semibold text-white">{sent}</p>
            <p className="text-[10px] text-zinc-500">Sent</p>
          </div>
          <div>
            <p className="text-lg font-semibold text-white">{replied}</p>
            <p className="text-[10px] text-zinc-500">Replied</p>
          </div>
        </div>
      )}

      <p className="text-[10px] text-zinc-600 mt-3">
        {new Date(campaign.created_at).toLocaleDateString("en-GB")}
      </p>
    </div>
  );
}
