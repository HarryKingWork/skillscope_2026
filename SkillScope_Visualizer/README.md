# System Health Visualizer

A Python-based tool that runs a series of system health, displays results, and generates a visual report using a bar graph.

---

##Features

- Run basic and common system-level checks (disk, CPU, memory, services, ports, etc.)
- Evaluate environment readiness for DevOps workloads
- Visualize test results with a color-coded horizontal bar chart
- Designed for use in Linux-based environments

---

## Visual Output

The tool shows test results using a simple chart:

- **Green** = PASS
- **Red** = FAIL

Each bar is labeled for easy analysis.

---

## Tests Performed

### Common Tests:

- Disk Usage
- File System Health
- Memory Usage
- CPU Usage
- Nginx Running
- Port 80 Open
- Network Latency
- Disk IO
- Available Updates
- System Uptime

You can also add or customize tests under `Common` module.

---

