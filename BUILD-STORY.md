# How Batch & Balance was built

The request was a constrained workshop: choose the best production mix, explain binding limits, explore new capacity and expose infeasible requirements. [Original planning](PLANNING-CONVERSATION.md) is explicitly simulated; it translated the workshop into three bakery products and resources. [PLAN](PLAN.md) now documents all equations, units and acceptance; [DECISIONS](DECISIONS.md) distinguishes user-authorized revision choices from that original exchange.

The first version solved mixes but left capacity value to manual edits and had no default whole-batch gap. The revision adds three+60-minute integer experiments, a590-minute oven default with a real$5 gap, and a geometric two-product lesson. It keeps actual HiGHS worker solving, bounded validation, infeasibility, cancellation, manual checks and copied rationale.

Browser App Builder Build/Evaluate and HiGHS guidance supplied the implementation workflow. HiGHS1.15.3 and its WASM run locally; plain SVG shows the feasible region. Campus Designer's public color/type guidance supplies the local EB Garamond/Open Sans pairing, with licenses included. There is no runtime service or remote data.

[Evaluation](EVALUATION.md) retains independently enumerated expected answers, browser observations and failed rounds. [Review](REVIEW.md) records independent review and [deployment](DEPLOYMENT.md) identifies what is live. No synthetic figure is evidence of real bakery performance.

## Try the experiment

Predict before changing the controls. Copy each solved rationale before leaving; reload restores the example. These tasks use invented coefficients and cannot establish a real bakery schedule.

1. **Challenge “highest contribution first.”** Reset the bakery. Celebration boxes contribute $40 per batch, versus $25 breakfast and $22 tea. Predict whether maximizing celebration first wins. Open “Fractional batches and manual comparison,” enter breakfast0, tea0, celebration18 and check. Then reserve all minimum commitments (4/3/2), fill celebration to18, add as much breakfast as remaining resources permit, then tea. Check the resulting5/4/18 mix.

   **Answer:**18 celebrations alone ignores the4-breakfast and3-tea commitments. Reserving commitments and filling in descending contribution order produces5/4/18: $933, using460 prep,588 oven and350 packing minutes, so it is feasible. The optimum5/8/16 earns$941. Swapping two celebration batches for four tea batches adds4×$22−2×$40=$8, leaves prep unchanged, frees2 oven minutes and uses10 more packing minutes. A high per-batch contribution does not account for resource tradeoffs. Do not call an infeasible mix an improvement just because its arithmetic contribution is high.

2. **Predict infeasibility without a solver.** Reset, edit oven capacity from590 to157, then use “Review the pending result” and “Solve current assumptions.” Before solving, calculate oven time required by minimum commitments.

   **Answer:**4×18+3×12+2×25=158 oven minutes.157 cannot accommodate the commitments; the reported shortfall is1 minute. The minimum uses118 prep and92 packing minutes, within their480/360 capacities. Solve does not silently relax promises. Restore oven590 and solve again; the default returns$941.

3. **Buy an hour only if it earns its cost.** Predict which resource has the highest gross benefit from another hour. Compare the three actual experiments, then choose “Add60 oven minutes.” Reconcile the new mix and previous-solve comparison.

   **Answer:** Prep earns$0, oven$46 and packing$62 of extra contribution before any capacity purchase cost. Adding60 oven minutes produces15/6/12 batches and$987 versus$941. The original oven has4 minutes of slack yet another hour is valuable; whole batches make these finite changes, not universal per-minute prices. At oven9940, another60 is supported; above9940 it would exceed the explicit10000-minute limit, so the app omits that experiment rather than clamping it.

4. **Explain why an allocation is not a schedule.** Imagine the oven capacity is590 total productive minutes. Before assuming this plan can run tomorrow, ask whether batches need simultaneous trays, fixed start times, cleaning between products or a single sequenced machine. Name one additional fact you need.

   **Answer:** This model adds each batch's resource minutes. It contains neither tray concurrency nor order/start times. A feasible total-minute allocation can still be impossible to sequence. Demand maxima are assumed sales ceilings, not demand forecasts or guaranteed sell-through.

5. **Explain integrality.** Try the two-product lesson. Predict what rounding both fractional quantities8/3 to3 will do, then check manual3/3 and read the geometric constraints.

   **Answer:** Both prep and oven use9 minutes against8. The fractional$24 bound is not a baking plan; the feasible whole-batch optimum3/2 earns$23. The exact feasible region and integer points show the distinction.

## Optional extension: priced overtime

Introduce purchased capacity only after stating its per-resource price, upper bounds and availability. Change the objective to subtract its cost, and decide whether additional minutes are divisible or come in blocks. Hand-check zero purchase, an uneconomic purchase and a binding purchase cap before testing the optimizer. The shipped app keeps gross finite capacity comparisons and adds no overtime control.
