import grpc 
from grpc_out.users_pb2 import AllUsersRequest, UserId
import grpc_out.users_pb2_grpc as users_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = users_grpc.UsersInfoStub(channel)

print(stub.GetAllUsersInfo(AllUsersRequest(max_result=3)))
print(stub.GetInfoById(UserId(user_id=1)))
