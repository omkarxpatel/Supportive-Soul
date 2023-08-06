from firebase_admin import firestore, credentials, initialize_app
from colorama import Fore

cred = credentials.Certificate("supportive-soul-firebase-credentials.json")
initialize_app(cred)
DATABASE = firestore.client()
print(f"Connected to: {Fore.GREEN}Firebase Database{Fore.RESET}")


def set_user(username, data):
    doc_ref = DATABASE.collection("users").document(username)
    doc_ref.set(data)


def get_user(username):
    doc_ref = DATABASE.collection("users").document(username)
    if not doc_ref.get().exists:
        doc_ref.set({})

    user = doc_ref.get().to_dict()

    if "message_history" not in user:
        user["message_history"] = []
    if "suicide_history" not in user:
        user["suicide_history"] = []
    if "flag_messages" not in user:
        user["flag_messages"] = True  # Default value, messages will be scanned by default

    set_user(username, user)

    return user


# FOR FLAGGING LOGGING


def set_logging_channel(server_id, channel_id):
    try:
        doc_ref = DATABASE.collection("logging_channels").document(server_id)
        doc_ref.set({"channel_id": channel_id})
        return True
    except Exception as e:
        return e


def get_logging_channel(server_id):
    try:
        doc_ref = DATABASE.collection("logging_channels").document(server_id)
        doc = doc_ref.get()

        if doc.exists:
            return doc.to_dict().get("channel_id", None)
        else:
            return None
    except Exception as e:
        return e


# FOR FLAGGING MESSAGE SCANNING


def set_message_scanning_flag(server_id, flag_value):
    try:
        doc_ref = DATABASE.collection("message_scanning_flags").document(server_id)
        doc_ref.set({"flag_messages": flag_value})
        return flag_value
    except Exception as e:
        return e


def get_message_scanning_flag(server_id):
    try:
        doc_ref = DATABASE.collection("message_scanning_flags").document(server_id)
        doc = doc_ref.get()

        if doc.exists:
            return doc.to_dict()  # Default value, messages will be scanned by default
        else:
            return True  # Default value, messages will be scanned by default
    except Exception as e:
        return e
