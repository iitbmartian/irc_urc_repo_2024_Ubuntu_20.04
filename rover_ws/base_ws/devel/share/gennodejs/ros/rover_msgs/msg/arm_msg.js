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

class arm_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.shoulder_actuator = null;
      this.elbow_actuator = null;
      this.base_motor = null;
      this.wrist_actuator = null;
      this.elbow_motor = null;
      this.gripper = null;
      this.gripper_rot = null;
      this.finger_actuator = null;
      this.soil_box = null;
      this.bio = null;
    }
    else {
      if (initObj.hasOwnProperty('shoulder_actuator')) {
        this.shoulder_actuator = initObj.shoulder_actuator
      }
      else {
        this.shoulder_actuator = new drive_msg();
      }
      if (initObj.hasOwnProperty('elbow_actuator')) {
        this.elbow_actuator = initObj.elbow_actuator
      }
      else {
        this.elbow_actuator = new drive_msg();
      }
      if (initObj.hasOwnProperty('base_motor')) {
        this.base_motor = initObj.base_motor
      }
      else {
        this.base_motor = new drive_msg();
      }
      if (initObj.hasOwnProperty('wrist_actuator')) {
        this.wrist_actuator = initObj.wrist_actuator
      }
      else {
        this.wrist_actuator = new drive_msg();
      }
      if (initObj.hasOwnProperty('elbow_motor')) {
        this.elbow_motor = initObj.elbow_motor
      }
      else {
        this.elbow_motor = new drive_msg();
      }
      if (initObj.hasOwnProperty('gripper')) {
        this.gripper = initObj.gripper
      }
      else {
        this.gripper = new drive_msg();
      }
      if (initObj.hasOwnProperty('gripper_rot')) {
        this.gripper_rot = initObj.gripper_rot
      }
      else {
        this.gripper_rot = new drive_msg();
      }
      if (initObj.hasOwnProperty('finger_actuator')) {
        this.finger_actuator = initObj.finger_actuator
      }
      else {
        this.finger_actuator = new drive_msg();
      }
      if (initObj.hasOwnProperty('soil_box')) {
        this.soil_box = initObj.soil_box
      }
      else {
        this.soil_box = new drive_msg();
      }
      if (initObj.hasOwnProperty('bio')) {
        this.bio = initObj.bio
      }
      else {
        this.bio = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type arm_msg
    // Serialize message field [shoulder_actuator]
    bufferOffset = drive_msg.serialize(obj.shoulder_actuator, buffer, bufferOffset);
    // Serialize message field [elbow_actuator]
    bufferOffset = drive_msg.serialize(obj.elbow_actuator, buffer, bufferOffset);
    // Serialize message field [base_motor]
    bufferOffset = drive_msg.serialize(obj.base_motor, buffer, bufferOffset);
    // Serialize message field [wrist_actuator]
    bufferOffset = drive_msg.serialize(obj.wrist_actuator, buffer, bufferOffset);
    // Serialize message field [elbow_motor]
    bufferOffset = drive_msg.serialize(obj.elbow_motor, buffer, bufferOffset);
    // Serialize message field [gripper]
    bufferOffset = drive_msg.serialize(obj.gripper, buffer, bufferOffset);
    // Serialize message field [gripper_rot]
    bufferOffset = drive_msg.serialize(obj.gripper_rot, buffer, bufferOffset);
    // Serialize message field [finger_actuator]
    bufferOffset = drive_msg.serialize(obj.finger_actuator, buffer, bufferOffset);
    // Serialize message field [soil_box]
    bufferOffset = drive_msg.serialize(obj.soil_box, buffer, bufferOffset);
    // Serialize message field [bio]
    bufferOffset = _serializer.string(obj.bio, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type arm_msg
    let len;
    let data = new arm_msg(null);
    // Deserialize message field [shoulder_actuator]
    data.shoulder_actuator = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [elbow_actuator]
    data.elbow_actuator = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [base_motor]
    data.base_motor = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [wrist_actuator]
    data.wrist_actuator = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [elbow_motor]
    data.elbow_motor = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [gripper]
    data.gripper = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [gripper_rot]
    data.gripper_rot = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [finger_actuator]
    data.finger_actuator = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [soil_box]
    data.soil_box = drive_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [bio]
    data.bio = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += drive_msg.getMessageSize(object.shoulder_actuator);
    length += drive_msg.getMessageSize(object.elbow_actuator);
    length += drive_msg.getMessageSize(object.base_motor);
    length += drive_msg.getMessageSize(object.wrist_actuator);
    length += drive_msg.getMessageSize(object.elbow_motor);
    length += drive_msg.getMessageSize(object.gripper);
    length += drive_msg.getMessageSize(object.gripper_rot);
    length += drive_msg.getMessageSize(object.finger_actuator);
    length += drive_msg.getMessageSize(object.soil_box);
    length += _getByteLength(object.bio);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rover_msgs/arm_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '71499babfc2a932e972bf03c02baad13';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    drive_msg shoulder_actuator
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
    string mode
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new arm_msg(null);
    if (msg.shoulder_actuator !== undefined) {
      resolved.shoulder_actuator = drive_msg.Resolve(msg.shoulder_actuator)
    }
    else {
      resolved.shoulder_actuator = new drive_msg()
    }

    if (msg.elbow_actuator !== undefined) {
      resolved.elbow_actuator = drive_msg.Resolve(msg.elbow_actuator)
    }
    else {
      resolved.elbow_actuator = new drive_msg()
    }

    if (msg.base_motor !== undefined) {
      resolved.base_motor = drive_msg.Resolve(msg.base_motor)
    }
    else {
      resolved.base_motor = new drive_msg()
    }

    if (msg.wrist_actuator !== undefined) {
      resolved.wrist_actuator = drive_msg.Resolve(msg.wrist_actuator)
    }
    else {
      resolved.wrist_actuator = new drive_msg()
    }

    if (msg.elbow_motor !== undefined) {
      resolved.elbow_motor = drive_msg.Resolve(msg.elbow_motor)
    }
    else {
      resolved.elbow_motor = new drive_msg()
    }

    if (msg.gripper !== undefined) {
      resolved.gripper = drive_msg.Resolve(msg.gripper)
    }
    else {
      resolved.gripper = new drive_msg()
    }

    if (msg.gripper_rot !== undefined) {
      resolved.gripper_rot = drive_msg.Resolve(msg.gripper_rot)
    }
    else {
      resolved.gripper_rot = new drive_msg()
    }

    if (msg.finger_actuator !== undefined) {
      resolved.finger_actuator = drive_msg.Resolve(msg.finger_actuator)
    }
    else {
      resolved.finger_actuator = new drive_msg()
    }

    if (msg.soil_box !== undefined) {
      resolved.soil_box = drive_msg.Resolve(msg.soil_box)
    }
    else {
      resolved.soil_box = new drive_msg()
    }

    if (msg.bio !== undefined) {
      resolved.bio = msg.bio;
    }
    else {
      resolved.bio = ''
    }

    return resolved;
    }
};

module.exports = arm_msg;
