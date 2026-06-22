from pydantic_settings import BaseSettings

class Config(BaseSettings):

    debug_tool: bool = False
    db_user: str = ''
    db_password: str = ''
    db_name: str = 'notes.db'




    @property
    def db_url(self):
        return f"sqlite:///./{self.db_name}"

config = Config()