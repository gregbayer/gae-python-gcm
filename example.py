
from gae_python_gcm.gcm import GCMMessage, GCMConnection

gcm_message = GCMMessage(device_profile.push_token, android_payload, android_collapse_id)
gcm_conn = GCMConnection()
logging.info("Attempting to send Android push notification %s to user id %s." % (str(android_payload), str(target_user_id)))
gcm_conn.notify_device(gcm_message)