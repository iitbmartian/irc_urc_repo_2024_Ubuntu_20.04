// Auto-generated. Do not edit!

// (in-package rover_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let drive_msg = require('./drive_msg.js');

//-----------------------------------------------------------

class bio_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.drill = null;
      this.inner_cylinder = null;
      this.stepper = null;
    }
    else {
      if (initObj.hasOwnProperty('drill')) {
        this.drill = initObj.drill
      }
      else {
        this.drill = new drive_msg();
      }
      if (initObj.hasOwnProperty('inner_cylinder')) {
        this.inner_cylinder = initObj.inner_cylinder
      }
      else {
        this.inner_cylinder = new drive_msg();
      }
      if (initObj.hasOwnProperty('stepper')) {
        this.stepper = initObj.stepper
      }
      else {
        this.stepper = new drive_msg();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type bio_msg
    // Serialize message field [drill]
    bufferOffset = drive_msg.serialize(obj.drill, buffer, bufferOffset);
    // Serialize message field [inner_cylinder]
    bufferOffset = drive_msg.serialize(obj.inner_cylinder, buffer, bufferOffset);
    // Serialize message field [stepper]
    bufferOffset = drive_msg.serialize(obj.stepper, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type bio_msg
    let len;
    let data = new bio_msg(null);
    // Deserialize message field [drill]
    data.drill = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [inner_cylinder]
    data.inner_cylinder = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [stepper]
    data.stepper = drive_msg.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += drive_msg.getMessageSize(object.drill);
    length += drive_msg.getMessageSize(object.inner_cylinder);
    length += drive_msg.getMessageSize(object.stepper);
    return length;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rover_msgs/bio_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ce3326cb70451413da0fa73fa55e3748';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    drive_msg drill
    drive_msg inner_cylinder
    drive_msg stepper
    ================================================================================
    MSG: rover_msgs/drive_msg
    string direction
    float64 speed
    string mode
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new bio_msg(null);
    if (msg.drill !== undefined) {
      resolved.drill = drive_msg.Resolve(msg.drill)
    }
    else {
      resolved.drill = new drive_msg()
    }

    if (msg.inner_cylinder !== undefined) {
      resolved.inner_cylinder = drive_msg.Resolve(msg.inner_cylinder)
    }
    else {
      resolved.inner_cylinder = new drive_msg()
    }

    if (msg.stepper !== undefined) {
      resolved.stepper = drive_msg.Resolve(msg.stepper)
    }
    else {
      resolved.stepper = new drive_msg()
    }

    return resolved;
    }
};

module.exports = bio_msg;
