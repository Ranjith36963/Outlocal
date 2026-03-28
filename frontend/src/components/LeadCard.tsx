import type { Lead } from "@/lib/api";

const STATUS_COLORS: Record<string, string> = {
  new: "bg-zinc-700 text-zinc-300",
  enriched: "bg-blue-900/50 text-blue-300",
  scored: "bg-indigo-900/50 text-indigo-300",
  contacted: "bg-yellow-900/50 text-yellow-300",
  replied: "bg-cyan-900/50 text-cyan-300",
  interested: "bg-emerald-900/50 text-emerald-300",
  converted: "bg-green-900/50 text-green-300",
  lost: "bg-zinc-800 text-zinc-500",
  unsubscribed: "bg-red-900/50 text-red-400",
};

interface LeadCardProps {
  lead: Lead;
  onClick?: () => void;
  compact?: boolean;
}

export default function LeadCard({ lead, onClick, compact = false }: LeadCardProps) {
  const statusColor = STATUS_COLORS[lead.status] || STATUS_COLORS.new;

  return (
    <div
      onClick={onClick}
      className={`bg-zinc-900 border border-zinc-800 rounded-lg p-4 hover:border-zinc-600 transition-colors ${
        onClick ? "cursor-pointer" : ""
      } ${lead.status === "interested" ? "border-emerald-800 bg-emerald-950/20" : ""}`}
    >
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0">
          <h3 className="text-sm font-medium text-white truncate">{lead.business_name}</h3>
          <p className="text-xs text-zinc-500 mt-0.5">{lead.town}</p>
        </div>
        <span className={`text-[10px] px-2 py-0.5 rounded-full font-medium shrink-0 ${statusColor}`}>
          {lead.status}
        </span>
      </div>

      {!compact && (
        <div className="mt-3 space-y-1">
          {lead.email && (
            <p className="text-xs text-zinc-400 truncate">{lead.email}</p>
          )}
          {lead.score !== null && (
            <div className="flex items-center gap-2">
              <div className="flex-1 h-1.5 bg-zinc-800 rounded-full overflow-hidden">
                <div
                  className="h-full rounded-full bg-emerald-500"
                  style={{ width: `${lead.score}%` }}
                />
              </div>
              <span className="text-[10px] text-zinc-500 w-6 text-right">{lead.score}</span>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
