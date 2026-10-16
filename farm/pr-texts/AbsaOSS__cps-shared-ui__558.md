# Fix inconsistent routing when reselecting sidebar component

Clicking the same sidebar item while already at `/componentName/examples` navigated back to `/componentName`. Because Angular reuses the component instance (same route definition matches both URLs), `ngOnInit()` didn't re-run, leaving the URL at `/componentName`. A subsequent API tab click then resolved `../api` relative to the single-segment path → `/api` → wildcard redirect → `/colors`.

## Changes

- **`ViewerComponent`**: Replace one-shot `snapshot.params` read with a subscription to `this._route.params` observable, so the redirect to `./examples` and `selectedTabIndex` update fire on both initial load and component reuse.
- **Subscription cleanup**: Add `takeUntilDestroyed(this._destroyRef)` to both the new `params` subscription and the pre-existing `router.events` subscription in `ngAfterViewInit`.

```ts
// Before — only runs once at component creation
ngOnInit(): void {
  if (!this._route.snapshot.params.type) {
    this._router.navigate(['./examples'], { relativeTo: this._route });
  }
  // ...
}

// After — reacts to every route reuse
ngOnInit(): void {
  this._route.params.pipe(takeUntilDestroyed(this._destroyRef)).subscribe((params) => {
    if (!params['type']) {
      this._router.navigate(['./examples'], { relativeTo: this._route });
      return;
    }
    // set selectedTabIndex ...
  });
}
```
