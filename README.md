# Flask GraphQL API

Este proyecto es una API construida con Flask, SQLAlchemy y GraphQL, utilizando Graphene para definir el esquema GraphQL. Proporciona un punto de acceso para interactuar con una base de datos de posts a través de consultas GraphQL.

## Requisitos

- Python 3.7 o superior. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- Virtualenv (opcional, pero recomendado).

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/IDWM/flask-graphql-posts.git
   cd flask-graphql-posts
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicia la aplicación:

   ```bash
   python app.py
   ```

5. Accede a la interfaz de GraphQL:

   Abre tu navegador y ve a `http://127.0.0.1:5000/graphql` para interactuar con la API usando GraphiQL.

## Uso

Puedes realizar consultas y mutaciones a través de la interfaz de GraphQL. Aquí tienes algunos ejemplos:

### Obtener todos los posts

```graphql
{
  allPosts {
    edges {
      node {
        id
        nombre
        descripcion
      }
    }
  }
}
```

### Crear un nuevo post

Para crear un nuevo post, puedes usar la siguiente mutación:

```graphql
mutation {
  createPost(input: {nombre: "Nuevo Post", descripcion: "Descripción del nuevo post"}) {
    post {
      id
      nombre
      descripcion
    }
  }
}
```