from rest_framework.decorators import api_view
from modules.common_utilities.di import obj_graph
from modules.user_module.business.user_module.services.user_service import UserService
from modules.user_module.business.user_module.Dtos.user_dto import UserDto
from rest_framework.response import Response


@api_view(["GET", "POST"])
def register(request):
    """
    for register user.
    """
    if request.method == "GET":
        users = obj_graph.provide(UserService)
        users_list = users.get_users()
        return Response(users_list)

    elif request.method == "POST":
        user = obj_graph.provide(UserService)
        dto = UserDto(
            username=request.data["username"], first_name=request.data["first_name"],
            last_name=request.data["last_name"], email=request.data["email"],
            birthdate=request.data["birthdate"], gender=request.data["gender"],
            password=request.data['password']
        )
        create_user = user.register(dto)
        return Response(create_user)


@api_view(["POST"])
def login(request):
    """
    for login
    """
    if request.method == "POST":
        user = obj_graph.provide(UserService)
        print(user)
        dto = UserDto(
            username=request.data["username"], first_name=None,
            last_name=None, email=None, birthdate=None,
            gender=None, password=request.data['password']
        )
        login_u = user.login_user(dto)
        return Response(login_u)


@api_view(["GET"])
def user_list(request):
    """
        for list of users.
    """
    if request.method == "GET":
        users = obj_graph.provide(UserService)
        users_list = users.get_users()
        return Response(users_list)
