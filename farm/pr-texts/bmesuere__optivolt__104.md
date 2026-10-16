# Graph improvements: zero line, negative-price highlights, and buy-price strip

## Summary
- Add zero reference line to price chart for visual anchoring
- Highlight grid injection slots with negative electricity prices in a distinct color
- Add buy-price color strip below the flows chart: one segment per time slot, colored from blue (negative prices) through neutral to red (high prices), interpolated in Oklab for perceptual uniformity
- Refresh all charts on theme change

<img width="1676" height="630" alt="image" src="https://github.com/user-attachments/assets/0c367314-387e-4b1b-889e-7e609f6412dd" />
<img width="2466" height="718" alt="image" src="https://github.com/user-attachments/assets/3cb77003-d9a8-410e-afeb-e5456f5d220b" />
<img width="370" height="670" alt="image" src="https://github.com/user-attachments/assets/f47aa121-f6d6-4f79-8162-d223f1cd9cf3" />


## Test Plan
- [ ] Verify zero line appears on price chart
- [ ] Verify negative-price grid injection slots are visually highlighted
- [ ] Verify buy-price strip renders below the flows chart with correct colors per slot
- [ ] Toggle dark/light theme and confirm all charts update correctly
