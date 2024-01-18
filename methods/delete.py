from prisma import Prisma
from flask import jsonify

prisma = Prisma()
prisma.connect()

def delete(skill_id):
    """
    Delete an existing skill from the database.

    :param skill_id: The ID of the skill to be deleted.
    :return: A response object with a status code.
    """
    response = {}
    header = {'Content-Type': 'application/json'}

    try:
        deleted_skill = prisma.skill.delete({
            'where': {'id': skill_id}
        })

        if deleted_skill:
            response['message'] = 'Skill successfully deleted'
            return jsonify(response), 200, header
        else:
            response['message'] = 'Skill not found'
            return jsonify(response), 404, header

    except Exception as e:
        
        response['message'] = str(e)
        return jsonify(response), 500, header