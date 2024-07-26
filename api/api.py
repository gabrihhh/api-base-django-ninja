from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return {"message": "Hello World"}

@api.get("/tchau")
def hello(request):
    return {"message": "Tchau"}

@api.get("/welcome")
def hello(request):
    return {"message": "Welcome"}
