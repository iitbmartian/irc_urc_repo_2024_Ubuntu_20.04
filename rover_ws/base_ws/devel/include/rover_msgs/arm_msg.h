// Generated by gencpp from file rover_msgs/arm_msg.msg
// DO NOT EDIT!


#ifndef ROVER_MSGS_MESSAGE_ARM_MSG_H
#define ROVER_MSGS_MESSAGE_ARM_MSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>
#include <rover_msgs/drive_msg.h>

namespace rover_msgs
{
template <class ContainerAllocator>
struct arm_msg_
{
  typedef arm_msg_<ContainerAllocator> Type;

  arm_msg_()
    : shoulder_actuator()
    , elbow_actuator()
    , base_motor()
    , wrist_actuator()
    , elbow_motor()
    , gripper()
    , gripper_rot()
    , finger_actuator()
    , soil_box()
    , bio()  {
    }
  arm_msg_(const ContainerAllocator& _alloc)
    : shoulder_actuator(_alloc)
    , elbow_actuator(_alloc)
    , base_motor(_alloc)
    , wrist_actuator(_alloc)
    , elbow_motor(_alloc)
    , gripper(_alloc)
    , gripper_rot(_alloc)
    , finger_actuator(_alloc)
    , soil_box(_alloc)
    , bio(_alloc)  {
  (void)_alloc;
    }



   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _shoulder_actuator_type;
  _shoulder_actuator_type shoulder_actuator;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _elbow_actuator_type;
  _elbow_actuator_type elbow_actuator;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _base_motor_type;
  _base_motor_type base_motor;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _wrist_actuator_type;
  _wrist_actuator_type wrist_actuator;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _elbow_motor_type;
  _elbow_motor_type elbow_motor;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _gripper_type;
  _gripper_type gripper;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _gripper_rot_type;
  _gripper_rot_type gripper_rot;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _finger_actuator_type;
  _finger_actuator_type finger_actuator;

   typedef  ::rover_msgs::drive_msg_<ContainerAllocator>  _soil_box_type;
  _soil_box_type soil_box;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _bio_type;
  _bio_type bio;





  typedef boost::shared_ptr< ::rover_msgs::arm_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rover_msgs::arm_msg_<ContainerAllocator> const> ConstPtr;

}; // struct arm_msg_

typedef ::rover_msgs::arm_msg_<std::allocator<void> > arm_msg;

typedef boost::shared_ptr< ::rover_msgs::arm_msg > arm_msgPtr;
typedef boost::shared_ptr< ::rover_msgs::arm_msg const> arm_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rover_msgs::arm_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rover_msgs::arm_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rover_msgs::arm_msg_<ContainerAllocator1> & lhs, const ::rover_msgs::arm_msg_<ContainerAllocator2> & rhs)
{
  return lhs.shoulder_actuator == rhs.shoulder_actuator &&
    lhs.elbow_actuator == rhs.elbow_actuator &&
    lhs.base_motor == rhs.base_motor &&
    lhs.wrist_actuator == rhs.wrist_actuator &&
    lhs.elbow_motor == rhs.elbow_motor &&
    lhs.gripper == rhs.gripper &&
    lhs.gripper_rot == rhs.gripper_rot &&
    lhs.finger_actuator == rhs.finger_actuator &&
    lhs.soil_box == rhs.soil_box &&
    lhs.bio == rhs.bio;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rover_msgs::arm_msg_<ContainerAllocator1> & lhs, const ::rover_msgs::arm_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rover_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rover_msgs::arm_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rover_msgs::arm_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rover_msgs::arm_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rover_msgs::arm_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rover_msgs::arm_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rover_msgs::arm_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rover_msgs::arm_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "71499babfc2a932e972bf03c02baad13";
  }

  static const char* value(const ::rover_msgs::arm_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x71499babfc2a932eULL;
  static const uint64_t static_value2 = 0x972bf03c02baad13ULL;
};

template<class ContainerAllocator>
struct DataType< ::rover_msgs::arm_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rover_msgs/arm_msg";
  }

  static const char* value(const ::rover_msgs::arm_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rover_msgs::arm_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "drive_msg shoulder_actuator\n"
"drive_msg elbow_actuator\n"
"drive_msg base_motor\n"
"drive_msg wrist_actuator\n"
"drive_msg elbow_motor\n"
"drive_msg gripper\n"
"drive_msg gripper_rot\n"
"drive_msg finger_actuator\n"
"drive_msg soil_box\n"
"string bio\n"
"\n"
"================================================================================\n"
"MSG: rover_msgs/drive_msg\n"
"string direction\n"
"float64 speed\n"
"string mode\n"
;
  }

  static const char* value(const ::rover_msgs::arm_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rover_msgs::arm_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.shoulder_actuator);
      stream.next(m.elbow_actuator);
      stream.next(m.base_motor);
      stream.next(m.wrist_actuator);
      stream.next(m.elbow_motor);
      stream.next(m.gripper);
      stream.next(m.gripper_rot);
      stream.next(m.finger_actuator);
      stream.next(m.soil_box);
      stream.next(m.bio);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct arm_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rover_msgs::arm_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rover_msgs::arm_msg_<ContainerAllocator>& v)
  {
    s << indent << "shoulder_actuator: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.shoulder_actuator);
    s << indent << "elbow_actuator: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.elbow_actuator);
    s << indent << "base_motor: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.base_motor);
    s << indent << "wrist_actuator: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.wrist_actuator);
    s << indent << "elbow_motor: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.elbow_motor);
    s << indent << "gripper: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.gripper);
    s << indent << "gripper_rot: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.gripper_rot);
    s << indent << "finger_actuator: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.finger_actuator);
    s << indent << "soil_box: ";
    s << std::endl;
    Printer< ::rover_msgs::drive_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.soil_box);
    s << indent << "bio: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.bio);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROVER_MSGS_MESSAGE_ARM_MSG_H
