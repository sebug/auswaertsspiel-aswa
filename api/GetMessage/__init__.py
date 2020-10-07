import logging
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    message_text = os.environ["MESSAGE_TEXT"]
    logging.info(f'The message text is {message_text}')
    # This should now have landed in App Insights

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"{message_text} {name}")
    else:
        return func.HttpResponse(
            message_text,
             status_code=200
        )
