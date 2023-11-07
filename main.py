from app import app


# flask shell
@app.shell_context_processor
def make_shell_conext():
    return {
        # variables
    }
