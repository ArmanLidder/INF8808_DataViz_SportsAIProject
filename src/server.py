'''
    Contains the server to run our application.
'''
from flask_failsafe import failsafe
import time
import os

@failsafe
def create_app():
    '''
        Gets the underlying Flask server from our Dash app.

        Returns:
            The server to be run
    '''
    from app import app
    return app.server


if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    server = create_app()
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Time taken to create and run the app: {elapsed_time:.2f} seconds")

    port = int(os.environ.get("PORT", 8050))
    server.run(host="0.0.0.0", port=port, debug=False)
