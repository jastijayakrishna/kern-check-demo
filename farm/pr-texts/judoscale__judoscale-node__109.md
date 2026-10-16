# fix: Skip ephemeral reporters and redundant worker metrics

## Summary

- Treat release and one-off containers as ephemeral platform instances and skip reporter startup for them.
- Skip worker metric collection on redundant platform instances while keeping web metrics reporting.
- Cover primary, redundant, and ephemeral instance behavior in the core tests.

## Design decisions

The reporter owns ephemeral-container startup gating because release and one-off containers should not report regardless of which adapter path starts Judoscale. Platform subclasses own the naming rules because Heroku and Scalingo expose different container conventions.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Behavioral tightening in metrics reporting only; reduces duplicate or inappropriate reports without changing API or auth paths.
> 
> **Overview**
> Renames platform **`oneOff()`** to **`ephemeralInstance()`** and expands Heroku detection so **release-phase** dynos (`release.*`) are ephemeral alongside **`run.*`** one-offs; Scalingo **`one-off-*`** behavior is unchanged.
> 
> The **reporter** no longer starts periodic reporting when **`ephemeralInstance()`** is true (logs and returns early). On **redundant** formation instances (e.g. Heroku `web.2+`), it still reports but **`activeCollectors`** drops **`WorkerMetricsCollector`** so queue/worker metrics are only sent from the primary instance while web metrics continue.
> 
> Tests in **`platform.test.js`** and new **`reporter.test.js`** cover ephemeral gating and collector filtering.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 88567b4e1614e97879b56744390d2ee651f28deb. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
