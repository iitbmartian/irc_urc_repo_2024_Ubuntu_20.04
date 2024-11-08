// Generated by gencpp from file sbg_driver/SbgGpsVelStatus.msg
// DO NOT EDIT!


#ifndef SBG_DRIVER_MESSAGE_SBGGPSVELSTATUS_H
#define SBG_DRIVER_MESSAGE_SBGGPSVELSTATUS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace sbg_driver
{
template <class ContainerAllocator>
struct SbgGpsVelStatus_
{
  typedef SbgGpsVelStatus_<ContainerAllocator> Type;

  SbgGpsVelStatus_()
    : vel_status(0)
    , vel_type(0)  {
    }
  SbgGpsVelStatus_(const ContainerAllocator& _alloc)
    : vel_status(0)
    , vel_type(0)  {
  (void)_alloc;
    }



   typedef uint8_t _vel_status_type;
  _vel_status_type vel_status;

   typedef uint8_t _vel_type_type;
  _vel_type_type vel_type;





  typedef boost::shared_ptr< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> const> ConstPtr;

}; // struct SbgGpsVelStatus_

typedef ::sbg_driver::SbgGpsVelStatus_<std::allocator<void> > SbgGpsVelStatus;

typedef boost::shared_ptr< ::sbg_driver::SbgGpsVelStatus > SbgGpsVelStatusPtr;
typedef boost::shared_ptr< ::sbg_driver::SbgGpsVelStatus const> SbgGpsVelStatusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator2> & rhs)
{
  return lhs.vel_status == rhs.vel_status &&
    lhs.vel_type == rhs.vel_type;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sbg_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8c5fcc3c3ffd11ce820539049c166dde";
  }

  static const char* value(const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8c5fcc3c3ffd11ceULL;
  static const uint64_t static_value2 = 0x820539049c166ddeULL;
};

template<class ContainerAllocator>
struct DataType< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sbg_driver/SbgGpsVelStatus";
  }

  static const char* value(const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# SBG Ellipse Messages\n"
"# Submessage\n"
"\n"
"# The raw GPS velocity status\n"
"# 0 SOL_COMPUTED		A valid solution has been computed.\n"
"# 1 INSUFFICIENT_OBS	Not enough valid SV to compute a solution.\n"
"# 2 INTERNAL_ERROR		An internal error has occurred.\n"
"# 3 LIMIT				Velocity limit exceeded.\n"
"uint8 vel_status\n"
"\n"
"# The raw GPS velocity type\n"
"# 0 VEL_NO_SOLUTION		No valid velocity solution available.\n"
"# 1 VEL_UNKNOWN_TYPE	An unknown solution type has been computed.\n"
"# 2 VEL_DOPPLER			A Doppler velocity has been computed.\n"
"# 3 VEL_DIFFERENTIAL	A velocity has been computed between two positions.\n"
"uint8 vel_type\n"
;
  }

  static const char* value(const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.vel_status);
      stream.next(m.vel_type);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SbgGpsVelStatus_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sbg_driver::SbgGpsVelStatus_<ContainerAllocator>& v)
  {
    s << indent << "vel_status: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.vel_status);
    s << indent << "vel_type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.vel_type);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SBG_DRIVER_MESSAGE_SBGGPSVELSTATUS_H
