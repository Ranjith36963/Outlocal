"use client";

import { useEffect, useState } from "react";
import { getLeads, getLead, updateLead, type Lead, type ActivityEntry } from "@/lib/api";
import LeadCard from "@/components/LeadCard";

const PIPELINE_COLUMNS = [
  { status: "new", label: "New" },
  { status: "enriched", label: "Enriched" },
  { status: "scored", label: "Scored" },
  { status: "contacted", label: "Contacted" },
  { status: "replied", label: "Replied" },
  { status: "interested", label: "Interested" },
  { status: "converted", label: "Converted" },
];

export default function LeadsPage() {
  const [leads, setLeads] = useState<Lead[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedLead, setSelectedLead] = useState<(Lead & { activity_log: ActivityEntry[] }) | null>(null);
  const [filterTown, setFilterTown] = useState("");
  const [viewMode, setViewMode] = useState<"pipeline" | "list">("pipeline");

  useEffect(() => {
    loadLeads();
  }, [filterTown]);

  async function loadLeads() {
    setLoading(true);
    try {
      const params: Record<string, string> = {};
      if (filterTown) params.town = filterTown;
      const data = await getLeads(params);
      setLeads(data);
    } finally {
      setLoading(false);
    }
  }

  async function handleSelectLead(id: number) {
    const detail = await getLead(id);
    setSelectedLead(detail);
  }

  async function handleStatusChange(id: number, newStatus: string) {
    await updateLead(id, { status: newStatus });
    await loadLeads();
    setSelectedLead(null);
  }

  return (
    <div className="max-w-7xl">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-semibold text-white">Leads</h1>
        <div className="flex items-center gap-3">
          <input
            type="text"
            placeholder="Filter by town..."
            value={filterTown}
            onChange={(e) => setFilterTown(e.target.value)}
            className="bg-zinc-800 border border-zinc-700 rounded-lg px-3 py-2 text-sm text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-500 w-48"
          />
          <div className="flex bg-zinc-800 rounded-lg p-0.5">
            <button
              onClick={() => setViewMode("pipeline")}
              className={`px-3 py-1.5 rounded-md text-xs ${viewMode === "pipeline" ? "bg-zinc-700 text-white" : "text-zinc-400"}`}
            >
              Pipeline
            </button>
            <button
              onClick={() => setViewMode("list")}
              className={`px-3 py-1.5 rounded-md text-xs ${viewMode === "list" ? "bg-zinc-700 text-white" : "text-zinc-400"}`}
            >
              List
            </button>
          </div>
        </div>
      </div>

      {loading ? (
        <p className="text-zinc-500 text-sm">Loading...</p>
      ) : viewMode === "pipeline" ? (
        /* Pipeline View */
        <div className="flex gap-3 overflow-x-auto pb-4">
          {PIPELINE_COLUMNS.map((col) => {
            const columnLeads = leads.filter((l) => l.status === col.status);
            return (
              <div key={col.status} className="min-w-[200px] flex-shrink-0">
                <div className="flex items-center gap-2 mb-2">
                  <h3 className="text-xs font-medium text-zinc-500 uppercase">{col.label}</h3>
                  <span className="text-[10px] bg-zinc-800 text-zinc-400 px-1.5 py-0.5 rounded-full">
                    {columnLeads.length}
                  </span>
                </div>
                <div className="space-y-2">
                  {columnLeads.map((lead) => (
                    <LeadCard
                      key={lead.id}
                      lead={lead}
                      compact
                      onClick={() => handleSelectLead(lead.id)}
                    />
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      ) : (
        /* List View */
        <div className="space-y-2">
          {leads.map((lead) => (
            <LeadCard key={lead.id} lead={lead} onClick={() => handleSelectLead(lead.id)} />
          ))}
        </div>
      )}

      {/* Lead Detail Drawer */}
      {selectedLead && (
        <div className="fixed inset-0 z-50 flex justify-end">
          <div className="absolute inset-0 bg-black/50" onClick={() => setSelectedLead(null)} />
          <div className="relative w-[420px] bg-zinc-900 border-l border-zinc-800 h-full overflow-y-auto p-6">
            <div className="flex items-start justify-between mb-6">
              <div>
                <h2 className="text-lg font-medium text-white">{selectedLead.business_name}</h2>
                <p className="text-sm text-zinc-400">{selectedLead.town}</p>
              </div>
              <button onClick={() => setSelectedLead(null)} className="text-zinc-500 hover:text-white text-xl">
                &times;
              </button>
            </div>

            <div className="space-y-4">
              <div className="grid grid-cols-2 gap-3">
                {selectedLead.email && (
                  <div>
                    <p className="text-[10px] text-zinc-500 uppercase">Email</p>
                    <p className="text-sm text-white">{selectedLead.email}</p>
                  </div>
                )}
                {selectedLead.phone && (
                  <div>
                    <p className="text-[10px] text-zinc-500 uppercase">Phone</p>
                    <p className="text-sm text-white">{selectedLead.phone}</p>
                  </div>
                )}
                {selectedLead.website && (
                  <div className="col-span-2">
                    <p className="text-[10px] text-zinc-500 uppercase">Website</p>
                    <p className="text-sm text-blue-400">{selectedLead.website}</p>
                  </div>
                )}
                {selectedLead.score !== null && (
                  <div>
                    <p className="text-[10px] text-zinc-500 uppercase">Score</p>
                    <p className="text-2xl font-semibold text-white">{selectedLead.score}/100</p>
                  </div>
                )}
                <div>
                  <p className="text-[10px] text-zinc-500 uppercase">Status</p>
                  <p className="text-sm text-white capitalize">{selectedLead.status}</p>
                </div>
              </div>

              {/* Status Actions */}
              <div className="flex gap-2 pt-2">
                {selectedLead.status !== "converted" && (
                  <button
                    onClick={() => handleStatusChange(selectedLead.id, "converted")}
                    className="bg-emerald-600 text-white px-3 py-1.5 rounded-lg text-xs font-medium hover:bg-emerald-500"
                  >
                    Mark Converted
                  </button>
                )}
                {selectedLead.status !== "lost" && (
                  <button
                    onClick={() => handleStatusChange(selectedLead.id, "lost")}
                    className="bg-zinc-700 text-zinc-300 px-3 py-1.5 rounded-lg text-xs font-medium hover:bg-zinc-600"
                  >
                    Mark Lost
                  </button>
                )}
              </div>

              {/* Activity Log */}
              <div className="pt-4 border-t border-zinc-800">
                <h3 className="text-xs font-medium text-zinc-500 uppercase mb-3">Activity Log</h3>
                {selectedLead.activity_log.length === 0 ? (
                  <p className="text-xs text-zinc-600">No activity yet</p>
                ) : (
                  <div className="space-y-2">
                    {selectedLead.activity_log.map((entry, i) => (
                      <div key={i} className="flex gap-3">
                        <div className="w-1.5 h-1.5 rounded-full bg-zinc-600 mt-1.5 shrink-0" />
                        <div>
                          <p className="text-xs text-zinc-300">{entry.action}</p>
                          {entry.details && <p className="text-[10px] text-zinc-500">{entry.details}</p>}
                          <p className="text-[10px] text-zinc-600">{entry.timestamp}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
