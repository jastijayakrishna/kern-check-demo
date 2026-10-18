# feat: add autonomous shared WiFi signal survey

## Summary

- add a mower-side WiFi heatmap with shared, bounded and atomically persisted survey data
- collect pose and dBm without an active browser through one persistent fixed-name rospy subscriber
- reject unlocalized samples outside the current map bounds and clean up ROS helper processes on shutdown
- keep browser traffic and SD-card writes bounded through revision-aware polling, spatial cells, revisit thresholds and delayed flushes
- verify pull requests with the existing multi-arch Docker build while only publishing images from main

## Vanilla OpenMower compatibility

No Raspberry Pi host packages are required. In particular this does not use rpi-monitor, jq, host Python or the Docker CLI. The backend uses the mounted Docker Engine socket and runs the subscriber inside the official open_mower_ros container, where the existing OpenMower ROS 1 / xbot_msgs environment is available.

The previous ARM build failure was unrelated to runtime dependencies: the AMD64 build completed, while QEMU hit an illegal instruction during the frontend npm install. The architecture-independent Vite build stage now runs on BUILDPLATFORM; runtime stages remain multi-arch.

## Resource and privacy safeguards

- one sleeping ROS subscriber, one compact sample every 10 seconds by default
- maximum 2,000 cells; typically under 200 KB
- disk flush at most every 30 seconds, atomic rename and mower-file ownership
- fixed-name collector replacement and explicit graceful cleanup prevent process accumulation
- no SSID, map, coordinates, credentials or survey data are included in the repository or uploaded externally

## Verification

- node --check server.js
- 71 Vitest tests passed
- Vite production build passed
- runtime smoke test on OpenMower OS v2 with the official open_mower_ros image
- observed wlan0 signal collection and verified map-bounds rejection for an unlocalized startup pose
- verified graceful stop removes the ROS collector and ROS task count remains stable
