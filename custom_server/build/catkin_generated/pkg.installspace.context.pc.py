# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "geometry_msgs;message_generation;rospy;sensor_msgs;std_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lcustom_server".split(';') if "-lcustom_server" != "" else []
PROJECT_NAME = "custom_server"
PROJECT_SPACE_DIR = "/usr/local"
PROJECT_VERSION = "0.0.0"
