-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2023 at 11:35 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `userdata`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `username` varchar(50) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`username`, `password`) VALUES
('minaz', '1234'),
('niaz', '1234'),
('sojib', 'sojib1234'),
('safi', 'safi1234'),
('sojib102', 'sojibmc'),
('samiun', '1234'),
('datta', '1234'),
('arnob', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `detectobject`
--

CREATE TABLE `detectobject` (
  `username` varchar(50) NOT NULL,
  `file_name` varchar(50) NOT NULL,
  `file_path` varchar(100) NOT NULL,
  `date_time` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detectobject`
--

INSERT INTO `detectobject` (`username`, `file_name`, `file_path`, `date_time`) VALUES
('niaz', '1_objDect_Person.mp4', 'Z:/soft/final/1_objDect_Person.mp4', '2023-10-13 19:54:54');

-- --------------------------------------------------------

--
-- Table structure for table `summarizedvideo`
--

CREATE TABLE `summarizedvideo` (
  `username` varchar(50) NOT NULL,
  `file_name` varchar(50) NOT NULL,
  `file_path` varchar(100) NOT NULL,
  `date_time` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `summarizedvideo`
--

INSERT INTO `summarizedvideo` (`username`, `file_name`, `file_path`, `date_time`) VALUES
('arnob', 'Counting Up to 60 Seconds_summarized.mp4', 'S:/soft/final/Counting Up to 60 Seconds_summarized.mp4', '2023-10-12 23:33:59'),
('arnob', 'Counting Up to 60 Seconds_summarized.mp4', 'Z:/soft/final/Counting Up to 60 Seconds_summarized.mp4', '2023-10-12 23:39:42'),
('arnob', '1_summarized.mp4', 'Z:/soft/final/1_summarized.mp4', '2023-10-12 23:44:07'),
('niaz', '1_summarized.mp4', 'Z:/soft/final/1_summarized.mp4', '2023-10-13 18:00:57'),
('niaz', '1_summarized.mp4', 'Z:/soft/final/1_summarized.mp4', '2023-10-13 18:47:59');

-- --------------------------------------------------------

--
-- Table structure for table `uploadvideo`
--

CREATE TABLE `uploadvideo` (
  `username` varchar(50) NOT NULL,
  `file_name` varchar(50) NOT NULL,
  `file_path` varchar(100) NOT NULL,
  `date_time` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `uploadvideo`
--

INSERT INTO `uploadvideo` (`username`, `file_name`, `file_path`, `date_time`) VALUES
('arnob', 'Counting Up to 60 Seconds.mp4', 'C:/Users/navyn/Downloads/Counting Up to 60 Seconds.mp4', '2023-10-12 23:31:50'),
('arnob', 'Counting Up to 60 Seconds.mp4', 'C:/Users/navyn/Downloads/Counting Up to 60 Seconds.mp4', '2023-10-12 23:37:34'),
('arnob', 'Desktop 2023.10.01 - 23.17.59.01.mp4', 'C:/Users/navyn/Videos/Desktop/Desktop 2023.10.01 - 23.17.59.01.mp4', '2023-10-12 23:40:36'),
('arnob', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-12 23:42:02'),
('niaz', 'Untitled video - Made with Clipchamp.mp4', 'C:/Users/navyn/OneDrive/Desktop/Untitled video - Made with Clipchamp.mp4', '2023-10-13 16:44:56'),
('niaz', 'Untitled video - Made with Clipchamp.mp4', 'C:/Users/navyn/OneDrive/Desktop/Untitled video - Made with Clipchamp.mp4', '2023-10-13 16:59:20'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 17:03:02'),
('niaz', 'Untitled video - Made with Clipchamp.mp4', 'C:/Users/navyn/OneDrive/Desktop/Untitled video - Made with Clipchamp.mp4', '2023-10-13 17:03:06'),
('niaz', 'khecha.mp4', 'C:/Users/navyn/OneDrive/Desktop/khecha.mp4', '2023-10-13 17:03:09'),
('niaz', 'Untitled video - Made with Clipchamp.mp4', 'C:/Users/navyn/OneDrive/Desktop/Untitled video - Made with Clipchamp.mp4', '2023-10-13 17:03:27'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 17:18:14'),
('niaz', 'Untitled video - Made with Clipchamp.mp4', 'C:/Users/navyn/OneDrive/Desktop/Untitled video - Made with Clipchamp.mp4', '2023-10-13 17:30:33'),
('niaz', 'khecha.mp4', 'C:/Users/navyn/OneDrive/Desktop/khecha.mp4', '2023-10-13 17:30:44'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 17:30:56'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 17:32:43'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 17:32:51'),
('niaz', 'khecha.mp4', 'C:/Users/navyn/OneDrive/Desktop/khecha.mp4', '2023-10-13 17:33:14'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:00:42'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:01:54'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:03:15'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:04:10'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:04:31'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:04:50'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:05:08'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:05:32'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:05:46'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:17:21'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:17:37'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:17:48'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:18:22'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:35:19'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:35:46'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:38:00'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:38:47'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:43:27'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:44:01'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:44:41'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:45:24'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:46:22'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:46:30'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:46:38'),
('niaz', 'jhcfgjkghkgjhkkgjhk.mp4', 'C:/Users/navyn/OneDrive/Desktop/jhcfgjkghkgjhkkgjhk.mp4', '2023-10-13 18:46:47'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:47:11'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:47:26'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 18:47:44'),
('niaz', '1.mp4', 'Z:/soft/final/1.mp4', '2023-10-13 19:53:49');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
