
(cl:in-package :asdf)

(defsystem "rover_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "arm_msg" :depends-on ("_package_arm_msg"))
    (:file "_package_arm_msg" :depends-on ("_package"))
    (:file "bio_msg" :depends-on ("_package_bio_msg"))
    (:file "_package_bio_msg" :depends-on ("_package"))
    (:file "drive_msg" :depends-on ("_package_drive_msg"))
    (:file "_package_drive_msg" :depends-on ("_package"))
  ))