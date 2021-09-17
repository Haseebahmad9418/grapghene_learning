from typing import AsyncGenerator
from graphene import ObjectType, String, Schema
from graphene.types.scalars import Int

class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"), age=Int(default_value=13))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name, age):
        return f"[{{\"name\": {name}, \"age\": {age}}}]"

    def resolve_goodbye(root, info):
        return 'See ya!'



def main():
    schema = Schema(query=Query)
    query_string = '{ hello (name: "bob")  }'
    result = schema.execute(query_string)
    print(result.data['hello'])
    pass 



if __name__ == "__main__":
    main()
