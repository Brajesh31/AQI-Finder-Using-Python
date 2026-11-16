# ♿ Accessibility statement

## Scope

AQI Finder currently presents a small Tkinter desktop interface. Accessibility depends on Python, Tk/Tcl, the operating system, theme, display scaling, and assistive technology. This statement records design expectations; it is not a claim of formal WCAG conformance.

## Current expectations

- Location input has a clear label.
- The main lookup can be triggered with the keyboard.
- Focus remains usable after validation or provider errors.
- Loading and failure states are communicated in text.
- AQI category labels are written out and are not indicated by colour alone.
- Long category names and station names should not be clipped.
- Error messages should be actionable and must not expose credentials.

## Known limitations

Screen-reader output and keyboard traversal can differ across platforms and Tk versions. The project has not yet published a formal assistive-technology test matrix. Do not infer conformance from the existence of this checklist.

## Reporting an accessibility issue

Open an issue describing the operating system, Python/Tk version, assistive technology if applicable, steps to reproduce, and expected behaviour. Remove API tokens and private location data from screenshots and logs.

## Review checklist

- [ ] Keyboard-only interaction tested.
- [ ] Focus is visible and predictable.
- [ ] Result/status text remains visible at supported scaling.
- [ ] Colour is not the only signal.
- [ ] Error states are understandable.
- [ ] Assistive-technology behaviour is described accurately.
