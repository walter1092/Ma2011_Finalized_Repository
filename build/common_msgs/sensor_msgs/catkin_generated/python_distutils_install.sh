#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/walter1092/Desktop/workspace/src/common_msgs/sensor_msgs"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/walter1092/Desktop/workspace/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/walter1092/Desktop/workspace/install/lib/python3/dist-packages:/home/walter1092/Desktop/workspace/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/walter1092/Desktop/workspace/build" \
    "/usr/bin/python3" \
    "/home/walter1092/Desktop/workspace/src/common_msgs/sensor_msgs/setup.py" \
    egg_info --egg-base /home/walter1092/Desktop/workspace/build/common_msgs/sensor_msgs \
    build --build-base "/home/walter1092/Desktop/workspace/build/common_msgs/sensor_msgs" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/walter1092/Desktop/workspace/install" --install-scripts="/home/walter1092/Desktop/workspace/install/bin"
