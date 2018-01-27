from api import create_app


APP = create_app()
APP.run(host="0.0.0.0", port=8080, debug=True)
