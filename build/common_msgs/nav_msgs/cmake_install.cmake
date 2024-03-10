# Install script for directory: /home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/walter1092/Desktop/workspace/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs/msg" TYPE FILE FILES
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/msg/GridCells.msg"
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/msg/MapMetaData.msg"
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/msg/OccupancyGrid.msg"
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/msg/Odometry.msg"
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/msg/Path.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs/srv" TYPE FILE FILES
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/srv/GetMap.srv"
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/srv/GetPlan.srv"
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/srv/SetMap.srv"
    "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/srv/LoadMap.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs/action" TYPE FILE FILES "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/action/GetMap.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs/msg" TYPE FILE FILES
    "/home/walter1092/Desktop/workspace/devel/share/nav_msgs/msg/GetMapAction.msg"
    "/home/walter1092/Desktop/workspace/devel/share/nav_msgs/msg/GetMapActionGoal.msg"
    "/home/walter1092/Desktop/workspace/devel/share/nav_msgs/msg/GetMapActionResult.msg"
    "/home/walter1092/Desktop/workspace/devel/share/nav_msgs/msg/GetMapActionFeedback.msg"
    "/home/walter1092/Desktop/workspace/devel/share/nav_msgs/msg/GetMapGoal.msg"
    "/home/walter1092/Desktop/workspace/devel/share/nav_msgs/msg/GetMapResult.msg"
    "/home/walter1092/Desktop/workspace/devel/share/nav_msgs/msg/GetMapFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs/cmake" TYPE FILE FILES "/home/walter1092/Desktop/workspace/build/common_msgs/nav_msgs/catkin_generated/installspace/nav_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/walter1092/Desktop/workspace/devel/include/nav_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/walter1092/Desktop/workspace/devel/share/roseus/ros/nav_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/walter1092/Desktop/workspace/devel/share/common-lisp/ros/nav_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/walter1092/Desktop/workspace/devel/share/gennodejs/ros/nav_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/walter1092/Desktop/workspace/devel/lib/python3/dist-packages/nav_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/walter1092/Desktop/workspace/devel/lib/python3/dist-packages/nav_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/walter1092/Desktop/workspace/build/common_msgs/nav_msgs/catkin_generated/installspace/nav_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs/cmake" TYPE FILE FILES "/home/walter1092/Desktop/workspace/build/common_msgs/nav_msgs/catkin_generated/installspace/nav_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs/cmake" TYPE FILE FILES
    "/home/walter1092/Desktop/workspace/build/common_msgs/nav_msgs/catkin_generated/installspace/nav_msgsConfig.cmake"
    "/home/walter1092/Desktop/workspace/build/common_msgs/nav_msgs/catkin_generated/installspace/nav_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nav_msgs" TYPE FILE FILES "/home/walter1092/Desktop/workspace/src/common_msgs/nav_msgs/package.xml")
endif()

