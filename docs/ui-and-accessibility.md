# 🖥️ Desktop UI and accessibility guide

## 1. Interface purpose

The Tkinter window has one primary task: accept a city or station query, initiate an AQI lookup, and present the returned reading and context. The interface should not overwhelm the user with unsupported controls or imply that a provider reading is a medical diagnosis.

## 2. Interaction states

| State | Expected user feedback |
|---|---|
| Idle | Prompt for a city or supported station |
| Empty input | Explain that a location is required |
| Missing token | Explain how to configure `WAQI_TOKEN` |
| Loading | Indicate that the provider is being contacted and prevent duplicate submissions |
| Success | Display numeric AQI, configured category, optional station and timestamp, and attribution |
| Failure | Display a clear non-sensitive explanation and allow retry |

## 3. Keyboard support

The city entry should receive initial focus. Enter should trigger the same action as the Find AQI button. Buttons and fields must remain reachable with keyboard navigation. Focus should not be lost after a failed request.

## 4. Readability and layout

- Use readable font sizes and avoid relying on colour alone to communicate AQI category.
- Provide enough window space for long category names and station labels.
- Allow the result label to wrap rather than clipping long text.
- Test at different display scaling settings.
- Keep status feedback distinguishable from the primary AQI result.
- Use plain language and explain unavailable data rather than showing stack traces.

## 5. Colour and AQI communication

Colour may reinforce a category, but text must always communicate the label. Do not use colour alone to communicate health risk. Any future colour palette must be reviewed for contrast and should remain understandable in high-contrast or monochrome contexts.

## 6. Accessibility review checklist

- [ ] Every input has a clear label.
- [ ] Keyboard-only use is possible.
- [ ] Keyboard focus remains visible.
- [ ] Enter triggers search from the location field.
- [ ] Result and status text are not clipped.
- [ ] Category meaning is conveyed in text, not colour alone.
- [ ] Error messages are actionable and do not expose credentials.
- [ ] Long station names and category labels fit the layout.
- [ ] Window can be resized to a practical minimum.
- [ ] Screen-reader behaviour is manually reviewed on supported platforms where possible.

## 7. Limits

Tkinter accessibility behaviour depends partly on the operating system, toolkit version, theme, and screen reader. A checklist is not proof of formal WCAG conformance. Record the operating systems and assistive technologies actually tested.
