interface StatsCardProps {
  label: string;
  value: string | number;
  sub?: string;
  accent?: "default" | "green" | "amber" | "red";
}

const ACCENT_COLORS = {
  default: "text-white",
  green: "text-emerald-400",
  amber: "text-amber-400",
  red: "text-red-400",
};

export default function StatsCard({ label, value, sub, accent = "default" }: StatsCardProps) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-5">
      <p className="text-xs text-zinc-500 uppercase tracking-wider">{label}</p>
      <p className={`text-3xl font-semibold mt-1 ${ACCENT_COLORS[accent]}`}>{value}</p>
      {sub && <p className="text-xs text-zinc-500 mt-1">{sub}</p>}
    </div>
  );
}
