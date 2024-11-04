;; Auto-generated. Do not edit!


(when (boundp 'rover_msgs::arm_msg)
  (if (not (find-package "ROVER_MSGS"))
    (make-package "ROVER_MSGS"))
  (shadow 'arm_msg (find-package "ROVER_MSGS")))
(unless (find-package "ROVER_MSGS::ARM_MSG")
  (make-package "ROVER_MSGS::ARM_MSG"))

(in-package "ROS")
;;//! \htmlinclude arm_msg.msg.html


(defclass rover_msgs::arm_msg
  :super ros::object
  :slots (_shoulder_actuator _elbow_actuator _base_motor _wrist_actuator _elbow_motor _gripper _gripper_rot _finger_actuator _soil_box _bio ))

(defmethod rover_msgs::arm_msg
  (:init
   (&key
    ((:shoulder_actuator __shoulder_actuator) (instance rover_msgs::drive_msg :init))
    ((:elbow_actuator __elbow_actuator) (instance rover_msgs::drive_msg :init))
    ((:base_motor __base_motor) (instance rover_msgs::drive_msg :init))
    ((:wrist_actuator __wrist_actuator) (instance rover_msgs::drive_msg :init))
    ((:elbow_motor __elbow_motor) (instance rover_msgs::drive_msg :init))
    ((:gripper __gripper) (instance rover_msgs::drive_msg :init))
    ((:gripper_rot __gripper_rot) (instance rover_msgs::drive_msg :init))
    ((:finger_actuator __finger_actuator) (instance rover_msgs::drive_msg :init))
    ((:soil_box __soil_box) (instance rover_msgs::drive_msg :init))
    ((:bio __bio) "")
    )
   (send-super :init)
   (setq _shoulder_actuator __shoulder_actuator)
   (setq _elbow_actuator __elbow_actuator)
   (setq _base_motor __base_motor)
   (setq _wrist_actuator __wrist_actuator)
   (setq _elbow_motor __elbow_motor)
   (setq _gripper __gripper)
   (setq _gripper_rot __gripper_rot)
   (setq _finger_actuator __finger_actuator)
   (setq _soil_box __soil_box)
   (setq _bio (string __bio))
   self)
  (:shoulder_actuator
   (&rest __shoulder_actuator)
   (if (keywordp (car __shoulder_actuator))
       (send* _shoulder_actuator __shoulder_actuator)
     (progn
       (if __shoulder_actuator (setq _shoulder_actuator (car __shoulder_actuator)))
       _shoulder_actuator)))
  (:elbow_actuator
   (&rest __elbow_actuator)
   (if (keywordp (car __elbow_actuator))
       (send* _elbow_actuator __elbow_actuator)
     (progn
       (if __elbow_actuator (setq _elbow_actuator (car __elbow_actuator)))
       _elbow_actuator)))
  (:base_motor
   (&rest __base_motor)
   (if (keywordp (car __base_motor))
       (send* _base_motor __base_motor)
     (progn
       (if __base_motor (setq _base_motor (car __base_motor)))
       _base_motor)))
  (:wrist_actuator
   (&rest __wrist_actuator)
   (if (keywordp (car __wrist_actuator))
       (send* _wrist_actuator __wrist_actuator)
     (progn
       (if __wrist_actuator (setq _wrist_actuator (car __wrist_actuator)))
       _wrist_actuator)))
  (:elbow_motor
   (&rest __elbow_motor)
   (if (keywordp (car __elbow_motor))
       (send* _elbow_motor __elbow_motor)
     (progn
       (if __elbow_motor (setq _elbow_motor (car __elbow_motor)))
       _elbow_motor)))
  (:gripper
   (&rest __gripper)
   (if (keywordp (car __gripper))
       (send* _gripper __gripper)
     (progn
       (if __gripper (setq _gripper (car __gripper)))
       _gripper)))
  (:gripper_rot
   (&rest __gripper_rot)
   (if (keywordp (car __gripper_rot))
       (send* _gripper_rot __gripper_rot)
     (progn
       (if __gripper_rot (setq _gripper_rot (car __gripper_rot)))
       _gripper_rot)))
  (:finger_actuator
   (&rest __finger_actuator)
   (if (keywordp (car __finger_actuator))
       (send* _finger_actuator __finger_actuator)
     (progn
       (if __finger_actuator (setq _finger_actuator (car __finger_actuator)))
       _finger_actuator)))
  (:soil_box
   (&rest __soil_box)
   (if (keywordp (car __soil_box))
       (send* _soil_box __soil_box)
     (progn
       (if __soil_box (setq _soil_box (car __soil_box)))
       _soil_box)))
  (:bio
   (&optional __bio)
   (if __bio (setq _bio __bio)) _bio)
  (:serialization-length
   ()
   (+
    ;; rover_msgs/drive_msg _shoulder_actuator
    (send _shoulder_actuator :serialization-length)
    ;; rover_msgs/drive_msg _elbow_actuator
    (send _elbow_actuator :serialization-length)
    ;; rover_msgs/drive_msg _base_motor
    (send _base_motor :serialization-length)
    ;; rover_msgs/drive_msg _wrist_actuator
    (send _wrist_actuator :serialization-length)
    ;; rover_msgs/drive_msg _elbow_motor
    (send _elbow_motor :serialization-length)
    ;; rover_msgs/drive_msg _gripper
    (send _gripper :serialization-length)
    ;; rover_msgs/drive_msg _gripper_rot
    (send _gripper_rot :serialization-length)
    ;; rover_msgs/drive_msg _finger_actuator
    (send _finger_actuator :serialization-length)
    ;; rover_msgs/drive_msg _soil_box
    (send _soil_box :serialization-length)
    ;; string _bio
    4 (length _bio)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; rover_msgs/drive_msg _shoulder_actuator
       (send _shoulder_actuator :serialize s)
     ;; rover_msgs/drive_msg _elbow_actuator
       (send _elbow_actuator :serialize s)
     ;; rover_msgs/drive_msg _base_motor
       (send _base_motor :serialize s)
     ;; rover_msgs/drive_msg _wrist_actuator
       (send _wrist_actuator :serialize s)
     ;; rover_msgs/drive_msg _elbow_motor
       (send _elbow_motor :serialize s)
     ;; rover_msgs/drive_msg _gripper
       (send _gripper :serialize s)
     ;; rover_msgs/drive_msg _gripper_rot
       (send _gripper_rot :serialize s)
     ;; rover_msgs/drive_msg _finger_actuator
       (send _finger_actuator :serialize s)
     ;; rover_msgs/drive_msg _soil_box
       (send _soil_box :serialize s)
     ;; string _bio
       (write-long (length _bio) s) (princ _bio s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; rover_msgs/drive_msg _shoulder_actuator
     (send _shoulder_actuator :deserialize buf ptr-) (incf ptr- (send _shoulder_actuator :serialization-length))
   ;; rover_msgs/drive_msg _elbow_actuator
     (send _elbow_actuator :deserialize buf ptr-) (incf ptr- (send _elbow_actuator :serialization-length))
   ;; rover_msgs/drive_msg _base_motor
     (send _base_motor :deserialize buf ptr-) (incf ptr- (send _base_motor :serialization-length))
   ;; rover_msgs/drive_msg _wrist_actuator
     (send _wrist_actuator :deserialize buf ptr-) (incf ptr- (send _wrist_actuator :serialization-length))
   ;; rover_msgs/drive_msg _elbow_motor
     (send _elbow_motor :deserialize buf ptr-) (incf ptr- (send _elbow_motor :serialization-length))
   ;; rover_msgs/drive_msg _gripper
     (send _gripper :deserialize buf ptr-) (incf ptr- (send _gripper :serialization-length))
   ;; rover_msgs/drive_msg _gripper_rot
     (send _gripper_rot :deserialize buf ptr-) (incf ptr- (send _gripper_rot :serialization-length))
   ;; rover_msgs/drive_msg _finger_actuator
     (send _finger_actuator :deserialize buf ptr-) (incf ptr- (send _finger_actuator :serialization-length))
   ;; rover_msgs/drive_msg _soil_box
     (send _soil_box :deserialize buf ptr-) (incf ptr- (send _soil_box :serialization-length))
   ;; string _bio
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _bio (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get rover_msgs::arm_msg :md5sum-) "71499babfc2a932e972bf03c02baad13")
(setf (get rover_msgs::arm_msg :datatype-) "rover_msgs/arm_msg")
(setf (get rover_msgs::arm_msg :definition-)
      "drive_msg shoulder_actuator
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
")



(provide :rover_msgs/arm_msg "71499babfc2a932e972bf03c02baad13")


