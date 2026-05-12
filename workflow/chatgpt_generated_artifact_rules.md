# ChatGPT-generated Teaching Artifact Rules

This file defines how teaching visuals created during ChatGPT-led lessons should be handled in the repository.

## Scope

Examples:

- flowcharts
- beginner-friendly concept diagrams
- state-machine diagrams
- command side-effect tables
- annotated learning figures

## Core rule

If ChatGPT creates a teaching artifact during a lesson, it can count as a draft learning deliverable for the current stage.

The artifact should be saved or reproduced in the repository when it helps future lessons, reviews, or submissions.

## ChatGPT should provide

- the artifact or a reproducible text/SVG version,
- what the artifact teaches,
- the suggested repository path,
- a clear limitation statement.

## Codex should provide

- repository placement,
- links from the relevant docs,
- learning-record updates,
- evidence-register updates when appropriate,
- explicit git status and commit guidance.

## Evidence boundary

Teaching visuals are learning/documentation evidence only.
They do not prove firmware build, board flashing, serial behavior, or hardware behavior unless separate validation evidence is recorded.

## Current P1 example

For the NUCLEO UART lesson, a beginner-friendly `UART DMA + IDLE` flowchart is an acceptable small deliverable.

Suggested paths:

- `docs/05_test_and_logs/figures/2026-05-12_uart_dma_idle_flowchart_beginner.svg`
- `docs/05_test_and_logs/week1_nucleo_baseline.md`
- `learning/session_notes/2026-05-12_uart_dma_buffer_boundary.md`
