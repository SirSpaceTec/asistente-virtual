

orders = ["apagar asistente"]

def interactionOrOrder(text):
  if text.lower() in orders:
    # Logica para enviar orden a C
    return "order"
  else:
    return "interaction"
