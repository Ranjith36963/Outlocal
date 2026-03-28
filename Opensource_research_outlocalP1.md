# Open source toolkit for an AI-powered lead generation pipeline

**Building a complete cold outreach system from open source components is entirely feasible in 2026.** Across the 12 pipeline steps — from lead discovery through compliance — there are production-grade repositories covering roughly 80% of the workflow. The strongest open source coverage exists for business scraping (Step 1), website crawling (Step 2), CRM (Step 9), and email sending (Step 6). The weakest coverage is in lead scoring (Step 4), reply classification (Step 8), and AI email personalisation (Step 5), where most projects are reference implementations or require significant custom development. This report catalogues **90+ repositories** ranked by stars, activity, and production-readiness.

---

## Step 1: Lead discovery and business scraping

These tools scrape Google Maps, Yellow Pages, Yelp, and other directories to extract business contact data at scale.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) | **~3,500** | Mar 2026 (very active) | Production-grade Google Maps scraper with CLI, Web UI, REST API, and K8s deployment. Extracts name, address, phone, website, ratings, reviews, emails. | Go | MIT | CPU/memory-intensive headless browser; MacOS Docker issues; min 3-min runtime |
| [omkarcloud/google-maps-scraper](https://github.com/omkarcloud/google-maps-scraper) | **~2,500** | 2025–2026 | Desktop GUI extracting **50+ data points** from Google Maps including emails, phones, social profiles. Built on Botasaurus framework. | Python | Proprietary (free tier) | Enrichment features require paid API ($16/mo); not fully open source |
| [serpapi/google-maps-scraper](https://github.com/serpapi/google-maps-scraper) | ~100–200 | Maintained | SerpAPI's official scraper with clean structured JSON output for GPS coordinates, reviews, ratings, hours. | Python | MIT | **Requires paid SerpAPI key** — it's an API wrapper, not self-contained |
| [Zubdata/Google-Maps-Scraper](https://github.com/Zubdata/Google-Maps-Scraper) | ~100–200 | 2024–2025 | GUI tool built with Selenium/Chrome for scraping Google Maps business data. | Python | GPL-3.0 | Selenium-based (slower than Playwright); Chrome driver compatibility issues |
| [zohaibbashir/Google-Maps-Scrapper](https://github.com/zohaibbashir/Google-Maps-Scrapper) | ~50–150 | 2025 | Playwright-based Maps scraper with operating hours, delivery/pickup detection, append mode. | Python | Open source | DOM changes can break XPaths; not headless by default; rate limiting risk |
| [scrapehero/yellowpages-scraper](https://github.com/scrapehero/yellowpages-scraper) | ~200–300 | Maintained | Lightweight YellowPages.com scraper using requests + LXML. No browser needed. | Python | Open source | YellowPages-specific; no rate limiting or proxy rotation built in |
| [kaymen99/Yelp-scraper](https://github.com/kaymen99/Yelp-scraper) | ~20–50 | Maintained | Selenium + Flask app scraping Yelp business data including phones, websites, reviews. | Python | Open source | Yelp actively blocks scrapers; Selenium is heavy; small project |

**Top pick**: `gosom/google-maps-scraper` is the clear winner — MIT-licensed, Go-based, Docker/K8s-ready, REST API, actively maintained with **3,500+ stars**. It's the most production-ready Maps scraper available.

---

## Step 2: Website crawling and data extraction

Tools for crawling business websites to extract emails, phone numbers, social links, and technology stack information.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | **~60,000** | Mar 2026 (v0.8.x) | #1 trending open source crawler. AI-ready with LLM-optimised markdown output, async Playwright, CSS/XPath/LLM extraction strategies. | Python | Apache 2.0 | General-purpose — needs custom logic for email/phone extraction on top |
| [Lissy93/web-check](https://github.com/Lissy93/web-check) | **~32,000** | 2025–2026 | All-in-one OSINT tool: SSL analysis, DNS records, tech stack via Wappalyzer, performance metrics, security headers, 30+ checks. | JavaScript (React + Node) | MIT | Single-URL analysis, not batch processing; some checks require API keys |
| [champmq/TheScrapper](https://github.com/champmq/TheScrapper) | ~312 | 2024–2025 | Purpose-built OSINT tool extracting emails, phone numbers, and social media accounts from any website. | Python | Open source | No JS rendering; may miss dynamically loaded content; no tech stack detection |
| [s0md3v/wappalyzer-next](https://github.com/s0md3v/wappalyzer-next) | ~319 | Jan 2026 (v1.0.20) | Most accurate Wappalyzer alternative using actual browser extension fingerprints. CLI + Python library with fast/balanced/full scan modes. | Python | GPL-3.0 | Requires Firefox + geckodriver for full scan; GPL copyleft license |
| [Lissy93/wapalyzer](https://github.com/Lissy93/wapalyzer) | ~302 | Community fork | Community fork of original Wappalyzer. Maintains regex fingerprint DB identifying **2,500+ web technologies**. | JavaScript | GPL-3.0 | Original NPM package deprecated; CLI setup issues on some distros |
| [kevincobain2000/email_extractor](https://github.com/kevincobain2000/email_extractor) | ~200–400 | Maintained | Ultra-fast Go email extractor — crawls **1,000 URLs in ~11 seconds**. 10KB binary, configurable depth. | Go | MIT | Email-only (no phones/social); no JS rendering; command-line only |
| [vdrmota/Social-Media-and-Contact-Info-Extractor](https://github.com/vdrmota/Social-Media-and-Contact-Info-Extractor) | ~100–200 | Maintained | Apify-based crawler extracting emails, phones, Facebook, Twitter, Instagram, YouTube, LinkedIn links. | JavaScript | Open source | Requires Apify platform; not standalone; costs money at scale |

**Recommended combo**: Use **crawl4ai** as the crawling backbone, **TheScrapper** or **email_extractor** for contact extraction, and **wappalyzer-next** for technology detection. Add **web-check** for deep-dive analysis on high-priority leads.

---

## Step 3: Email finding and validation

Tools for discovering email addresses from domains, validating deliverability, and detecting disposable addresses.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [laramies/theHarvester](https://github.com/laramies/theHarvester) | **~15,900** | Feb 2026 (v4.10.0) | Premier OSINT tool gathering emails, names, subdomains from **30+ public sources** (Google, Bing, LinkedIn, HaveIBeenPwned). | Python | GPL-2.0 | Some sources require API keys; results depend on public indexing |
| [cjhutto/vaderSentiment](https://github.com/disposable-email-domains/disposable-email-domains) | **~3,200** | Continuously updated | Curated list of ~4,000 disposable/temporary email domains. Used by PyPI to block fake signups. Includes allowlist. | Text file (language-agnostic) | CC0 / Public Domain | Only ~4,000 domains (accuracy over coverage); requires integration code |
| [AfterShip/email-verifier](https://github.com/AfterShip/email-verifier) | **~1,500** | Mar 2026 | Most complete email verification library: syntax, MX lookup, SMTP check, disposable detection, free provider check, role account detection, catch-all detection. | Go | MIT | ISPs often block port 25; Yahoo doesn't allow mailbox verification |
| [truemail-rb/truemail](https://github.com/truemail-rb/truemail) | **~1,300** | Apr 2024 (stable) | Configurable email validator with layered approach: Regex → DNS → SMTP. Whitelists/blacklists, timeouts, detailed reporting. Has companion Rack web API server. | Ruby | MIT | Ruby-only; SMTP validation can be slow; some providers block verification |
| [disposable/disposable](https://github.com/disposable/disposable) | **~1,300** | Daily automated updates | Aggregated **~100,000 disposable email domains** from multiple sources. npm, Go, and Python packages included. | Python/JS/Go | MIT | Higher false-positive rate than curated lists; some legit services flagged |
| [sham00n/buster](https://github.com/sham00n/buster) | **~1,000** | Maintained | Email permutation generator + verifier. Checks social accounts (Gravatar, GitHub, LinkedIn, Skype), breach databases. | Python | GPL-3.0 | Relies on hunter.io API (200/day free); some verification sources unreliable |
| [maldevel/EmailHarvester](https://github.com/maldevel/EmailHarvester) | ~800–1,000 | Stable | Domain email retrieval from 6 search engines. Plugin system for Twitter, LinkedIn, GitHub, Instagram, Reddit. | Python | GPL-3.0 | Older codebase; some plugins need updating; rate limiting issues |
| [Josue87/EmailFinder](https://github.com/Josue87/EmailFinder) | ~200–500 | Maintained | Finds company emails via Google, Bing, Baidu search engines. Filters for @company.com patterns. CLI + library. | Python | GPL-3.0 | Depends on search engine availability and rate limits |
| [jacobgoh101/email-permutator](https://github.com/jacobgoh101/email-permutator) | ~50–100 | Stable | Generates **~34 email permutations** per name/domain pair (john.doe@, jdoe@, doe.john@, etc.). | JavaScript (Node.js) | MIT | No validation itself; limited to Western name formats; no bulk processing |

**Best pipeline**: theHarvester (discovery) → email-permutator (generate candidates) → AfterShip/email-verifier (validate via SMTP/MX) → disposable-email-domains (filter throwaway addresses). Note that **ISP port 25 blocking** is a universal limitation — use a VPS for SMTP verification.

---

## Step 4: Lead scoring and qualification

ML-based scoring models, CRM scoring features, and reference implementations for ranking sales leads.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [pycaret/pycaret](https://github.com/pycaret/pycaret) | **~9,700** | Apr 2025 | Low-code ML library wrapping scikit-learn, XGBoost, LightGBM, CatBoost. Has **documented lead scoring tutorials** using classification models. | Python | MIT | General-purpose ML (not lead-scoring specific); needs training data |
| [mautic/mautic](https://github.com/mautic/mautic) | **~9,400** | Mar 2026 (v7.1 RC) | Marketing automation with **native contact point scoring** — assigns points based on page visits, form submissions, email opens, custom rules. | PHP (Symfony) | GPL-3.0 | Complex to self-host; steep learning curve; PHP-based |
| [salesagility/SuiteCRM](https://github.com/salesagility/SuiteCRM) | **~4,500** | Active | Enterprise CRM with full lead lifecycle management, workflow engine for rule-based scoring, and REST API for external ML integration. | PHP | AGPL-3.0 | No native ML scoring; requires extensions for predictive scoring |
| [rh-marketingops/mlsm](https://github.com/rh-marketingops/mlsm) | ~50–80 | Reference | Red Hat's Multiple Lead Score Models framework. Standardised architecture for deploying concurrent scoring models with version control. | Python | MIT | Small community; designed for Red Hat's OpenShift; limited docs |
| [calvdee/end-to-end-lead-scoring](https://github.com/calvdee/end-to-end-lead-scoring) | ~100–150 | Reference | Enterprise data science project demonstrating the CoNVO framework, financial modelling of costs/benefits, and experiment design for lead scoring. | Python (Jupyter) | MIT | Reference only; no production deployment code |
| [joehoeller/Machine-Learning-For-Predictive-Lead-Scoring](https://github.com/joehoeller/Machine-Learning-For-Predictive-Lead-Scoring) | ~50–80 | Reference | B2B predictive lead scoring with propensity models. Covers theory, implementation, and deployment considerations. | Python | Not specified | More documentation/theory than runnable code |

**Important finding**: No high-star standalone "lead scoring library" exists on GitHub. The space is split between **CRM platforms with built-in scoring** (Mautic) and **ML frameworks applied to scoring** (PyCaret). The practical path is to use **Mautic for rule-based scoring** (page visits = X points, form fill = Y points) combined with **PyCaret for building a predictive ML model** that feeds scores back via Mautic's API.

---

## Step 5: AI email personalisation and generation

LLM-powered tools that generate personalised cold outreach based on lead-specific data — not just templates.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [filip-michalsky/SalesGPT](https://github.com/filip-michalsky/SalesGPT) | **~2,500** | Early 2025 (slowing) | Context-aware AI sales agent understanding sales stages (intro → qualification → objection handling → close). Supports email, voice, SMS. Uses RAG to reduce hallucinations. Multi-LLM via LiteLLM. | Python (LangChain, FastAPI) | MIT | Development slowing; more conversational agent than pure email tool |
| [IST-DASLab/PanzaMail](https://github.com/IST-DASLab/PanzaMail) | ~350 | 2024–2025 | Fine-tunes an LLM on your past emails to **match your writing style**, then uses RAG for contextual generation. Runs locally on single GPU. | Python (PyTorch, HuggingFace) | Apache 2.0 | Requires GPU (16–24GB VRAM); designed for replies not cold outreach |
| [The-Pocket/PocketFlow-Tutorial-Cold-Email-Personalization](https://github.com/The-Pocket/PocketFlow-Tutorial-Cold-Email-Personalization) | ~200+ | 2025 | Researches prospects via web search, analyses for personalisation opportunities, generates custom openers. Batch CSV processing + Streamlit UI. | Python (PocketFlow, Claude/Gemini) | MIT | Tutorial-quality; generates openers only; 30–60s per prospect |
| [codebasics/project-genai-cold-email-generator](https://github.com/codebasics/project-genai-cold-email-generator) | ~130 | 2024 (stable) | Uses **Llama 3.1 + ChromaDB** to scrape career pages, extract job listings, generate cold emails with matched portfolio links from a vector database. | Python (Streamlit, LangChain, Groq) | MIT (commercial restricted) | Job-posting focused; commercial use prohibited; requires Groq API key |
| [MatthewDailey/open-sdr](https://github.com/MatthewDailey/open-sdr) | ~70 | 2025 | MCP-based AI SDR that uses Firecrawl for research + Claude for analysis + Gemini for processing. Multi-agent architecture researches and generates personalised outreach. | TypeScript (MCP, Node.js) | MIT | Very new; requires 3 API keys; small community; no email sending |
| [fichel/sdr-agent](https://github.com/fichel/sdr-agent) | ~15 | 2025 | Hierarchical agent system: Sales Manager → Sales Rep → Email Agent. Gradio UI. Sends via SendGrid. OpenAI trace logging. | Python (OpenAI, Gradio) | MIT | Small project; locked to OpenAI; no lead research/enrichment |

**Key gap**: No mature, high-star open source project handles AI-personalised cold email generation end-to-end. **SalesGPT** is the most mature but development has slowed. The practical approach is combining **PocketFlow's prospect-research pattern** with a custom LLM pipeline using LangChain or similar orchestration.

---

## Step 6: Email sending and deliverability

Infrastructure for sending cold emails at scale with rate limiting, authentication, domain warming, and bounce handling.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [knadh/listmonk](https://github.com/knadh/listmonk) | **~19,100** | Mar 2025 (v5.0.3) | High-performance mailing system. Multi-threaded multi-SMTP queues, **sliding window rate limiting**, bounce tracking, SQL segmentation. Used by Zerodha for millions monthly. Single Go binary + PostgreSQL. | Go + Vue.js | AGPL-3.0 | Newsletter-focused; no domain warming; no DKIM management; AGPL license |
| [postalserver/postal](https://github.com/postalserver/postal) | **~16,400** | Feb 2026 (v3.3.5) | Full mail delivery platform (self-hosted Sendgrid/Mailgun). Detailed delivery tracking, bounce processing, click/open tracking, webhooks. | Ruby (Rails) | MIT | Complex self-hosting; MTA not campaign manager; requires DNS configuration |
| [mautic/mautic](https://github.com/mautic/mautic) | **~9,400** | Mar 2026 | Marketing automation with built-in **DKIM configuration**, domain management, bounce/complaint handling via SES/SendGrid/Mailgun webhooks, campaign scheduling. | PHP (Symfony) | GPL-3.0 | Complex setup; resource-heavy; no inbox rotation or domain warming |
| [Mailtrain-org/mailtrain](https://github.com/Mailtrain-org/mailtrain) | **~5,700** | Apr 2025 | Self-hosted newsletter app with **bundled ZoneMTA** for SMTP delivery, DKIM signing configuration, SPF guidance, bounce handling via webhooks. | JavaScript (Node.js) | GPL-3.0 | Dated UI; requires more resources than listmonk; less active community |
| [domainaware/checkdmarc](https://github.com/domainaware/checkdmarc) | **~600** | 2025 | Validates SPF and DMARC DNS records. Parses record syntax, checks misconfigurations, supports bulk domain scanning. pip + Docker. | Python | Apache 2.0 | Validation only (doesn't configure records); no DKIM checking |
| [GlobalCyberAlliance/DomainSecurityScanner](https://github.com/GlobalCyberAlliance/DomainSecurityScanner) | ~200 | 2025 | Scans domains for **DKIM + DMARC + SPF + BIMI**. Provides remediation advice. CLI, REST API, Docker. | Go | Apache 2.0 | Read-only scanning; advisory only; no email sending capabilities |
| [PaulleDemon/Email-automation](https://github.com/PaulleDemon/Email-automation) | ~150 | 2024–2025 | Cold email outreach tool with Jinja2 templates, scheduling, follow-up sequences, Celery async processing. | Python (Django, Celery) | MIT | No domain warming or inbox rotation; relies on external SMTP |
| [WKL-Sec/Warmer](https://github.com/WKL-Sec/Warmer) | ~100 | 2024 | Email domain warmup automation. Configurable volume, AI-generated content mode, single/bulk targets. | Python (Selenium) | Not specified | Outlook-focused; Selenium-based; not scalable for many accounts |
| [pypes-dev/coldflow](https://github.com/pypes-dev/coldflow) | ~50 | 2025 | Purpose-built cold email platform with **inbox rotation**, safe sending limits, reply tracking, follow-up automation. | TypeScript (Next.js) | Open source | Very new; features may be incomplete; small community |

**Recommended stack**: **listmonk** for high-volume sending infrastructure + **checkdmarc** and **DomainSecurityScanner** for authentication validation + **Warmer** for domain warmup. For a purpose-built cold email tool with inbox rotation, watch **Coldflow** — it's the only OSS project targeting this exact use case.

---

## Step 7: Follow-up automation

Automated email sequences, reply detection, drip campaigns, and multi-step outreach with conditional logic.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | **~181,000** | Mar 2026 (very active) | Workflow automation with 400+ integrations and **native AI/LLM nodes**. Build multi-step email flows with conditional branching, reply detection via IMAP, and AI-generated follow-ups. | TypeScript (Node.js) | Sustainable Use License | Not email-specific; requires building from scratch; not fully open source |
| [mautic/mautic](https://github.com/mautic/mautic) | **~9,400** | Mar 2026 | Visual campaign builder with **conditional logic** (if no reply → send follow-up), drip sequences, behavioural triggers, A/B testing. | PHP (Symfony) | GPL-3.0 | Complex setup; no native AI-generated content; steep learning curve |
| [filip-michalsky/SalesGPT](https://github.com/filip-michalsky/SalesGPT) | **~2,500** | Early 2025 | AI sales agent understanding conversation stages. Generates contextually-aware follow-up emails based on conversation history. | Python (LangChain) | MIT | Low recent activity; more conversational than sequence-based |
| [agnitas-org/openemm](https://github.com/agnitas-org/openemm) | ~350 | 2024–2025 | Web-based email automation with **multi-stage campaigns**, autoresponders, date-driven emails. Unlimited contacts. | Java | CPAL | Complex Java setup; dated UI; smaller community |
| [joshmn/caffeinate](https://github.com/joshmn/caffeinate) | ~360 | Stable | Rails engine specifically for drip campaigns. DSL for sequences with **timezone-aware timing**, business-day support, skip/unsubscribe logic. | Ruby on Rails | MIT | Rails-only; no standalone UI; no AI content generation |
| [PaulleDemon/Email-automation](https://github.com/PaulleDemon/Email-automation) | ~124 | Sep 2024 | Cold email outreach with **scheduled follow-ups and follow-up rules**, Jinja2 conditional templates. | Python (Django, Celery) | MIT | Basic follow-up logic; no reply detection; requires Celery/Redis |
| [kaymen99/langgraph-email-automation](https://github.com/kaymen99/langgraph-email-automation) | ~80 | 2024–2025 | Multi-AI agent system categorising emails and drafting **personalised responses** using RAG for product-aware answers. | Python (LangGraph) | MIT | Demo project; not production sequence tool; requires LLM API costs |
| [kaymen99/sales-outreach-automation-langgraph](https://github.com/kaymen99/sales-outreach-automation-langgraph) | ~30 | 2024–2025 | AI sales outreach system automating lead research + qualification + **personalised outreach** with CRM integration (HubSpot, Airtable). | Python (LangGraph) | MIT | Small demo; needs customisation for production; LLM costs |

**Best approach**: Use **n8n** (181k stars) as the orchestration backbone — its visual workflow builder can chain IMAP polling → reply detection → conditional branching → LLM nodes for AI follow-up generation → email sending. Supplement with **Mautic** if you need a pre-built campaign builder with native drip sequences.

---

## Step 8: Reply classification and intent detection

NLP/LLM tools for classifying email replies as interested, not interested, out-of-office, or unsubscribe.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [RasaHQ/rasa](https://github.com/RasaHQ/rasa) | **~19,000** | 2025–2026 | Conversational AI framework with NLU (intent classification + entity extraction). DIET classifier, BERT support, production HTTP API. | Python | Apache 2.0 | Designed for chatbots; heavy dependency footprint for classification-only use |
| [sloria/TextBlob](https://github.com/sloria/TextBlob) | **~9,100** | Stable | Simple NLP library with sentiment analysis (polarity/subjectivity), POS tagging, and **Naive Bayes text classification** trainable on custom categories. | Python | MIT | Basic models; not state-of-the-art; classification needs training data |
| [cjhutto/vaderSentiment](https://github.com/cjhutto/vaderSentiment) | **~4,500** | Stable | Lexicon-based sentiment analyser returning compound/positive/negative/neutral scores. No training data needed. | Python | MIT | Can't distinguish fine-grained intents (OOO vs unsubscribe); lexicon-only |
| [snipsco/snips-nlu](https://github.com/snipsco/snips-nlu) | **~3,900** | Archived (~2020) | Lightweight, privacy-focused intent classification and slot filling. Competitive with Dialogflow/LUIS. | Python | Apache 2.0 | **Archived/unmaintained**; dependency issues with newer Python versions |
| [xiamx/awesome-sentiment-analysis](https://github.com/xiamx/awesome-sentiment-analysis) | **~1,100** | Periodically updated | Curated list of sentiment analysis methods, implementations, tools, and datasets across multiple approaches. | N/A (list) | N/A | Meta-resource only; not a tool itself |
| [thuml/TEXTOIR](https://github.com/thuml/TEXTOIR) | **~500** | 2022 | First toolkit for **text open intent recognition** (ACL 2021). Handles both known intents and unknown/out-of-domain detection. | Python (PyTorch) | MIT | Academic project; last updated 2022; requires deep learning expertise |
| [ParakweetLabs/EmailIntentDataSet](https://github.com/ParakweetLabs/EmailIntentDataSet) | ~100 | 2017 (dataset) | Labelled training/test data for email intent ML based on Enron corpus speech acts. | Data (ARFF) | Open source | Old dataset; binary classification only; not sales-specific |
| [SerjSmor/open-intent-classifier](https://github.com/SerjSmor/open-intent-classifier) | ~60 | 2025–2026 | **Zero-shot and few-shot intent classifier** with dynamic labels. Supports embeddings, OpenAI, DSPy, SmolLM2 backends. No pretraining needed. | Python | MIT | Small community; not email-specific; quality depends on backend model |
| [shxntanu/email-classifier](https://github.com/shxntanu/email-classifier) | ~15 | 2024 | LLM-based email classification + auto-routing using Mixtral/Llama3 with Celery/RabbitMQ distributed queues. Barclays hackathon winner. | Python (Flask, Ollama) | MIT | Hackathon project; enterprise-focused (dept routing) not sales-focused |

**Key gap**: No widely-adopted open source project exists specifically for **sales email reply classification**. The most practical approach is using **open-intent-classifier** for zero-shot classification with labels like ["Interested", "Not Interested", "Out of Office", "Unsubscribe"] — or simply prompting an LLM via **n8n's AI nodes** or a LangChain pipeline. For a production system, **Rasa** provides the most robust framework if you invest in sales-specific training data.

---

## Step 9: CRM and pipeline tracking

Lightweight, API-first CRM systems suited for solo founders and small outbound teams.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | **~40,600** | Mar 2026 (very active) | Modern Salesforce alternative. **PostgreSQL backend**, GraphQL + REST API, kanban views, Notion/Linear-inspired UX. | TypeScript (React, NestJS, GraphQL) | BSL (Business Source License) | BSL restricts commercial SaaS redistribution; large codebase |
| [monicahq/monica](https://github.com/monicahq/monica) | **~24,300** | Mar 2026 (v5 beta) | Personal Relationship Management — tracks interactions, calls, notes, reminders per contact. | PHP (Laravel), Vue.js | AGPL-3.0 | Personal CRM, not sales pipeline; v4→v5 transition with no migration path |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | **~21,900** | Mar 2026 (v2.2.0) | Full sales CRM: leads, contacts, orgs, activities, **sales pipeline kanban**, email parsing, dashboards, REST API. Built by Webkul (650+ employees). | PHP (Laravel 12), Vue.js | **MIT** | PHP/Laravel stack; WhatsApp/VoIP extensions are paid add-ons |
| [salesagility/SuiteCRM](https://github.com/salesagility/SuiteCRM) | **~4,500** | Active | Most widely adopted open source enterprise CRM. Full sales, marketing, customer service with workflow automation and REST API v8. | PHP | AGPL-3.0 | Heavy for solo founders; MySQL/MariaDB only; older UI |
| [erxes/erxes](https://github.com/erxes/erxes) | **~3,900** | 2025–2026 | All-in-one HubSpot alternative: CRM + marketing automation + omnichannel inbox + knowledge base. Plugin architecture. | TypeScript (React, Node.js, GraphQL) | AGPL-3.0 (SaaS restricted) | MongoDB (not PostgreSQL); complex microservices; heavy resources |
| [espocrm/espocrm](https://github.com/espocrm/espocrm) | **~2,800** | Mar 2026 | Lightweight CRM with leads, contacts, accounts, opportunities, calendar, email integration, kanban, REST API. **Supports PostgreSQL.** | PHP, JavaScript (Backbone.js) | GPL-3.0 | Smaller community; older Backbone.js frontend; limited plugins |
| [frappe/crm](https://github.com/frappe/crm) | **~2,500** | Mar 2026 | Modern CRM on Frappe framework (ERPNext ecosystem). Leads, deals, contacts, pipeline views, Vue.js 3 frontend. | Python (Frappe), Vue.js 3 | AGPL-3.0 | Requires Frappe framework; MariaDB default (not PostgreSQL) |
| [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | **~8,300** | 2025–2026 | ERP + CRM + invoicing. Customer management, lead tracking, quotes, invoices, payments with REST API. | JavaScript (Node.js, React) | AGPL-3.0 | MongoDB; ~25% truly open per community reports; CRUD limitations |

**Best fit for solo founders**: **Twenty** (40k stars, PostgreSQL, API-first, modern UX) or **Krayin CRM** (22k stars, MIT license, full sales pipeline). Twenty is the most modern and developer-friendly option but note its BSL license. Krayin offers the best MIT-licensed sales CRM.

---

## Step 10: Multi-channel outreach across LinkedIn, WhatsApp, and SMS

Automation tools for LinkedIn, WhatsApp, SMS, and cross-channel sequencing.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | **~8,700** | Mar 2026 (v7.0.0-rc.9) | WebSocket-based WhatsApp Web API. Send/receive messages, media, polls, reactions — **no browser needed**. Most popular OSS WhatsApp library. | TypeScript (Node.js) | MIT | ⚠️ Unofficial — violates WhatsApp ToS; account ban risk; no campaign management |
| [laudspeaker/laudspeaker](https://github.com/laudspeaker/laudspeaker) | **~3,500** | Active | Multi-channel customer engagement (Braze/Customer.io alternative). Visual **journey builder** for email + SMS + push + webhooks. A/B testing. **500M+ messages sent.** | TypeScript (NestJS, React) | MIT | No native LinkedIn or WhatsApp channels; requires Twilio/SendGrid |
| [tomquirk/linkedin-api](https://github.com/tomquirk/linkedin-api) | **~2,000** | Nov 2024 (PyPI) | Unofficial Python library for LinkedIn's Voyager API. Search profiles, send messages, manage connections — direct HTTP, no Selenium. | Python | MIT | ⚠️ Violates LinkedIn ToS; ~900 requests/session; challenge URLs may block logins |
| [eracle/OpenOutreach](https://github.com/eracle/OpenOutreach) | **~1,135** | Mar 2026 | AI-powered LinkedIn automation: autonomous search → qualify → connect → personalised messages. **Gaussian Process model** learns ideal customer profile. Built-in Django CRM. | Python (Django, Playwright) | GPL-3.0 | ⚠️ Violates LinkedIn ToS; requires LLM API key; single-account only |
| [parcelvoy/platform](https://github.com/parcelvoy/platform) | ~500 | Active | Multi-channel marketing automation: email, SMS, push, webhooks. Journey builder, segmentation. **PostgreSQL backend**. REST API + SDKs. | TypeScript | MIT | No LinkedIn or WhatsApp; smaller community; requires Twilio for SMS |
| [linkedin-developers/linkedin-api-python-client](https://github.com/linkedin-developers/linkedin-api-python-client) | ~200 | Maintained (beta) | **Official** LinkedIn API client with proper OAuth 2.0/3.0. For marketing APIs, ads, Sign In with LinkedIn. | Python | Apache 2.0 | Very limited scope — no messaging or connection automation; requires developer app approval |
| [fazer-ai/baileys-api](https://github.com/fazer-ai/baileys-api) | ~100 | 2025–2026 | REST API wrapper around Baileys for WhatsApp. Multi-device, webhooks, Redis sessions, Swagger docs, Docker-ready. | TypeScript (Express, Prisma) | MIT | Same ToS risks as Baileys; early development; no campaign management |

**⚠️ Critical compliance note**: LinkedIn and WhatsApp automation tools carry **significant platform risk** — both platforms prohibit automated messaging and enforce account bans. For compliant LinkedIn integration, use the official API client (limited scope). For WhatsApp, consider the official WhatsApp Business API instead of Baileys for production use. **No single tool covers all channels** — use **Laudspeaker** or **n8n** as an orchestration layer to coordinate email + SMS + social.

---

## Step 11: Campaign analytics and reporting

Dashboards, tracking pixels, A/B testing frameworks, and performance reporting for outreach campaigns.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [knadh/listmonk](https://github.com/knadh/listmonk) | **~19,200** | Mar 2026 (v5.0.3) | Built-in analytics dashboard visualising campaign performance, bounce rates, top links. Tracks opens/clicks per campaign. | Go + Vue.js | AGPL-3.0 | No A/B testing for subject lines; analytics are campaign-level only |
| [postalserver/postal](https://github.com/postalserver/postal) | **~16,400** | Feb 2026 (v3.3.5) | Mail delivery platform with **detailed delivery tracking**, bounce processing, click/open tracking via webhooks. | Ruby (Rails) | MIT | MTA-level tracking; needs separate visualisation for aggregate reporting |
| [Unleash/unleash](https://github.com/Unleash/unleash) | **~13,200** | Daily commits, Mar 2026 | Largest OSS feature management platform. Feature flags, gradual rollouts, **A/B testing with variants**. GDPR/Schrems II compliant. | TypeScript (Node.js) | Apache 2.0 | Not email-specific; requires integration work; analytics need external provider |
| [mautic/mautic](https://github.com/mautic/mautic) | **~9,100** | Jan 2026 (v7.0.0) | Comprehensive email analytics: open rates, click rates, bounces, unsubscribes. **Built-in A/B testing for emails.** Visual campaign reporting. | PHP (Symfony) | GPL-3.0 | High complexity; resource-intensive; steep learning curve |
| [growthbook/growthbook](https://github.com/growthbook/growthbook) | **~7,300** | Daily commits, Mar 2026 | A/B testing with **world-class statistics engine** (CUPED, Sequential, Bayesian). Warehouse-native analytics. Auto-alerts on significance. **24 SDKs.** | TypeScript (Node.js) | MIT (Open Core) | Not email-specific; requires data warehouse; enterprise features paid |
| [Mailtrain-org/mailtrain](https://github.com/Mailtrain-org/mailtrain) | **~5,700** | 2024–2025 | Campaign analytics with open/click tracking. Subscriber segmentation. Template management with drag-and-drop editor. | JavaScript (Node.js) | GPL-3.0 | Less actively maintained; complex v2 setup |
| [aaPanel/BillionMail](https://github.com/aaPanel/BillionMail) | **~3,000+** | 2025–2026 (growing rapidly) | All-in-one mail server + email marketing with **analytics dashboard**, campaign tracking. Docker-based, 8-minute installation. | Go/Docker | AGPL-3.0 | Newer project; less battle-tested; feature set still maturing |
| [phpList/phplist3](https://github.com/phpList/phplist3) | ~833 | Maintained | Email marketing manager used in 95 countries. Real-time analytics, bounce processing, content personalisation. **25B+ messages sent.** | PHP | AGPL-3.0 | Dated UI; phpList 4 rewrite incomplete; lower GitHub activity |
| [dockwa/openpixel](https://github.com/dockwa/openpixel) | ~700 | 2023–2024 | Customisable JavaScript tracking pixel library. Handles cookies, UTM tracking, beacons, page analytics. | JavaScript | MIT | Web-focused, not email-specific; needs customisation; no dashboard |
| [powergo/pytracking](https://github.com/powergo/pytracking) | ~200 | 2024 | Python library for **email open and click tracking** via tracking pixels and redirect links. Stateless — all data encoded in URLs. Django integration. | Python | MIT | Library only — no dashboard; requires building analytics layer |

**Best stack**: **Mautic** for all-in-one campaign analytics with built-in A/B testing, or **listmonk** for lightweight tracking + **GrowthBook** for rigorous A/B testing with proper statistical significance. Use **pytracking** if building custom tracking into your own pipeline.

---

## Step 12: Compliance engine for GDPR and CAN-SPAM

Consent management, unsubscribe handling, data retention, and privacy frameworks.

| Repository | ⭐ Stars | Last Active | What It Does | Language | License | Limitations |
|---|---|---|---|---|---|---|
| [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler) | **~11,000** | Daily, Mar 2026 | Cloud security platform with automated **GDPR compliance checks** alongside PCI-DSS, HIPAA, SOC2. Continuous monitoring. | Python | Apache 2.0 | Infrastructure-focused; doesn't handle email consent or CAN-SPAM directly |
| [mautic/mautic](https://github.com/mautic/mautic) | **~9,100** | Jan 2026 | Built-in GDPR features: **consent tracking, data portability, right to erasure**. Unsubscribe management, double opt-in, contact preference centres. | PHP (Symfony) | GPL-3.0 | Can't use compliance features independently of the marketing platform |
| [orestbida/cookieconsent](https://github.com/orestbida/cookieconsent) | **~5,300** | 2025–2026 (v3.x) | Lightweight GDPR/CCPA cookie consent. Zero dependencies. **Google Consent Mode v2**. Auto-detects language. Records consent for audit. | JavaScript | MIT | Cookie/web only; no email unsubscribe management |
| [osano/cookieconsent](https://github.com/osano/cookieconsent) | **~3,500** | v4.x | Most popular consent project — **seen 2B+ times/month**. GeoIP-based consent type. REST API for consent searching. 3rd party script blocking. | JavaScript | ISC | Open source version limited vs hosted platform; no email-specific consent |
| [AmauriC/tarteaucitron.js](https://github.com/AmauriC/tarteaucitron.js) | **~2,500** | 2025–2026 (v1.25+) | GDPR cookie/tag manager with **95+ built-in service integrations**. Per-service granular consent. 100+ contributors. | JavaScript | MIT | Primarily French community/docs; cookie-focused only |
| [kiprotect/klaro](https://github.com/kiprotect/klaro) | **~1,400** | 2024–2025 | Privacy-friendly consent manager with per-service control. Supports **IAB consent framework**. Multi-language. JS API for programmatic consent. | JavaScript | BSD-3-Clause | Commercial version (Klaro Pro) has additional features; cookie-focused |
| [LINCnil/GDPR-Developer-Guide](https://github.com/LINCnil/GDPR-Developer-Guide) | ~500 | Periodic updates | **Official GDPR guide from France's CNIL** data protection authority. 16 thematic sheets covering development lifecycle. | Markdown/Docs | GPL-3.0 | Documentation only; not software; requires manual implementation |
| [appnexus/cmp](https://github.com/appnexus/cmp) | ~200 | Reference | IAB TCF reference implementation. Consent Management Platform for GDPR/ePrivacy in advertising. Standardised consent strings. | JavaScript | Apache 2.0 | Ad-tech focused; reference implementation needs customisation |
| [getprobo/probo](https://github.com/getprobo/probo) | Growing | 2025–2026 | Compliance platform for SOC2, GDPR, ISO27001. Audit trails, evidence collection, trust centre. Designed for startups. | Go | Open source | Early development; not production-ready; organisational compliance focus |

**Important finding**: No dedicated open source CAN-SPAM compliance tool exists with significant adoption. CAN-SPAM requirements (unsubscribe links, physical address, honest subject lines) are handled as features within email platforms like **Mautic** and **listmonk**. For a comprehensive compliance stack: use **Mautic** for email-specific GDPR compliance (consent tracking, unsubscribe, right to erasure) + **orestbida/cookieconsent** for web consent + **CNIL's GDPR Developer Guide** as an authoritative reference for privacy-by-design patterns.

---

## How these pieces fit together

The 12 steps form a clear data pipeline where each stage feeds the next. Here's the optimal open source stack based on this research:

- **Discovery → Enrichment**: `gosom/google-maps-scraper` → `crawl4ai` + `wappalyzer-next` + `theHarvester` → `AfterShip/email-verifier`
- **Scoring → Personalisation**: `Mautic` (rule-based scoring) + `PyCaret` (ML scoring) → `SalesGPT` or custom LangChain pipeline for AI email generation
- **Sending → Follow-up**: `listmonk` or `Postal` for delivery → `n8n` for orchestrating conditional follow-up sequences with LLM-generated content
- **Classification → CRM**: `open-intent-classifier` or LLM-based classification via n8n → `Twenty` or `Krayin CRM` for pipeline tracking
- **Analytics → Compliance**: `GrowthBook` for A/B testing + `Mautic` for campaign analytics → `Mautic` + `orestbida/cookieconsent` for GDPR/CAN-SPAM

Three tools appear across multiple steps — **Mautic** (scoring, sending, follow-ups, analytics, compliance), **n8n** (follow-ups, orchestration, classification), and **listmonk** (sending, analytics) — making them the backbone of any open source outreach stack. The weakest links remain **AI email personalisation** and **sales reply classification**, where commercial tools still lead and custom development is required to close the gap.