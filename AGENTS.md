# Agents used to build this integration

This integration was built with the help of several AI sub-agents, each given a
narrow, well-scoped job. This file documents who did what, so the work is
traceable and reproducible.

## Orchestration

The main agent (Claude, Opus 4.8) did the architecture and all the coupled,
correctness-critical work directly:

- Reverse-engineered the sample **Growatt Modbus** Home Assistant integration
  (`E:\Projekty\Growatt_Modbus_MID-MOD`) to reuse its YAML-map-driven,
  coordinator-based architecture.
- Extracted the **Deye three-phase hybrid Modbus protocol** from the supplied
  Word document (`Modbus amit posun.docx`) into text and identified the register
  layout (device type `0x0500`, FC03 for all live values, realtime block
  500–683, settings 60–499).
- Wrote the Python package: `coordinator.py` (poll-all-holding, `offset` +
  per-register `word_order` decoding), `config_flow.py` (with inverter-model
  dropdown), `__init__.py`, `mapping.py`, `models.py`, `const.py`, and the four
  entity platforms (`sensor`, `number`, `select`, `switch`).
- Hand-authored the register map `maps/sun_3ph_hybrid.yaml` and validated it
  with a standalone decode harness.

## Sub-agents (run in parallel, in the background)

| # | Agent (type) | Job | Output |
|---|--------------|-----|--------|
| 1 | Register-map verifier (`general-purpose`) | Audited `maps/sun_3ph_hybrid.yaml` line-by-line against the extracted Deye protocol doc: addresses, scales, `signed`/S16, 32-bit `word_order`, temperature `offset`; and listed notable missing realtime registers. **Read-only** — reported findings only. | Findings folded back into the map by the main agent. |
| 2 | Docs writer (`general-purpose`) | Wrote `README.md` (English + a Czech section) and `info.md` (HACS card) from the actual code. | `README.md`, `info.md` |
| 3 | CI / metadata (`general-purpose`) | Created `.gitignore`, `LICENSE` (MIT), and GitHub Actions workflows `.github/workflows/validate.yml` (hassfest + HACS validation) and `release.yml` (zip + attach on release). | `.gitignore`, `LICENSE`, `.github/workflows/*` |

## Why this split

The coordinator, config flow, and register map are tightly coupled and
correctness-sensitive (a wrong scale or word order silently produces bad data),
so the main agent kept those. The verifier, docs, and CI/metadata jobs are
independent and parallelizable, which is where sub-agents add the most value
without risking conflicting edits to the same files.
