
from gae_python_gcm.gcm import GCMMessage, GCMConnection

push_token = 'YOUR_PUSH_TOKEN'
android_payload = {'your-key': 'your-value'}
android_collapse_id = None

gcm_message = GCMMessage(push_token, android_payload, android_collapse_id)
gcm_conn = GCMConnection()
logging.info("Attempting to send Android push notification %s to user id %s." % (str(android_payload), str(target_user_id)))
gcm_conn.notify_device(gcm_message)