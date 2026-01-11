from prefect import task
from datetime import datetime

@task
def transform(data):
    """
    transformamos la data de randomuser
    """
    transform_data = []
    for user in data:
        nombre = f"{user['name']['first']} {user['name']['last']}"
        sexo = user['gender']
        pais = user['location']['country']
        fecha_nac = user['dob']['date']
        fecha_nac = datetime.fromisoformat(fecha_nac.rstrip("Z")).date()
        transform_data.append((nombre,sexo,pais,fecha_nac))
    return transform_data