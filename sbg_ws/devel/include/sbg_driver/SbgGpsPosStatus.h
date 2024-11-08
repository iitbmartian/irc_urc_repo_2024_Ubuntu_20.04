// Generated by gencpp from file sbg_driver/SbgGpsPosStatus.msg
// DO NOT EDIT!


#ifndef SBG_DRIVER_MESSAGE_SBGGPSPOSSTATUS_H
#define SBG_DRIVER_MESSAGE_SBGGPSPOSSTATUS_H


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
struct SbgGpsPosStatus_
{
  typedef SbgGpsPosStatus_<ContainerAllocator> Type;

  SbgGpsPosStatus_()
    : status(0)
    , type(0)
    , gps_l1_used(false)
    , gps_l2_used(false)
    , gps_l5_used(false)
    , glo_l1_used(false)
    , glo_l2_used(false)  {
    }
  SbgGpsPosStatus_(const ContainerAllocator& _alloc)
    : status(0)
    , type(0)
    , gps_l1_used(false)
    , gps_l2_used(false)
    , gps_l5_used(false)
    , glo_l1_used(false)
    , glo_l2_used(false)  {
  (void)_alloc;
    }



   typedef uint8_t _status_type;
  _status_type status;

   typedef uint8_t _type_type;
  _type_type type;

   typedef uint8_t _gps_l1_used_type;
  _gps_l1_used_type gps_l1_used;

   typedef uint8_t _gps_l2_used_type;
  _gps_l2_used_type gps_l2_used;

   typedef uint8_t _gps_l5_used_type;
  _gps_l5_used_type gps_l5_used;

   typedef uint8_t _glo_l1_used_type;
  _glo_l1_used_type glo_l1_used;

   typedef uint8_t _glo_l2_used_type;
  _glo_l2_used_type glo_l2_used;





  typedef boost::shared_ptr< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> const> ConstPtr;

}; // struct SbgGpsPosStatus_

typedef ::sbg_driver::SbgGpsPosStatus_<std::allocator<void> > SbgGpsPosStatus;

typedef boost::shared_ptr< ::sbg_driver::SbgGpsPosStatus > SbgGpsPosStatusPtr;
typedef boost::shared_ptr< ::sbg_driver::SbgGpsPosStatus const> SbgGpsPosStatusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator2> & rhs)
{
  return lhs.status == rhs.status &&
    lhs.type == rhs.type &&
    lhs.gps_l1_used == rhs.gps_l1_used &&
    lhs.gps_l2_used == rhs.gps_l2_used &&
    lhs.gps_l5_used == rhs.gps_l5_used &&
    lhs.glo_l1_used == rhs.glo_l1_used &&
    lhs.glo_l2_used == rhs.glo_l2_used;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator1> & lhs, const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sbg_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "85506deb3699c6f0e87097da56884a7e";
  }

  static const char* value(const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x85506deb3699c6f0ULL;
  static const uint64_t static_value2 = 0xe87097da56884a7eULL;
};

template<class ContainerAllocator>
struct DataType< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sbg_driver/SbgGpsPosStatus";
  }

  static const char* value(const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# SBG Ellipse Messages\n"
"# Submessage\n"
"\n"
"\n"
"# The raw GPS position status\n"
"# 0 SOL_COMPUTED		A valid solution has been computed.\n"
"# 1 INSUFFICIENT_OBS 	Not enough valid SV to compute a solution.\n"
"# 2 INTERNAL_ERROR 		An internal error has occurred.\n"
"# 3 HEIGHT_LIMIT 		The height limit has been exceeded.\n"
"uint8 status\n"
"\n"
"# The raw GPS position type\n"
"# 0 NO_SOLUTION		No valid solution available.\n"
"# 1 UNKNOWN_TYPE	An unknown solution type has been computed.\n"
"# 2 SINGLE			Single point solution position.\n"
"# 3 PSRDIFF			Standard Pseudorange Differential Solution (DGPS).\n"
"# 4 SBAS			SBAS satellite used for differential corrections.\n"
"# 5 OMNISTAR		Omnistar VBS Position (L1 sub-meter).\n"
"# 6 RTK_FLOAT		Floating RTK ambiguity solution (20 cms RTK).\n"
"# 7 RTK_INT			Integer RTK ambiguity solution (2 cms RTK).\n"
"# 8 PPP_FLOAT		Precise Point Positioning with float ambiguities\n"
"# 9 PPP_INT			Precise Point Positioning with fixed ambiguities\n"
"# 10 FIXED			Fixed location solution position\n"
"uint8 type\n"
"\n"
"# True if GPS L1 is used in the solution\n"
"bool gps_l1_used\n"
"\n"
"# True if GPS L2 is used in the solution\n"
"bool gps_l2_used\n"
"\n"
"# True if GPS L5 is used in the solution\n"
"bool gps_l5_used\n"
"\n"
"# True if GLONASS L1 is used in the solution\n"
"bool glo_l1_used\n"
"\n"
"# True if GLONASS L2 is used in the solution\n"
"bool glo_l2_used\n"
;
  }

  static const char* value(const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
      stream.next(m.type);
      stream.next(m.gps_l1_used);
      stream.next(m.gps_l2_used);
      stream.next(m.gps_l5_used);
      stream.next(m.glo_l1_used);
      stream.next(m.glo_l2_used);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SbgGpsPosStatus_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sbg_driver::SbgGpsPosStatus_<ContainerAllocator>& v)
  {
    s << indent << "status: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.status);
    s << indent << "type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.type);
    s << indent << "gps_l1_used: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.gps_l1_used);
    s << indent << "gps_l2_used: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.gps_l2_used);
    s << indent << "gps_l5_used: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.gps_l5_used);
    s << indent << "glo_l1_used: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.glo_l1_used);
    s << indent << "glo_l2_used: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.glo_l2_used);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SBG_DRIVER_MESSAGE_SBGGPSPOSSTATUS_H
