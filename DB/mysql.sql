CREATE DATABASE tourguide
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

-- 
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE tourguide;

--
-- Create table `user`
--
CREATE TABLE user (
  UserID char(36) NOT NULL DEFAULT '',
  UserName char(100) NOT NULL DEFAULT '',
  Password char(15) NOT NULL DEFAULT '',
  Email char(150) NOT NULL DEFAULT '',
  PhoneNumber char(20) NOT NULL DEFAULT '',
  IdentityNumber char(20) NOT NULL DEFAULT '',
  PRIMARY KEY (UserID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;


--
-- Create table `admin`
--
CREATE TABLE admin (
  RefID char(36) NOT NULL DEFAULT '',
  UserName char(100) NOT NULL DEFAULT '',
  Password char(15) NOT NULL DEFAULT '',
  Email char(150) NOT NULL DEFAULT '',
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create table `listpartner`
--
CREATE TABLE listpartner (
  RefID char(36) NOT NULL DEFAULT '',
  UserName char(100) DEFAULT NULL,
  Password char(15) DEFAULT NULL,
  Code char(20) DEFAULT NULL,
  Name varchar(50) DEFAULT NULL,
  PhoneNumber char(20) DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;


--
-- Create table `province`
--
CREATE TABLE province (
  ProvinceID char(36) NOT NULL DEFAULT '',
  ProvinceName varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (ProvinceID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;


--
-- Create table `district`
--
CREATE TABLE district (
  DistrictID char(36) NOT NULL DEFAULT '',
  ProvinceID char(36) NOT NULL DEFAULT '',
  DistrictName varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (DistrictID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE district
ADD CONSTRAINT FK_District_ProvinceID FOREIGN KEY (ProvinceID)
REFERENCES province (ProvinceID);


--
-- Create table `tourdestination`
--
CREATE TABLE tourdestination (
  RefID char(36) NOT NULL DEFAULT '',
  ProvinceID char(36) NOT NULL DEFAULT '',
  DistrictID char(36) NOT NULL DEFAULT '',
  Name varchar(150) NOT NULL DEFAULT '',
  Place varchar(500) DEFAULT NULL,
  Described text NOT NULL,
  TicketPrice text NOT NULL COMMENT '{Adult: ‘’, Child: ‘’, Baby: ‘’}',
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE tourdestination
ADD CONSTRAINT FK_TourDestination_DistrictID FOREIGN KEY (DistrictID)
REFERENCES district (DistrictID);

--
-- Create foreign key
--
ALTER TABLE tourdestination
ADD CONSTRAINT FK_TourDestination_ProvinceID FOREIGN KEY (ProvinceID)
REFERENCES province (ProvinceID);

--
-- Create table `chatroom`
--
CREATE TABLE chatroom (
  RefID char(36) NOT NULL DEFAULT '',
  UserID char(36) NOT NULL DEFAULT '',
  CreationDate datetime DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE chatroom
ADD CONSTRAINT FK_ChatRoom_UserID FOREIGN KEY (UserID)
REFERENCES user (UserID);

--
-- Create table `contentmessagesend`
--
CREATE TABLE contentmessagesend (
  RefID char(36) NOT NULL DEFAULT '',
  RoomID char(36) NOT NULL DEFAULT '',
  Content text NOT NULL,
  SendingTime datetime DEFAULT NULL,
  TypeOfContent int NOT NULL COMMENT '0: tin nhắn văn bảng, 1: hình ảnh',
  RoleInConversation int NOT NULL COMMENT '0: tin nhắn của admin, 1: tin nhắn của user',
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE contentmessagesend
ADD CONSTRAINT FK_ContentMessageSend_RoomID FOREIGN KEY (RoomID)
REFERENCES chatroom (RefID);


--
-- Create table `listsendmessagetoadmin`
--
CREATE TABLE listsendmessagetoadmin (
  RefID char(36) NOT NULL DEFAULT '',
  UserID char(36) NOT NULL DEFAULT '',
  RoomID char(36) NOT NULL DEFAULT '',
  UserName char(100) DEFAULT NULL,
  LastSendingTime datetime DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE listsendmessagetoadmin
ADD CONSTRAINT FK_ListSendMessageToAdmin_UserID FOREIGN KEY (UserID)
REFERENCES user (UserID);

ALTER TABLE listsendmessagetoadmin
ADD CONSTRAINT FK_ListSendMessageToAdmin_RoomID FOREIGN KEY (RoomID)
REFERENCES chatroom (RefID);


--
-- Create table `tour`
--
CREATE TABLE tour (
  TourID char(36) NOT NULL DEFAULT '',
  TourContractXMLID char(36) NOT NULL DEFAULT '',
  TourContractID char(36) DEFAULT NULL,
  UserID char(36) DEFAULT NULL,
  TourCode char(100) DEFAULT NULL,
  TourName varchar(500) DEFAULT NULL,
  StartTime datetime DEFAULT NULL,
  TimeOfTour int DEFAULT NULL,
  IsSample int DEFAULT NULL COMMENT '1 là tour mẫu',
  Status int DEFAULT NULL COMMENT '0 là ngừng sử dụng',
  IsPayment int DEFAULT NULL COMMENT '1 là đã thanh toán',
  PRIMARY KEY (TourID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE tour
ADD CONSTRAINT FK_Tour_UserID FOREIGN KEY (UserID)
REFERENCES user (UserID);

--
-- Create table `hotel`
--
CREATE TABLE hotel (
  HotelID char(36) NOT NULL DEFAULT '',
  PartnerID char(36) NOT NULL DEFAULT '',
  HotelCode char(100) DEFAULT NULL,
  Name varchar(50) DEFAULT NULL,
  Email char(150) DEFAULT NULL,
  PhoneNumber char(20) DEFAULT NULL,
  Solgan varchar(500) DEFAULT NULL,
  Described text NOT NULL,
  Address varchar(500) DEFAULT NULL,
  Acreage float DEFAULT NULL COMMENT 'diện tích',
  `Rank` int DEFAULT NULL COMMENT '1-5',
  SortDescribed text NOT NULL COMMENT '{SortDescribed1:’’ , SortDescribed2: ‘’, SortDescribed3: ‘’}',
  DescribedRoom text NOT NULL,
  DescribedRestaurant text NOT NULL,
  PRIMARY KEY (HotelID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE hotel
ADD CONSTRAINT FK_Hotel_PartnerID FOREIGN KEY (PartnerID)
REFERENCES listpartner (RefID);


--
-- Create table `room`
--
CREATE TABLE room (
  RoomID char(36) NOT NULL DEFAULT '',
  HotelID char(36) DEFAULT NULL,
  RoomCode char(20) DEFAULT NULL,
  RoomName varchar(255) DEFAULT NULL,
  Described text DEFAULT NULL,
  Amount int DEFAULT NULL,
  Acreage float DEFAULT NULL,
  AdultMaximum int DEFAULT NULL,
  ChildMaximum int DEFAULT NULL,
  BabyMaximum int DEFAULT NULL,
  PRIMARY KEY (RoomID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE room
ADD CONSTRAINT FK_Room_HotelID FOREIGN KEY (HotelID)
REFERENCES hotel (HotelID);


--
-- Create table `roomtype`
--
CREATE TABLE roomtype (
  RoomTypeID char(36) NOT NULL DEFAULT '',
  RoomID char(36) DEFAULT NULL,
  Name varchar(50) DEFAULT NULL,
  Detail text DEFAULT NULL,
  Cost int DEFAULT NULL,
  CancelPolicy text DEFAULT NULL,
  SortOrder int DEFAULT NULL,
  PRIMARY KEY (RoomTypeID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE roomtype
ADD CONSTRAINT FK_RoomType_RoomID FOREIGN KEY (RoomID)
REFERENCES room (RoomID);


--
-- Create table `listbookroom`
--
CREATE TABLE listbookroom (
  RefID char(36) NOT NULL DEFAULT '',
  RoomID char(36) NOT NULL DEFAULT '',
  UserID char(36) NOT NULL DEFAULT '',
  RefCode char(20) DEFAULT NULL,
  TotalCost int DEFAULT NULL,
  RoomTypeID char(36) DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE listbookroom
ADD CONSTRAINT FK_ListBookRoom_RoomID FOREIGN KEY (RoomID)
REFERENCES room (RoomID);

--
-- Create foreign key
--
ALTER TABLE listbookroom
ADD CONSTRAINT FK_listbookroom_RoomTypeID FOREIGN KEY (RoomTypeID)
REFERENCES roomtype (RoomTypeID);

--
-- Create foreign key
--
ALTER TABLE listbookroom
ADD CONSTRAINT FK_ListBookRoom_UserID FOREIGN KEY (UserID)
REFERENCES user (UserID);


--
-- Create table `restaurant`
--
CREATE TABLE restaurant (
  RestaurantID char(36) NOT NULL DEFAULT '',
  HotelID char(36) DEFAULT NULL,
  Name varchar(50) DEFAULT NULL,
  TypeOfFood varchar(255) DEFAULT NULL,
  Described text DEFAULT NULL,
  OpenTime time DEFAULT NULL,
  PhoneNumber char(20) DEFAULT NULL,
  Menu text DEFAULT NULL COMMENT '{Item:’, Cost:’’’}',
  PRIMARY KEY (RestaurantID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE restaurant
ADD CONSTRAINT FK_Restaurant_HotelID FOREIGN KEY (HotelID)
REFERENCES hotel (HotelID);

--
-- Create table `listbookrestaurant`
--
CREATE TABLE listbookrestaurant (
  RefID char(36) NOT NULL DEFAULT '',
  RestaurantID char(36) DEFAULT NULL,
  UserID char(36) DEFAULT NULL,
  Amount int DEFAULT NULL,
  Time datetime DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE listbookrestaurant
ADD CONSTRAINT FK_ListBookRestaurant_RestaurantID FOREIGN KEY (RestaurantID)
REFERENCES restaurant (RestaurantID);

--
-- Create foreign key
--
ALTER TABLE listbookrestaurant
ADD CONSTRAINT FK_ListBookRestaurant_UserID FOREIGN KEY (UserID)
REFERENCES user (UserID);


--
-- Create table `nearby`
--
CREATE TABLE nearby (
  RefID char(36) NOT NULL DEFAULT '',
  HotelID char(36) DEFAULT NULL,
  DistrictID char(36) DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE nearby
ADD CONSTRAINT FK_NearBy_DistrictID FOREIGN KEY (DistrictID)
REFERENCES district (DistrictID);

--
-- Create foreign key
--
ALTER TABLE nearby
ADD CONSTRAINT FK_NearBy_HotelID FOREIGN KEY (HotelID)
REFERENCES hotel (HotelID);