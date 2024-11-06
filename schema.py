import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Post as PostModel
from database import SessionLocal


class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (graphene.relay.Node,)


class CreatePost(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    post = graphene.Field(lambda: Post)

    def mutate(self, info, nombre, descripcion):
        session = SessionLocal()
        try:
            post = PostModel(nombre=nombre, descripcion=descripcion)
            session.add(post)
            session.commit()
            session.refresh(post)
            return CreatePost(post=post)
        finally:
            session.close()


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(Post.connection)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
