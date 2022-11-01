from com.dtmilano.android.viewclient import ViewClient, AdbClient
import time

def get_view_client():
  device, serialno = ViewClient.connectToDeviceOrExit()
  vc = ViewClient(device, serialno)
  return vc

def maybe_click(vc, view_id):
  el = vc.findViewById(view_id)
  if el:
    el.touch()
    return True
  return False

def target():
  print("targeting wife ...")
  vc = get_view_client()
  if maybe_click(vc, 'co.hinge.app:id/like_button'):
    return True
  elif maybe_click(vc, 'co.hinge.app:id/likeButton'):
    return True
  elif maybe_click(vc, 'co.hinge.app:id/undo_button'):
    return True
  elif maybe_click(vc, 'co.hinge.app:id/dialog_primary_button'):
    return True
  elif swoop():
    return True
  return False

def swoop():
  print("swooping!")
  vc = get_view_client()
  el = vc.findViewById('co.hinge.app:id/send_like_button')
  if el:
    el.touch()
    print("payload delivered")
    return True
  return False


if __name__ == '__main__':
  while True:
    try:
      if target():
        time.sleep(2)
        swoop()
      time.sleep(3)
    except:
      print("error")
