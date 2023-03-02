#!/usr/bin/python3.8

from . import players_api_blueprint
from ariadne import load_schema_from_path, make_executable_schema, \
                    graphql_sync, snake_case_fallback_resolvers, ObjectType
from flask import request, jsonify, current_app
from .queries import getPlayers_resolver, getPlayer_resolver
from .mutations import createPlayer_resolver, updatePlayer_resolver, deletePlayer_resolver

query = ObjectType("Query")
query.set_field("getPlayers", getPlayers_resolver)
query.set_field("getPlayer", getPlayer_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createPlayer", createPlayer_resolver)
mutation.set_field("updatePlayer", updatePlayer_resolver)
mutation.set_field("deletePlayer", deletePlayer_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, mutation)

@players_api_blueprint.route('/', methods=['GET'])
def hello():
    return "Welcome to Voliboli!", 200

@players_api_blueprint.route('/players', methods=['POST'])
def hi():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=current_app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
