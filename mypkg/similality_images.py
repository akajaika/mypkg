##!/usr/bin/env python
# SPDX-FileCopyrightText: 2025 Kai Nonaka
# SPDX-License-Identifier: BSD-3-Clause:

import cv2
import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String

class SimilarityPublisher(Node):
    def __init__(self):
        super().__init__('similarity_publisher')
        self.similarity_publisher = self.create_publisher(Float32MultiArray, 'similar', 10)
        self.filename_publisher = self.create_publisher(String, 'file_names', 10)
        self.process_images()

    def process_images(self):
        TARGET_FILE = 'target.png'
        IMG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../..'))+'/src/mypkg/mypkg/images/'
        IMG_SIZE = (200, 200)

        # ターゲット画像の準備
        target_img_path = IMG_DIR + TARGET_FILE
        target_img = cv2.imread(target_img_path, cv2.IMREAD_GRAYSCALE)
        if target_img is None:
            self.get_logger().error(f"Target image {TARGET_FILE} not found!")
            return
        target_img = cv2.resize(target_img, IMG_SIZE)
        (target_kp, target_des) = cv2.AKAZE_create().detectAndCompute(target_img, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)

        # 類似度結果を格納する配列
        similarity_results = []
        filenames = []

        # 画像ディレクトリのすべてのファイルを処理
        files = os.listdir(IMG_DIR)

        for file in files:
            if file == TARGET_FILE:
                continue

            try:
                comparing_img_path = os.path.join(IMG_DIR, file)
                comparing_img = cv2.imread(comparing_img_path, cv2.IMREAD_GRAYSCALE)
                if comparing_img is None:
                    self.get_logger().warn(f"Could not read {file}, skipping.")
                    continue
                comparing_img = cv2.resize(comparing_img, IMG_SIZE)

                (comparing_kp, comparing_des) = cv2.AKAZE_create().detectAndCompute(comparing_img, None)
                if comparing_des is None:
                    self.get_logger().warn(f"No descriptors found in {file}. Skipping.")
                    continue

                matches = bf.match(target_des, comparing_des)
                if not matches:
                    self.get_logger().warn(f"No matches found for {file}.")
                    continue

                dist = [m.distance for m in matches]
                ret = sum(dist) / len(dist)
                filenames.append(file)
                similarity_results.append(ret)
            except cv2.error as e:
                self.get_logger().error(f"OpenCV error with file {file}: {e}")
            except Exception as e:
                self.get_logger().error(f"Unexpected error with file {file}: {e}")

        # ROS トピックに配信
        array_points = Float32MultiArray()
        array_points.data = similarity_results
        self.similarity_publisher.publish(array_points)

        filenames_array = String()
        filenames_array.data = ', '.join(filenames) 
        self.filename_publisher.publish(filenames_array)


def main():
    rclpy.init()
    node = SimilarityPublisher()
    rclpy.shutdown()
    node.destroy_node()


if __name__ == '__main__':
    main()
