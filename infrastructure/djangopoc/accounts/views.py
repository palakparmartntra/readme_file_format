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
