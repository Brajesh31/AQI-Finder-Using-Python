## 🧾 Summary

Describe the problem, affected users, and expected result. State whether this is a bug fix, feature, refactor, security change, or documentation update.

## 🔍 Scope and implementation

- What changed?
- Which existing behaviours are intentionally unchanged?
- Does this affect WAQI requests, AQI category mapping, Tkinter threading, configuration, or stored data?
- Are any capabilities still proposals rather than working features?

## 🧪 Validation

- [ ] Unit tests added or updated.
- [ ] Provider tests use mocked HTTP responses, not live WAQI requests.
- [ ] AQI boundary cases tested where relevant.
- [ ] GUI manually checked on the target OS where relevant.
- [ ] `python -m pytest` executed, with result recorded below.

**Validation evidence:**

<details>
<summary>Commands and outcomes</summary>

Paste sanitized commands, test counts, Python version, and platform here.

</details>

## 🔐 Security and privacy

- [ ] No provider token, credential, or secret is included.
- [ ] No personal precise location or private search history is included.
- [ ] Request failures do not expose credential-bearing URLs.
- [ ] Any new provider or data collection behaviour is documented.

## ♿ Usability and accessibility

- [ ] Keyboard interaction remains usable.
- [ ] Loading and error states are clear.
- [ ] Long result text is not clipped.
- [ ] Category meaning is conveyed in text, not colour alone.

## 📚 Documentation

- [ ] README updated where user-facing behaviour changed.
- [ ] Relevant docs and Mermaid diagrams updated.
- [ ] Changelog or roadmap updated accurately.
- [ ] Screenshots, if supplied, are from the real running application and contain no secrets.

## ⚠️ Risks and rollback

Describe provider, OS compatibility, classification, or security risks and how to revert the change.
