from app.server import server

srv = server.Server()
app = srv.env.http.get_app()
db = srv.env.http.get_db()