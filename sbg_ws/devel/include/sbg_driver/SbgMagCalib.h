// Generated by gencpp from file sbg_driver/SbgMagCalib.msg
// DO NOT EDIT!


#ifndef SBG_DRIVER_MESSAGE_SBGMAGCALIB_H
#define SBG_DRIVER_MESSAGE_SBGMAGCALIB_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace sbg_driver
{
template <class ContainerAllocator>
struct SbgMagCalib_
{
  typedef SbgMagCalib_<ContainerAllocator> Type;

  SbgMagCalib_()
    : header()  {
    }
  SbgMagCalib_(const ContainerAllocator& _alloc)
    : header(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;





  typedef boost::shared_ptr< ::sbg_driver::SbgMagCalib_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sbg_driver::SbgMagCalib_<ContainerAllocator> const> ConstPtr;

}; // struct SbgMagCalib_

typedef ::sbg_driver::SbgMagCalib_<std::allocator<void> > SbgMagCalib;

typedef boost::shared_ptr< ::sbg_driver::SbgMagCalib > SbgMagCalibPtr;
typedef boost::shared_ptr< ::sbg_driver::SbgMagCalib const> SbgMagCalibConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sbg_driver::SbgMagCalib_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sbg_driver::SbgMagCalib_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgMagCalib_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sbg_driver::SbgMagCalib_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgMagCalib_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sbg_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgMagCalib_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgMagCalib_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgMagCalib_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d7be0bb39af8fb9129d5a76e6b63a290";
  }

  static const char* value(const ::sbg_driver::SbgMagCalib_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd7be0bb39af8fb91ULL;
  static const uint64_t static_value2 = 0x29d5a76e6b63a290ULL;
};

template<class ContainerAllocator>
struct DataType< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sbg_driver/SbgMagCalib";
  }

  static const char* value(const ::sbg_driver::SbgMagCalib_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# SBG Ellipse Messages\n"
"Header header\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::sbg_driver::SbgMagCalib_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SbgMagCalib_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sbg_driver::SbgMagCalib_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sbg_driver::SbgMagCalib_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SBG_DRIVER_MESSAGE_SBGMAGCALIB_H
