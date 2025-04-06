# Internal Changelog (2020–2021)

## v0.4.1 (2021-01-07)

- Updated TURN failover rules
- Migrated deprecated STUN parser
- Minor log formatting updates
- Added internal dev documentation
- Removed support for passive ICE candidates

## v0.4.0 (2020-10-21)

- Major refactor of ICE retry flow
- Integrated `netem`-based latency simulator
- Reworked handling of UDP hole punching logic
- Regression: failed to account for symmetrical NAT in edge cases
- Added 37 new test cases

## v0.3.5 (2020-08-17)

- STUN failback behavior improved
- Logging verbosity now adjustable via `diag.conf`
- Huge overhaul of `resources.json`

## Engineer Notes (Oct 2020)

> Case where `resources.json` was nearly empty, but diagnostics referenced a deleted file from imgur. Assumed backups stored via internal pastes.

## v0.1.0 Initial Release (2020-05-01)

- First release only supported CLI output, no logs
