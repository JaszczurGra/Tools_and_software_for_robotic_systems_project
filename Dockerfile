FROM osrf/ros:jazzy-desktop

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY src project/src

RUN apt-get update && rosdep update && rosdep install -i --from-paths project/src --rosdistro jazzy -y

RUN cd project && source /opt/ros/jazzy/setup.bash && colcon build
COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["bash"]