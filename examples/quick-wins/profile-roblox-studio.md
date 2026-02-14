# Profile: Roblox Game Studio

## Objective

Deliver a secure gameplay increment while protecting economy and progression systems.

## 2-Hour Quick Win Plan

1. Gameplay and progression planning

`cw /game-dev design a gameplay loop update with progression, rewards, and balancing constraints.`

2. Roblox-specific security pass

`cw /roblox-game-dev harden RemoteEvent/RemoteFunction boundaries, DataStore usage, and anti-abuse checks.`

3. Performance and reliability pass

`cw /enhance optimize script boundaries and identify replication/performance bottlenecks.`

4. Launch readiness

`cw /deploy produce rollout checklist with rollback and moderation considerations.`

## Deliverables Checklist

- gameplay update blueprint;
- Roblox security controls;
- performance and replication recommendations;
- launch/rollback checklist for live operations.

## Validation Commands

`python scripts/codexwf.py validate --tests`

`python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37`
