// Auto-generated. Do not edit!

// (in-package image_processing.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class bot_state {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.num_circles = null;
      this.pose = null;
    }
    else {
      if (initObj.hasOwnProperty('num_circles')) {
        this.num_circles = initObj.num_circles
      }
      else {
        this.num_circles = 0;
      }
      if (initObj.hasOwnProperty('pose')) {
        this.pose = initObj.pose
      }
      else {
        this.pose = new geometry_msgs.msg.Pose2D();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type bot_state
    // Serialize message field [num_circles]
    bufferOffset = _serializer.int8(obj.num_circles, buffer, bufferOffset);
    // Serialize message field [pose]
    bufferOffset = geometry_msgs.msg.Pose2D.serialize(obj.pose, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type bot_state
    let len;
    let data = new bot_state(null);
    // Deserialize message field [num_circles]
    data.num_circles = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [pose]
    data.pose = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 25;
  }

  static datatype() {
    // Returns string type for a message object
    return 'image_processing/bot_state';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5b2e80437805ede8f38eb11e1d06bb53';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 num_circles
    geometry_msgs/Pose2D pose
    
    ================================================================================
    MSG: geometry_msgs/Pose2D
    # This expresses a position and orientation on a 2D manifold.
    
    float64 x
    float64 y
    float64 theta
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new bot_state(null);
    if (msg.num_circles !== undefined) {
      resolved.num_circles = msg.num_circles;
    }
    else {
      resolved.num_circles = 0
    }

    if (msg.pose !== undefined) {
      resolved.pose = geometry_msgs.msg.Pose2D.Resolve(msg.pose)
    }
    else {
      resolved.pose = new geometry_msgs.msg.Pose2D()
    }

    return resolved;
    }
};

module.exports = bot_state;
