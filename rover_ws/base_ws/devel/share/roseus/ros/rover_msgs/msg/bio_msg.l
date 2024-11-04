;; Auto-generated. Do not edit!


(when (boundp 'rover_msgs::bio_msg)
  (if (not (find-package "ROVER_MSGS"))
    (make-package "ROVER_MSGS"))
  (shadow 'bio_msg (find-package "ROVER_MSGS")))
(unless (find-package "ROVER_MSGS::BIO_MSG")
  (make-package "ROVER_MSGS::BIO_MSG"))

(in-package "ROS")
;;//! \htmlinclude bio_msg.msg.html


(defclass rover_msgs::bio_msg
  :super ros::object
  :slots (_drill _inner_cylinder _stepper ))

(defmethod rover_msgs::bio_msg
  (:init
   (&key
    ((:drill __drill) (instance rover_msgs::drive_msg :init))
    ((:inner_cylinder __inner_cylinder) (instance rover_msgs::drive_msg :init))
    ((:stepper __stepper) (instance rover_msgs::drive_msg :init))
    )
   (send-super :init)
   (setq _drill __drill)
   (setq _inner_cylinder __inner_cylinder)
   (setq _stepper __stepper)
   self)
  (:drill
   (&rest __drill)
   (if (keywordp (car __drill))
       (send* _drill __drill)
     (progn
       (if __drill (setq _drill (car __drill)))
       _drill)))
  (:inner_cylinder
   (&rest __inner_cylinder)
   (if (keywordp (car __inner_cylinder))
       (send* _inner_cylinder __inner_cylinder)
     (progn
       (if __inner_cylinder (setq _inner_cylinder (car __inner_cylinder)))
       _inner_cylinder)))
  (:stepper
   (&rest __stepper)
   (if (keywordp (car __stepper))
       (send* _stepper __stepper)
     (progn
       (if __stepper (setq _stepper (car __stepper)))
       _stepper)))
  (:serialization-length
   ()
   (+
    ;; rover_msgs/drive_msg _drill
    (send _drill :serialization-length)
    ;; rover_msgs/drive_msg _inner_cylinder
    (send _inner_cylinder :serialization-length)
    ;; rover_msgs/drive_msg _stepper
    (send _stepper :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; rover_msgs/drive_msg _drill
       (send _drill :serialize s)
     ;; rover_msgs/drive_msg _inner_cylinder
       (send _inner_cylinder :serialize s)
     ;; rover_msgs/drive_msg _stepper
       (send _stepper :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; rover_msgs/drive_msg _drill
     (send _drill :deserialize buf ptr-) (incf ptr- (send _drill :serialization-length))
   ;; rover_msgs/drive_msg _inner_cylinder
     (send _inner_cylinder :deserialize buf ptr-) (incf ptr- (send _inner_cylinder :serialization-length))
   ;; rover_msgs/drive_msg _stepper
     (send _stepper :deserialize buf ptr-) (incf ptr- (send _stepper :serialization-length))
   ;;
   self)
  )

(setf (get rover_msgs::bio_msg :md5sum-) "ce3326cb70451413da0fa73fa55e3748")
(setf (get rover_msgs::bio_msg :datatype-) "rover_msgs/bio_msg")
(setf (get rover_msgs::bio_msg :definition-)
      "drive_msg drill
drive_msg inner_cylinder
drive_msg stepper
================================================================================
MSG: rover_msgs/drive_msg
string direction
float64 speed
string mode
")



(provide :rover_msgs/bio_msg "ce3326cb70451413da0fa73fa55e3748")


