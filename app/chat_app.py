import azure.functions as func
import logging

chat_app_bp = func.Blueprint()


@chat_app_bp.function_name(name="chat")
@chat_app_bp.route(route="chat", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse("Hello from Chat", status_code=200)
