/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : student_system

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 19/03/2023 09:59:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `course_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `course_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `teacher_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `
start_time` date NULL DEFAULT NULL,
  `
end_time` date NULL DEFAULT NULL,
  `max_student` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`course_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('co_2022001', 'Politics', 'te_001', '2023-03-08', '2023-03-01', 100);
INSERT INTO `course` VALUES ('co_2022002', 'Politics', 'te_002', '2023-02-02', '2023-03-16', 80);
INSERT INTO `course` VALUES ('co_2022003', 'JAVA', 'te_004', '2022-11-17', '2023-04-05', 80);
INSERT INTO `course` VALUES ('co_2022004', 'C#', 'te_004', '2022-12-01', '2023-05-12', 100);
INSERT INTO `course` VALUES ('co_2022005', 'Datebase', 'te_003', '2022-06-16', '2023-12-21', 80);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `student_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `student_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `subject` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `age` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `dormitory` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`student_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('std_2019015', 'Jack', 'mechanical engineering', '18744444444', '25', '1', '5');
INSERT INTO `student` VALUES ('std_2021788', 'Tom', 'accounting', '14477777777', '24', '1', '10');
INSERT INTO `student` VALUES ('std_2022001', 'Rose', 'computer science', '15677777777', '25', '1', '9');
INSERT INTO `student` VALUES ('std_2022045', 'snow', 'english', '77777777777', '23', '2', '8');

-- ----------------------------
-- Table structure for student_course_select
-- ----------------------------
DROP TABLE IF EXISTS `student_course_select`;
CREATE TABLE `student_course_select`  (
  `student_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `course_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `score` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`student_id`, `course_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_course_select
-- ----------------------------
INSERT INTO `student_course_select` VALUES ('std_2019015', 'co_2022001', 80);
INSERT INTO `student_course_select` VALUES ('std_2019015', 'co_2022003', 95);
INSERT INTO `student_course_select` VALUES ('std_2019015', 'co_2022004', 90);
INSERT INTO `student_course_select` VALUES ('std_2021788', 'co_2022004', 80);
INSERT INTO `student_course_select` VALUES ('std_2022045', 'co_2022002', 70);
INSERT INTO `student_course_select` VALUES ('std_2022045', 'co_2022004', 67);

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `teacher_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `teacher_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `position` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`teacher_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('te_001', 'Frank', '14477995555', 'Professor');
INSERT INTO `teacher` VALUES ('te_002', 'York', '23355555555', 'lecturer');
INSERT INTO `teacher` VALUES ('te_003', 'Saber', '77777777777', 'Professor');
INSERT INTO `teacher` VALUES ('te_004', 'Jim', '33366664444', 'lecturer');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '123', '123');

SET FOREIGN_KEY_CHECKS = 1;
