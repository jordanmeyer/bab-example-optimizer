# Developer evaluation

2026-10-09. This original bakery allocation app follows the actual simulated planning exchange. The independent reviewer owns REVIEW.md. No independent PASS or publication is claimed here.

## Initial implementation evidence

Actual toolchain: Node 22.19.0 and npm 10.9.3, with exact HiGHS 1.15.3 and Vite 8.3.4. The registry lockfile was inspected; installation reported zero vulnerabilities; notices were generated. The canonical dependency checker rejects `Unapproved dependency: highs@1.15.3`. The coordinator authorized this exact candidate trial, with promotion still a separate gate. Build logs externalize HiGHS's Node-only `node:module` branch; the actual browser worker succeeds. Local worker/WASM assets use the production prefix. Complete network capture is unavailable; source/assets/log inspection is limited evidence, not a complete request trace.

Independent standard-library enumeration (`python3 scripts/oracles.py`) finds 2,681 feasible default mixes and unique (5,5,18), $955, resource use (470,600,360). The tiny case has 17 feasible mixes and unique (3,2), $23. The workshop fixture has 64 feasible mixes and optimum (0,1,3), $112; increasing machine capacity to 19 gives $119 and to 20 gives $123. Independent exact LP certificates give the default bound $955 and tiny bound $24. The workshop relaxation bound $113.20 follows the reviewer's separate algebra.

The actual browser suite passed 22/22 through Codex CUA at port 9515. It imports the application's real model/client and actual HiGHS worker. Tests cover default/tiny/workshop integer and LP answers, useful and nonbinding capacity changes, infeasible commitments, negative contribution, zero capacity, exact cents, input boundaries, manual feasibility, an actual raw unbounded solver fixture, real worker request→cancel→fresh known solve, and request supersession. Limited-incumbent/no-incumbent branches and corrupt returned solutions are explicitly adapter-level shaped-result checks. No real timeout was induced. The cancellation test waits for the real worker's loading phase before termination; no claim is made that this small model requires sustained CPU work. Browser warning/error logs were empty.

## Production behavior

The prefixed production app on port 9516 showed the default 5/5/18 batches and $955, with used minutes 470/600/360. The tiny lesson showed 3/2/0 and $23 versus a fractional LP of 8/3 each and $24. Manual 3/3 showed $27 arithmetic contribution but clearly failed both 9>8 resource limits. Manual 3/2 was feasible at $23, with slack 0/1/1. The actual copied rationale contained the tiny quantities, boxes, coefficients, bounds, status and model limits.

Oven capacity 157 produced Infeasible with its one-minute minimum-commitment overage. A blank prep field focused capacity-0 and cleared results; reset recovered. Zero capacity with zero commitments produced a feasible $0/zero-batch result, exact zero slack and zero-width bars, with binding terminology explained. Negative contributions −25/−22/−40 produced the committed 4/3/2 and −$246 with a costly-commitment explanation. Editing cleared obsolete evidence.

Actual keyboard controls opened the lesson, solved, checked manual mixes, reset and copied. Tab from prep capacity moved to oven capacity. Pressing Reset then Cancel during the real loading phase showed cancelled/no results; the next solve returned $955. Actual native away/Back after applied tiny/manual edits and a deliberately pending prep edit returned default prep 480 and manual 4 with an honest new-loading status before any interaction, then default results. Persisted bfcache was not observed. The source preserves completed cached state and cancels an active request on pagehide. Clipboard-denial fallback is source-reviewed only, not a claimed forced-denial test.

## Layout and observation limits

Actual 1440 CSS-pixel production frame measured document client/scroll widths 1439/1439; the 320 frame measured 319/319. Screenshots were inspected for the desktop header, capacity/product controls, narrow form and narrow allocation result. The wide allocation table scrolls locally. Developer screenshots are outside the publishing source in the parent temporary directory: optimizer-desktop.png, optimizer-narrow.png and optimizer-narrow-result.png. Fixed frames are responsive CSS checks, not physical-device evidence. The host has large screenshot scaling; clip dimensions were adjusted without changing the shared viewport.

The implementation's only styling change after these captures is none; the final model text polish abbreviates “more minutes” to “more min.” No unresolved application failure was found in this round. Final source freeze, clean evaluation comparisons and independent review are still required. Subsequent failures will be appended, never replaced.
