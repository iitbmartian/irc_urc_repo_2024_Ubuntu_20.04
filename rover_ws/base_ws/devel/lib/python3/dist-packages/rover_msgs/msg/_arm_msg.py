# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rover_msgs/arm_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rover_msgs.msg

class arm_msg(genpy.Message):
  _md5sum = "71499babfc2a932e972bf03c02baad13"
  _type = "rover_msgs/arm_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """drive_msg shoulder_actuator
drive_msg elbow_actuator
drive_msg base_motor
drive_msg wrist_actuator
drive_msg elbow_motor
drive_msg gripper
drive_msg gripper_rot
drive_msg finger_actuator
drive_msg soil_box
string bio

================================================================================
MSG: rover_msgs/drive_msg
string direction
float64 speed
string mode"""
  __slots__ = ['shoulder_actuator','elbow_actuator','base_motor','wrist_actuator','elbow_motor','gripper','gripper_rot','finger_actuator','soil_box','bio']
  _slot_types = ['rover_msgs/drive_msg','rover_msgs/drive_msg','rover_msgs/drive_msg','rover_msgs/drive_msg','rover_msgs/drive_msg','rover_msgs/drive_msg','rover_msgs/drive_msg','rover_msgs/drive_msg','rover_msgs/drive_msg','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       shoulder_actuator,elbow_actuator,base_motor,wrist_actuator,elbow_motor,gripper,gripper_rot,finger_actuator,soil_box,bio

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(arm_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.shoulder_actuator is None:
        self.shoulder_actuator = rover_msgs.msg.drive_msg()
      if self.elbow_actuator is None:
        self.elbow_actuator = rover_msgs.msg.drive_msg()
      if self.base_motor is None:
        self.base_motor = rover_msgs.msg.drive_msg()
      if self.wrist_actuator is None:
        self.wrist_actuator = rover_msgs.msg.drive_msg()
      if self.elbow_motor is None:
        self.elbow_motor = rover_msgs.msg.drive_msg()
      if self.gripper is None:
        self.gripper = rover_msgs.msg.drive_msg()
      if self.gripper_rot is None:
        self.gripper_rot = rover_msgs.msg.drive_msg()
      if self.finger_actuator is None:
        self.finger_actuator = rover_msgs.msg.drive_msg()
      if self.soil_box is None:
        self.soil_box = rover_msgs.msg.drive_msg()
      if self.bio is None:
        self.bio = ''
    else:
      self.shoulder_actuator = rover_msgs.msg.drive_msg()
      self.elbow_actuator = rover_msgs.msg.drive_msg()
      self.base_motor = rover_msgs.msg.drive_msg()
      self.wrist_actuator = rover_msgs.msg.drive_msg()
      self.elbow_motor = rover_msgs.msg.drive_msg()
      self.gripper = rover_msgs.msg.drive_msg()
      self.gripper_rot = rover_msgs.msg.drive_msg()
      self.finger_actuator = rover_msgs.msg.drive_msg()
      self.soil_box = rover_msgs.msg.drive_msg()
      self.bio = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.shoulder_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.shoulder_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.shoulder_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.elbow_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.base_motor.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.base_motor.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.base_motor.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.wrist_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.wrist_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.wrist_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_motor.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_motor.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.elbow_motor.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.gripper.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper_rot.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper_rot.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.gripper_rot.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.finger_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.finger_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.finger_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.soil_box.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.soil_box.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.soil_box.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.bio
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.shoulder_actuator is None:
        self.shoulder_actuator = rover_msgs.msg.drive_msg()
      if self.elbow_actuator is None:
        self.elbow_actuator = rover_msgs.msg.drive_msg()
      if self.base_motor is None:
        self.base_motor = rover_msgs.msg.drive_msg()
      if self.wrist_actuator is None:
        self.wrist_actuator = rover_msgs.msg.drive_msg()
      if self.elbow_motor is None:
        self.elbow_motor = rover_msgs.msg.drive_msg()
      if self.gripper is None:
        self.gripper = rover_msgs.msg.drive_msg()
      if self.gripper_rot is None:
        self.gripper_rot = rover_msgs.msg.drive_msg()
      if self.finger_actuator is None:
        self.finger_actuator = rover_msgs.msg.drive_msg()
      if self.soil_box is None:
        self.soil_box = rover_msgs.msg.drive_msg()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.shoulder_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.shoulder_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.shoulder_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.shoulder_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.shoulder_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.elbow_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_motor.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.base_motor.direction = str[start:end]
      start = end
      end += 8
      (self.base_motor.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_motor.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.base_motor.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.wrist_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.wrist_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.wrist_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.wrist_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.wrist_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_motor.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_motor.direction = str[start:end]
      start = end
      end += 8
      (self.elbow_motor.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_motor.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_motor.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper.direction = str[start:end]
      start = end
      end += 8
      (self.gripper.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper_rot.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper_rot.direction = str[start:end]
      start = end
      end += 8
      (self.gripper_rot.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper_rot.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper_rot.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.finger_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.finger_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.finger_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.finger_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.finger_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.soil_box.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.soil_box.direction = str[start:end]
      start = end
      end += 8
      (self.soil_box.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.soil_box.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.soil_box.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bio = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bio = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.shoulder_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.shoulder_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.shoulder_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.elbow_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.base_motor.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.base_motor.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.base_motor.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.wrist_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.wrist_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.wrist_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_motor.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.elbow_motor.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.elbow_motor.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.gripper.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper_rot.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper_rot.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.gripper_rot.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.finger_actuator.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.finger_actuator.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.finger_actuator.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.soil_box.direction
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.soil_box.speed
      buff.write(_get_struct_d().pack(_x))
      _x = self.soil_box.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.bio
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.shoulder_actuator is None:
        self.shoulder_actuator = rover_msgs.msg.drive_msg()
      if self.elbow_actuator is None:
        self.elbow_actuator = rover_msgs.msg.drive_msg()
      if self.base_motor is None:
        self.base_motor = rover_msgs.msg.drive_msg()
      if self.wrist_actuator is None:
        self.wrist_actuator = rover_msgs.msg.drive_msg()
      if self.elbow_motor is None:
        self.elbow_motor = rover_msgs.msg.drive_msg()
      if self.gripper is None:
        self.gripper = rover_msgs.msg.drive_msg()
      if self.gripper_rot is None:
        self.gripper_rot = rover_msgs.msg.drive_msg()
      if self.finger_actuator is None:
        self.finger_actuator = rover_msgs.msg.drive_msg()
      if self.soil_box is None:
        self.soil_box = rover_msgs.msg.drive_msg()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.shoulder_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.shoulder_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.shoulder_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.shoulder_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.shoulder_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.elbow_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_motor.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.base_motor.direction = str[start:end]
      start = end
      end += 8
      (self.base_motor.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_motor.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.base_motor.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.wrist_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.wrist_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.wrist_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.wrist_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.wrist_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_motor.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_motor.direction = str[start:end]
      start = end
      end += 8
      (self.elbow_motor.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.elbow_motor.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.elbow_motor.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper.direction = str[start:end]
      start = end
      end += 8
      (self.gripper.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper_rot.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper_rot.direction = str[start:end]
      start = end
      end += 8
      (self.gripper_rot.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.gripper_rot.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.gripper_rot.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.finger_actuator.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.finger_actuator.direction = str[start:end]
      start = end
      end += 8
      (self.finger_actuator.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.finger_actuator.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.finger_actuator.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.soil_box.direction = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.soil_box.direction = str[start:end]
      start = end
      end += 8
      (self.soil_box.speed,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.soil_box.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.soil_box.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bio = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.bio = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
