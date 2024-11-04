; Auto-generated. Do not edit!


(cl:in-package rover_msgs-msg)


;//! \htmlinclude bio_msg.msg.html

(cl:defclass <bio_msg> (roslisp-msg-protocol:ros-message)
  ((drill
    :reader drill
    :initarg :drill
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (inner_cylinder
    :reader inner_cylinder
    :initarg :inner_cylinder
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg))
   (stepper
    :reader stepper
    :initarg :stepper
    :type rover_msgs-msg:drive_msg
    :initform (cl:make-instance 'rover_msgs-msg:drive_msg)))
)

(cl:defclass bio_msg (<bio_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <bio_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'bio_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rover_msgs-msg:<bio_msg> is deprecated: use rover_msgs-msg:bio_msg instead.")))

(cl:ensure-generic-function 'drill-val :lambda-list '(m))
(cl:defmethod drill-val ((m <bio_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:drill-val is deprecated.  Use rover_msgs-msg:drill instead.")
  (drill m))

(cl:ensure-generic-function 'inner_cylinder-val :lambda-list '(m))
(cl:defmethod inner_cylinder-val ((m <bio_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:inner_cylinder-val is deprecated.  Use rover_msgs-msg:inner_cylinder instead.")
  (inner_cylinder m))

(cl:ensure-generic-function 'stepper-val :lambda-list '(m))
(cl:defmethod stepper-val ((m <bio_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-msg:stepper-val is deprecated.  Use rover_msgs-msg:stepper instead.")
  (stepper m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <bio_msg>) ostream)
  "Serializes a message object of type '<bio_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'drill) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'inner_cylinder) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'stepper) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <bio_msg>) istream)
  "Deserializes a message object of type '<bio_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'drill) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'inner_cylinder) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'stepper) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<bio_msg>)))
  "Returns string type for a message object of type '<bio_msg>"
  "rover_msgs/bio_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bio_msg)))
  "Returns string type for a message object of type 'bio_msg"
  "rover_msgs/bio_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<bio_msg>)))
  "Returns md5sum for a message object of type '<bio_msg>"
  "ce3326cb70451413da0fa73fa55e3748")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'bio_msg)))
  "Returns md5sum for a message object of type 'bio_msg"
  "ce3326cb70451413da0fa73fa55e3748")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<bio_msg>)))
  "Returns full string definition for message of type '<bio_msg>"
  (cl:format cl:nil "drive_msg drill~%drive_msg inner_cylinder~%drive_msg stepper~%================================================================================~%MSG: rover_msgs/drive_msg~%string direction~%float64 speed~%string mode~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'bio_msg)))
  "Returns full string definition for message of type 'bio_msg"
  (cl:format cl:nil "drive_msg drill~%drive_msg inner_cylinder~%drive_msg stepper~%================================================================================~%MSG: rover_msgs/drive_msg~%string direction~%float64 speed~%string mode~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <bio_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'drill))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'inner_cylinder))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'stepper))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <bio_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'bio_msg
    (cl:cons ':drill (drill msg))
    (cl:cons ':inner_cylinder (inner_cylinder msg))
    (cl:cons ':stepper (stepper msg))
))
