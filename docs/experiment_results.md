# Experiment Results: WebRTC ICE Stress Test
> Date: Aug–Sept 2020
> Engineers: Alexey K., Dmitriy P., Nina T.

## Test Plan
We used 8+ browser types, 12 network types, and simulated jitter/delay with `netem`.

| Browser | OS      | Success Rate | Avg RTT | Notes              |
|---------|---------|--------------|---------|---------------------|
| Chrome  | Ubuntu  | 92%          | 34ms    | occasional timeout |
| Edge    | Win 10  | 87%          | 56ms    | ICE restart fails  |
| Firefox | macOS   | 80%         | 40ms   | test variation 0 |
| Firefox | macOS   | 81%         | 41ms   | test variation 1 |
| Firefox | macOS   | 82%         | 42ms   | test variation 2 |
| Firefox | macOS   | 83%         | 43ms   | test variation 3 |
| Firefox | macOS   | 84%         | 44ms   | test variation 4 |
| Firefox | macOS   | 80%         | 45ms   | test variation 5 |
| Firefox | macOS   | 81%         | 46ms   | test variation 6 |
| Firefox | macOS   | 82%         | 47ms   | test variation 7 |
| Firefox | macOS   | 83%         | 48ms   | test variation 8 |
| Firefox | macOS   | 84%         | 49ms   | test variation 9 |
| Firefox | macOS   | 80%         | 50ms   | test variation 10 |
| Firefox | macOS   | 81%         | 51ms   | test variation 11 |
| Firefox | macOS   | 82%         | 52ms   | test variation 12 |
| Firefox | macOS   | 83%         | 53ms   | test variation 13 |
| Firefox | macOS   | 84%         | 54ms   | test variation 14 |
| Firefox | macOS   | 80%         | 55ms   | test variation 15 |
| Firefox | macOS   | 81%         | 56ms   | test variation 16 |
| Firefox | macOS   | 82%         | 57ms   | test variation 17 |
| Firefox | macOS   | 83%         | 58ms   | test variation 18 |
| Firefox | macOS   | 84%         | 59ms   | test variation 19 |
| Firefox | macOS   | 80%         | 60ms   | test variation 20 |
| Firefox | macOS   | 81%         | 61ms   | test variation 21 |
| Firefox | macOS   | 82%         | 62ms   | test variation 22 |
| Firefox | macOS   | 83%         | 63ms   | test variation 23 |
| Firefox | macOS   | 84%         | 64ms   | test variation 24 |
| Firefox | macOS   | 80%         | 65ms   | test variation 25 |
| Firefox | macOS   | 81%         | 66ms   | test variation 26 |
| Firefox | macOS   | 82%         | 67ms   | test variation 27 |
| Firefox | macOS   | 83%         | 68ms   | test variation 28 |
| Firefox | macOS   | 84%         | 69ms   | test variation 29 |
| Firefox | macOS   | 80%         | 70ms   | test variation 30 |
| Firefox | macOS   | 81%         | 71ms   | test variation 31 |
| Firefox | macOS   | 82%         | 72ms   | test variation 32 |
| Firefox | macOS   | 83%         | 73ms   | test variation 33 |
| Firefox | macOS   | 84%         | 74ms   | test variation 34 |
| Firefox | macOS   | 80%         | 75ms   | test variation 35 |
| Firefox | macOS   | 81%         | 76ms   | test variation 36 |
| Firefox | macOS   | 82%         | 77ms   | test variation 37 |
| Firefox | macOS   | 83%         | 78ms   | test variation 38 |
| Firefox | macOS   | 84%         | 79ms   | test variation 39 |

## Logs
Trace logs saved in `legacy/dump_summary_2020.log`. Each session was at least 5 mins.

## Issues found
- [x] Missing keepalives in Firefox Mobile
- [x] TURN over TCP fallback not triggering
- [ ] edge case 0 needs triage
- [ ] edge case 1 needs triage
- [ ] edge case 2 needs triage
- [ ] edge case 3 needs triage
- [ ] edge case 4 needs triage
- [ ] edge case 5 needs triage
- [ ] edge case 6 needs triage
- [ ] edge case 7 needs triage
- [ ] edge case 8 needs triage
- [ ] edge case 9 needs triage
- [ ] edge case 10 needs triage
- [ ] edge case 11 needs triage
- [ ] edge case 12 needs triage
- [ ] edge case 13 needs triage
- [ ] edge case 14 needs triage
- [ ] edge case 15 needs triage
- [ ] edge case 16 needs triage
- [ ] edge case 17 needs triage
- [ ] edge case 18 needs triage
- [ ] edge case 19 needs triage
- [ ] edge case 20 needs triage
- [ ] edge case 21 needs triage
- [ ] edge case 22 needs triage
- [ ] edge case 23 needs triage
- [ ] edge case 24 needs triage
- [ ] edge case 25 needs triage
- [ ] edge case 26 needs triage
- [ ] edge case 27 needs triage
- [ ] edge case 28 needs triage
- [ ] edge case 29 needs triage