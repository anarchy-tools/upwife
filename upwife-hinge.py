from com.dtmilano.android.viewclient import ViewClient
import time

def get_view_client():
  device, serialno = ViewClient.connectToDeviceOrExit()
  vc = ViewClient(device, serialno)
  return vc

def target():
  print("targeting wife ...")
  vc = get_view_client()
  el = vc.findViewById('co.hinge.app:id/like_button')
  if el:
    el.touch()
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
    if target():
      time.sleep(2)
      swoop()
    time.sleep(3)
