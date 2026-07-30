# SENTRY - Security Monitoring & Threat Intelligence Platform

SENTRY is the core platform of **CyberillSec**, the Threat Intelligence pillar of the CYBERILL ecosystem.

## Architecture

```
sentry/
├── app/               # FastAPI application core
│   ├── main.py        # Entry point
│   ├── config.py      # Pydantic settings
│   ├── database.py    # SQLAlchemy engine
│   └── models/        # SQLAlchemy models
├── modules/           # Feature modules
│   ├── threat_feeds/  # TI feed collection
│   ├── cve_tracker/   # CVE monitoring
│   ├── incidents/     # Incident management
│   ├── dashboard/     # SOC dashboard
│   └── threat_hunting/ # Threat hunting
├── cli/               # Click CLI commands
├── shared/            # Shared utilities
└── tests/             # Test suite
```

## Quick Start

```bash
cd sentry
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
