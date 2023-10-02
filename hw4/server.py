import grpc
import grpc_out.users_pb2_grpc as users_grpc
from grpc_out.users_pb2 import UserInfo, AllUsersResponse
from users_info import users
from concurrent import futures


class UserInfoServicer(users_grpc.UsersInfoServicer):
    def GetInfoById(self, request, context):
        if request.user_id <= 0 or request.user_id > len(users):
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, 'Invalid user id')
        
        user = users[request.user_id - 1]
        return UserInfo(name=user['name'], family=user['family'], email=user['email'])
    

    def GetAllUsersInfo(self, request, context):
        if request.max_result <= 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, 'max_result must be > 0')
        
        res = [UserInfo(name=user['name'], family=user['family'], email=user['email']) for user in users]
        return AllUsersResponse(user=res[:request.max_result])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_grpc.add_UsersInfoServicer_to_server(UserInfoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()