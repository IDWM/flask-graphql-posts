from flask import Flask
from flask_graphql import GraphQLView
from database import engine, Base, SessionLocal
from schema import schema

app = Flask(__name__)


def get_context():
    return {"session": SessionLocal()}


@app.teardown_appcontext
def shutdown_session(exception=None):
    SessionLocal.remove()


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,
        get_context=get_context,
    ),
)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)
