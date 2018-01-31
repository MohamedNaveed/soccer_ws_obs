// Auto-generated. Do not edit!

// (in-package image_processing.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ball_predict {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.predicted_x = null;
      this.predicted_y = null;
    }
    else {
      if (initObj.hasOwnProperty('predicted_x')) {
        this.predicted_x = initObj.predicted_x
      }
      else {
        this.predicted_x = 0.0;
      }
      if (initObj.hasOwnProperty('predicted_y')) {
        this.predicted_y = initObj.predicted_y
      }
      else {
        this.predicted_y = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ball_predict
    // Serialize message field [predicted_x]
    bufferOffset = _serializer.float64(obj.predicted_x, buffer, bufferOffset);
    // Serialize message field [predicted_y]
    bufferOffset = _serializer.float64(obj.predicted_y, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ball_predict
    let len;
    let data = new ball_predict(null);
    // Deserialize message field [predicted_x]
    data.predicted_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [predicted_y]
    data.predicted_y = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'image_processing/ball_predict';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8ddf12d0486a66fc3a6ad21565f35185';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 predicted_x
    float64 predicted_y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ball_predict(null);
    if (msg.predicted_x !== undefined) {
      resolved.predicted_x = msg.predicted_x;
    }
    else {
      resolved.predicted_x = 0.0
    }

    if (msg.predicted_y !== undefined) {
      resolved.predicted_y = msg.predicted_y;
    }
    else {
      resolved.predicted_y = 0.0
    }

    return resolved;
    }
};

module.exports = ball_predict;
