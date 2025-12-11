# Tools and Software for Robotic Systems Project

A ROS2 Jazzy project for controlling a Universal Robots UR5e using Docker. This setup includes the UR simulator, RViz visualization, interactive robot control, and USB camera integration.

## Installation

Clone the repository with submodules:

```bash
git clone --recursive https://github.com/JaszczurGra/Tools_and_software_for_robotic_systems_project
```

## Running

Start the Docker containers:

```bash
docker compose up
```

This will launch:
- RViz visualization
- Interactive control window (click to move robot above/below middle vertically)
- USB camera feed

### Required: Start the UR Simulator


1. Open the VNC interface in your browser: [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html)

2. **Start the Robot:**
   - Turn on the robot
   - Click the play button and choose **"Play from Selection"**

### Troubleshooting

If "Play from Selection" is not available, configure URCaps:

1. **Verify URCaps Initialization:**
   - Navigate to: `Settings > System > URCaps`
   - Check if **External Control** is active
   - If not, click the `+` button, go to `urcaps`, and open the URCap file

2. **Configure External Control:**
   - Navigate to: `Installation > URCaps > External Control`
   - Set the **Host IP** to `180.25.0.10` (or your modified IP from docker-compose.yml)
   - Go to `Program>URCaps>External Control` and add a new program 

3. Retry the "Play from Selection" step

