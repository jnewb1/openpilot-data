from openpilot.tools.lib.logreader import LogIterable

PRESERVE_SERVICES = ["can", "carParams", "pandaStates", "pandaStateDEPRECATED"]

def sanetize(lr: LogIterable) -> bytes:
  return filter(lambda msg: msg.which() in PRESERVE_SERVICES, lr)
