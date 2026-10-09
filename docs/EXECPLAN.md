# Put solve controls beside the decision and teach the constraints


This living plan follows ~/.codex/PLANS.md and the remaining126-item October9 checklist. Preserve previous source/evaluation history.

## Purpose / Big Picture


Students can apply edited assumptions or cancel a busy solve directly beside its status. Bounded prediction tasks expose greedy allocation, infeasibility and omitted scheduling assumptions. Capacity limits remain explicit.

## Progress


- [x] Read full shared/OPT checklist, complete current source/worker/model/tests/style and existing plans.
- [x] Move one canonical solve/cancel/status bar beside the result; correct deterministic-cap wording and persistence guidance.
- [x] Add bounded exercises, actual-worker range cases and authored UI-state/200%-text QA frames.
- [ ] Checkpoint, meaningful model/build checks and root actual production/browser/320px/200% review.
- [ ] Independent root review before publication; preserve human-evidence gaps.

## Surprises & Discoveries


All cancellation mechanics already exist; placement hides the action promised by the busy panel. No second solver or duplicate action owner is needed. The model admits a simple greedy feasible allocation5/4/18 for$933, versus optimum5/8/16 for$941.

## Decision Log


2026-10-09: Move existing form-associated submit/cancel/status controls into the outcome panel, with a link from the long form. Open assumptions only when invalid fields need focus. Keep unchanged worker deadlines; add real-worker tests for oven9940,9941,10000. Use authored app-iframe event tests for fast cancel/edit transitions, explicitly distinguish them from human screen-reader tasks and simulated timeout adapters. Optional purchased-capacity pricing remains an exercise only.

## Outcomes & Retrospective


Implementation complete; fresh install/build and independent Python plus actual Node HiGHS cases pass. Prior25-case actual-browser record remains historical. Root actual browser27-case suite and UI/320px/200% review pending. No novice-readiness or screen-reader claim.

## Context and Orientation


app/model.js owns allocation/rationale/validation; solver-worker.js calls pinned HiGHS; solver-client.js owns worker cancellation and deadline. app/app.js and index.html own the stateful UI. tests/tests.js covers real workers plus labeled adapters; scripts/oracles.py independently enumerates small models. Root has browser access; this subagent's inventory is empty.

## Plan of Work


Relocate existing actions/status without adding parallel controls. Pending and error results keep Solve reachable; busy results expose Cancel. Add precise assumed-demand wording and total-minutes versus schedule copy. Add prediction/answer tasks and references. Convert text sizes to relative units and keep the two-product diagram readable in a scrollable region. Add separate320px/200% authored frames. Freeze source, run required checks, then root performs actual browser tasks. Preserve failures and per-ID dispositions in course evidence/checklist-corrections/2026-10-09/optimizer.

## Concrete Steps


Run npm ci --cache /private/tmp/bab-npm-cache; packaged check-dependencies.mjs; python3 scripts/oracles.py; npm run build. Test server9703/tests/; production9704/bab-example-optimizer/. Copy authored QA frames into local dist after build only; publishing build omits them. Commit app source before final root review and do not push before authorization.

## Validation and Acceptance


Default941/LP946 and actual +60 gains0/46/62 retained. Greedy5/4/18 is feasible933;18 celebration alone misses breakfast/tea commitments. Oven157 is infeasible because minima require4×18+3×12+2×25=158. Oven9940 permits an experiment at10000;9941 and10000 suppress only the unsupported increment. Actual UI cancellation/retry/edit-during-solve must clear stale allocations; real limited-feasible result is attempted only if naturally reproducible and otherwise adapter-only. Root checks320px and200% text separately, visible reachable Solve/Cancel and all diagram labels. Actual novice and screen-reader tasks remain external gates.

## Idempotence and Recovery


Reset restores defaults; cancellation and editing terminate workers. Repeated builds replace only dist. Ordinary commits preserve all historical evidence; no shared course checklist or plugin edits.

## Artifacts and Notes


BUILD-STORY has task/control/answer/limitation. EVALUATION distinguishes Node/model/browser and prior rounds. Per-ID evidence includes optional-extension disposition and open human tasks.

## Interfaces and Dependencies


Use the existing form attribute to associate the relocated submit button with #scenario. No dependency or solver API change. HiGHS1.15.3/Vite8.3.4 and licensed local fonts remain pinned.

Revision note: applies remaining teaching, action-placement and range-boundary items without expanding the optimization model.
