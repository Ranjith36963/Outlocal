"use client";

import { useEffect, useState } from "react";
import { getHealth } from "@/lib/api";

export default function SettingsPage() {
  const [service, setService] = useState("Web development and SEO for local UK businesses");
  const [businessName, setBusinessName] = useState("");
  const [saved, setSaved] = useState(false);
  const [backendStatus, setBackendStatus] = useState<"connected" | "disconnected" | "checking">("checking");
  const [backendVersion, setBackendVersion] = useState("");

  useEffect(() => {
    // Load saved settings from localStorage
    const savedService = localStorage.getItem("outlocal_service");
    const savedBusiness = localStorage.getItem("outlocal_business");
    if (savedService) setService(savedService);
    if (savedBusiness) setBusinessName(savedBusiness);

    // Check backend
    getHealth()
      .then((h) => {
        setBackendStatus("connected");
        setBackendVersion(h.version);
      })
      .catch(() => setBackendStatus("disconnected"));
  }, []);

  function handleSave() {
    localStorage.setItem("outlocal_service", service);
    localStorage.setItem("outlocal_business", businessName);
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  }

  return (
    <div className="max-w-2xl">
      <h1 className="text-2xl font-semibold text-white mb-6">Settings</h1>

      {/* Service Config */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 mb-6">
        <h2 className="text-sm font-medium text-zinc-300 mb-4">Your Service</h2>
        <div className="space-y-4">
          <div>
            <label className="block text-xs text-zinc-500 mb-1">Business Name</label>
            <input
              type="text"
              value={businessName}
              onChange={(e) => setBusinessName(e.target.value)}
              placeholder="Your Company Ltd"
              className="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-3 py-2.5 text-sm text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-500"
            />
          </div>
          <div>
            <label className="block text-xs text-zinc-500 mb-1">
              What service do you offer? (used in AI email generation)
            </label>
            <textarea
              value={service}
              onChange={(e) => setService(e.target.value)}
              rows={3}
              className="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-3 py-2.5 text-sm text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-500 resize-none"
            />
          </div>
          <button
            onClick={handleSave}
            className="bg-white text-zinc-900 px-4 py-2 rounded-lg text-sm font-medium hover:bg-zinc-200 transition-colors"
          >
            {saved ? "Saved!" : "Save Settings"}
          </button>
        </div>
      </div>

      {/* System Status */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6">
        <h2 className="text-sm font-medium text-zinc-300 mb-4">System Status</h2>
        <div className="space-y-3">
          <div className="flex items-center justify-between py-2 border-b border-zinc-800">
            <span className="text-sm text-zinc-400">FastAPI Backend</span>
            <div className="flex items-center gap-2">
              <div
                className={`w-2 h-2 rounded-full ${
                  backendStatus === "connected"
                    ? "bg-emerald-400"
                    : backendStatus === "checking"
                      ? "bg-amber-400"
                      : "bg-red-400"
                }`}
              />
              <span className="text-xs text-zinc-400">
                {backendStatus === "connected"
                  ? `Connected (v${backendVersion})`
                  : backendStatus === "checking"
                    ? "Checking..."
                    : "Disconnected"}
              </span>
            </div>
          </div>

          <div className="flex items-center justify-between py-2 border-b border-zinc-800">
            <span className="text-sm text-zinc-400">AI Engine (Groq)</span>
            <span className="text-xs text-zinc-500">Configured via .env</span>
          </div>

          <div className="flex items-center justify-between py-2 border-b border-zinc-800">
            <span className="text-sm text-zinc-400">AI Engine (OpenRouter)</span>
            <span className="text-xs text-zinc-500">Configured via .env</span>
          </div>

          <div className="flex items-center justify-between py-2 border-b border-zinc-800">
            <span className="text-sm text-zinc-400">AI Engine (Gemini)</span>
            <span className="text-xs text-zinc-500">Configured via .env</span>
          </div>

          <div className="flex items-center justify-between py-2">
            <span className="text-sm text-zinc-400">SMTP Email</span>
            <span className="text-xs text-zinc-500">Configured via .env</span>
          </div>
        </div>
      </div>
    </div>
  );
}
