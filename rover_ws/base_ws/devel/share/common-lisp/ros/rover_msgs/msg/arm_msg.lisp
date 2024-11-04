; Auto-generated. Do not edit!


(cl:in-package rover_msgs-msg)


;//! \htmlinclude arm_msg.msg.html

(cl:defclass <arm_msg> (roslisp-msg-protocol:ros-message)
  ((shoulder_actuator
    :reader shoulder_actuator
    :initarg :shoulder_actuator
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (elbow_actuator
    :reader elbow_actuator
    :initarg :elbow_actuator
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (base_motor
    :reader base_motor
    :initarg :base_motor
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (wrist_actuator
    :reader wrist_actuator
    :initarg :wrist_actuator
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (elbow_motor
    :reader elbow_motor
    :initarg :elbow_motor
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (gripper
    :reader gripper
    :initarg :gripper
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (gripper_rot
    :reader gripper_rot
    :initarg :gripper_rot
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (finger_actuator
    :reader finger_actuator
    :initarg :finger_actuator
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (soil_box
    :reader soil_box
    :initarg :soil_box
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (bio
    :reader bio
    :initarg :bio
    :type cl:string
    :initform ""))
)

(cl:defclass arm_msg (<arm_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <arm_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'arm_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rover_msgs-msg:<arm_msg> is deprecated: use rover_msgs-msg:arm_msg instead.")))

(cl:ensure-generic-function 'shoulder_actuator-val :lambda-list '(m))
(cl:defmethod shoulder_actuator-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:shoulder_actuator-val is deprecated.  Use rover_msgs-msg:shoulder_actuator instead.")
  (shoulder_actuator m))

(cl:ensure-generic-function 'elbow_actuator-val :lambda-list '(m))
(cl:defmethod elbow_actuator-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:elbow_actuator-val is deprecated.  Use rover_msgs-msg:elbow_actuator instead.")
  (elbow_actuator m))

(cl:ensure-generic-function 'base_motor-val :lambda-list '(m))
(cl:defmethod base_motor-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:base_motor-val is deprecated.  Use rover_msgs-msg:base_motor instead.")
  (base_motor m))

(cl:ensure-generic-function 'wrist_actuator-val :lambda-list '(m))
(cl:defmethod wrist_actuator-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:wrist_actuator-val is deprecated.  Use rover_msgs-msg:wrist_actuator instead.")
  (wrist_actuator m))

(cl:ensure-generic-function 'elbow_motor-val :lambda-list '(m))
(cl:defmethod elbow_motor-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:elbow_motor-val is deprecated.  Use rover_msgs-msg:elbow_motor instead.")
  (elbow_motor m))

(cl:ensure-generic-function 'gripper-val :lambda-list '(m))
(cl:defmethod gripper-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:gripper-val is deprecated.  Use rover_msgs-msg:gripper instead.")
  (gripper m))

(cl:ensure-generic-function 'gripper_rot-val :lambda-list '(m))
(cl:defmethod gripper_rot-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:gripper_rot-val is deprecated.  Use rover_msgs-msg:gripper_rot instead.")
  (gripper_rot m))

(cl:ensure-generic-function 'finger_actuator-val :lambda-list '(m))
(cl:defmethod finger_actuator-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:finger_actuator-val is deprecated.  Use rover_msgs-msg:finger_actuator instead.")
  (finger_actuator m))

(cl:ensure-generic-function 'soil_box-val :lambda-list '(m))
(cl:defmethod soil_box-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:soil_box-val is deprecated.  Use rover_msgs-msg:soil_box instead.")
  (soil_box m))

(cl:ensure-generic-function 'bio-val :lambda-list '(m))
(cl:defmethod bio-val ((m <arm_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:bio-val is deprecated.  Use rover_msgs-msg:bio instead.")
  (bio m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <arm_msg>) ostream)
  "Serializes a message object of type '<arm_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'shoulder_actuator) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'elbow_actuator) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'base_motor) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'wrist_actuator) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'elbow_motor) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gripper) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gripper_rot) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'finger_actuator) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'soil_box) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'bio))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'bio))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <arm_msg>) istream)
  "Deserializes a message object of type '<arm_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'shoulder_actuator) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'elbow_actuator) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'base_motor) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'wrist_actuator) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'elbow_motor) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gripper) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gripper_rot) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'finger_actuator) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'soil_box) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'bio) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'bio) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<arm_msg>)))
  "Returns string type for a message object of type '<arm_msg>"
  "rover_msgs/arm_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'arm_msg)))
  "Returns string type for a message object of type 'arm_msg"
  "rover_msgs/arm_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<arm_msg>)))
  "Returns md5sum for a message object of type '<arm_msg>"
  "71499babfc2a932e972bf03c02baad13")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'arm_msg)))
  "Returns md5sum for a message object of type 'arm_msg"
  "71499babfc2a932e972bf03c02baad13")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<arm_msg>)))
  "Returns full string definition for message of type '<arm_msg>"
  (cl:format cl:nil "drive_msg shoulder_actuator~%drive_msg elbow_actuator~%drive_msg base_motor~%drive_msg wrist_actuator~%drive_msg elbow_motor~%drive_msg gripper~%drive_msg gripper_rot~%drive_msg finger_actuator~%drive_msg soil_box~%string bio~%~%================================================================================~%MSG: rover_msgs/drive_msg~%string direction~%float64 speed~%string mode~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'arm_msg)))
  "Returns full string definition for message of type 'arm_msg"
  (cl:format cl:nil "drive_msg shoulder_actuator~%drive_msg elbow_actuator~%drive_msg base_motor~%drive_msg wrist_actuator~%drive_msg elbow_motor~%drive_msg gripper~%drive_msg gripper_rot~%drive_msg finger_actuator~%drive_msg soil_box~%string bio~%~%================================================================================~%MSG: rover_msgs/drive_msg~%string direction~%float64 speed~%string mode~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <arm_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'shoulder_actuator))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'elbow_actuator))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'base_motor))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'wrist_actuator))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'elbow_motor))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gripper))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gripper_rot))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'finger_actuator))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'soil_box))
     4 (cl:length (cl:slot-value msg 'bio))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <arm_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'arm_msg
    (cl:cons ':shoulder_actuator (shoulder_actuator msg))
    (cl:cons ':elbow_actuator (elbow_actuator msg))
    (cl:cons ':base_motor (base_motor msg))
    (cl:cons ':wrist_actuator (wrist_actuator msg))
    (cl:cons ':elbow_motor (elbow_motor msg))
    (cl:cons ':gripper (gripper msg))
    (cl:cons ':gripper_rot (gripper_rot msg))
    (cl:cons ':finger_actuator (finger_actuator msg))
    (cl:cons ':soil_box (soil_box msg))
    (cl:cons ':bio (bio msg))
))
