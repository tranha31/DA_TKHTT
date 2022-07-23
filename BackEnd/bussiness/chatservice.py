from repository.chatrepository import ChatRepository


class ChatService:
    dl = None

    def __init__(self) -> None:
        self.dl = ChatRepository()

    def getChatRoomByUserID(self, UserID):
        result = self.dl.getChatRoomByUserID(UserID)

        if (result is None or len(result) <= 0 or len(result) > 1):
            return None
        else:
            newRoom = result[0]
            return newRoom

    def createNewChatRoom(self, UserID):
        result = self.dl.createNewChatRoom(UserID)

        return "Create New Chat Room Success!"

    def loadAllChatRoom(self):
        result = self.dl.loadAllChatRoom()
        return result

    def loadAllChatRoomByAmount(self, amount):
        result = self.dl.loadAllChatRoomByAmount(amount)
        return result
