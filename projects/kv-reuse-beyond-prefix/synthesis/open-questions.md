# Open Questions

## 1. When does reuse stop being cheaper than recomputation?

This project should not assume “more reuse is always better.”

The answer depends on:

- storage tier cost
- storage locality
- transfer overhead
- request recurrence
- quality loss from approximate reuse

## 2. What is the real boundary beyond exact prefix reuse?

There are several different answers already in the literature:

- approximate but still request-level reuse
- semantic reuse via matching
- cross-model reuse with selective recomputation
- agent-to-agent representation transfer

These are not one trick family. They are different compatibility contracts.

## 3. Do sparse-attention models make reuse more attractive or less necessary?

Possible outcomes:

- more attractive because smaller, more structured retained state is easier to keep and share
- less necessary because compute and memory pressure both drop
- both at once, depending on workload regime

This needs paper evidence rather than intuition.

## 4. Is reusable KV converging toward an intermediate representation?

The current signals come from:

- `DroidSpeak`
- `Q-KVComm`
- workflow papers like `Agentix`

The key question is whether the field is still just optimizing caches, or gradually standardizing reusable model-native state.
