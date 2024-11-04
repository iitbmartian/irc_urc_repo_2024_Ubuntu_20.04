;; Auto-generated. Do not edit!


(when (boundp 'rover_msgs::drive_msg)
  (if (not (find-package "ROVER_MSGS"))
    (make-package "ROVER_MSGS"))
  (shadow 'drive_msg (find-package "ROVER_MSGS")))
(unless (find-package "ROVER_MSGS::DRIVE_MSG")
  (make-package "ROVER_MSGS::DRIVE_MSG"))

(in-package "ROS")
;;//! \htmlinclude drive_msg.msg.html


(defclass rover_msgs::drive_msg
  :super ros::object
  :slots (_direction _speed _mode ))

(defmethod rover_msgs::drive_msg
  (:init
   (&key
    ((:direction __direction) "")
    ((:speed __speed) 0.0)
    ((:mode __mode) "")
    )
   (send-super :init)
   (setq _direction (string __direction))
   (setq _speed (float __speed))
   (setq _mode (string __mode))
   self)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:serialization-length
   ()
   (+
    ;; string _direction
    4 (length _direction)
    ;; float64 _speed
    8
    ;; string _mode
    4 (length _mode)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _direction
       (write-long (length _direction) s) (princ _direction s)
     ;; float64 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; string _mode
       (write-long (length _mode) s) (princ _mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _direction
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _direction (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _speed
     (setq _speed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _mode
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _mode (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get rover_msgs::drive_msg :md5sum-) "dd483411e489ff081154f8cefaf4e01e")
(setf (get rover_msgs::drive_msg :datatype-) "rover_msgs/drive_msg")
(setf (get rover_msgs::drive_msg :definition-)
      "string direction
float64 speed
string mode
")



(provide :rover_msgs/drive_msg "dd483411e489ff081154f8cefaf4e01e")


