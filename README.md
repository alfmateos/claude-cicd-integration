# Claude Code CI/CD Demo

A minimal Python project demonstrating how to integrate **Claude Code** (headless mode)
into a CI/CD pipeline — runnable locally via Docker Compose, or in the cloud via
GitHub Actions or GitLab CI.

## Project structure

```
├── src/
│   ├── __init__.py
│   └── calculator.py          # Simple module under review
├── tests/
│   ├── __init__.py
│   └── test_calculator.py     # Existing pytest suite
├── Dockerfile.claude-ci       # Claude Code runner image
├── docker-compose.yml         # ★ Local standalone pipeline
├── .github/workflows/
│   └── claude-ci.yml          # ★ GitHub Actions pipeline
├── .gitlab-ci.yml             # ★ GitLab CI pipeline
├── requirements.txt
└── .env.example               # API key template
```

## Quick start (local, standalone)

```bash
# 1. Copy and fill in your API key
cp .env.example .env
# edit .env → paste your ANTHROPIC_API_KEY

# 2. Run the full pipeline
docker compose up --build

# 3. Run a single stage
docker compose up test --build        # just pytest
docker compose up code-review --build # AI review only
```

## Running on GitHub Actions (free for public repos)

1. Push this repo to a **public** GitHub repository.
2. Go to **Settings → Secrets and variables → Actions**.
3. Add `ANTHROPIC_API_KEY` as a repository secret.
4. Open a Pull Request — the pipeline runs automatically.

## Running on GitLab CI (400 free minutes/month)

1. Push this repo to GitLab.
2. Go to **Settings → CI/CD → Variables**.
3. Add `ANTHROPIC_API_KEY` (masked + protected).
4. Open a Merge Request — the pipeline runs automatically.

## How the docker-compose → native pipeline mapping works

| docker-compose concept | GitHub Actions equivalent | GitLab CI equivalent |
|------------------------|--------------------------|----------------------|
| `services:` block      | `jobs:` block            | stages + job names   |
| `depends_on: ... service_completed_successfully` | `needs: [job]` | `stage:` ordering |
| `build: dockerfile:`   | Install tools in `steps:` | `image:` + `before_script:` |
| `environment:`         | `env:` + `secrets.X`     | `variables:` + CI/CD vars |
| `volumes:` (bind mount)| `actions/checkout@v4`    | auto-checkout        |
| `entrypoint` / `command` | `run:` in a step       | `script:`            |

## Cost notes

- **Local**: Free (you only pay for Anthropic API usage).
- **GitHub Actions**: Unlimited free minutes for public repos on standard runners.
- **GitLab CI**: 400 free compute minutes/month on the free tier.
- **Anthropic API**: Claude Code headless calls are billed per-token like
  normal API usage. A code review of a small file costs roughly $0.01–0.05.
